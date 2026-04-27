#!/usr/bin/env python3
"""
Extractor universal de contenido PDF.

Extrae texto, tablas e imágenes de archivos PDF usando PyMuPDF.
Soporta PDFs nativos (texto seleccionable) y escaneados (OCR).

Uso:
  # Extraer texto de un PDF
  python scripts/utils/pdf_extractor.py data/raw/clases/archivo.pdf

  # Extraer texto de todos los PDFs de una carpeta
  python scripts/utils/pdf_extractor.py data/raw/clases/

  # Extraer con tablas e imágenes
  python scripts/utils/pdf_extractor.py data/raw/clases/archivo.pdf --tables --images

  # Exportar a Markdown
  python scripts/utils/pdf_extractor.py data/raw/clases/archivo.pdf --format md

  # Solo info del PDF (sin extraer contenido)
  python scripts/utils/pdf_extractor.py data/raw/clases/archivo.pdf --info

  # Extraer con OCR (para PDFs escaneados/imágenes)
  python scripts/utils/pdf_extractor.py data/raw/clases/archivo.pdf --ocr

Salida:
  Por defecto escribe en data/processed/{nombre_pdf}/
  Se puede cambiar con --output
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import pymupdf


# ─────────────────────────────────────────────
# Utilidades
# ─────────────────────────────────────────────

def get_project_root() -> Path:
    """Busca la raíz del proyecto (donde está .github/)."""
    current = Path(__file__).resolve().parent
    for _ in range(5):
        if (current / ".github").is_dir():
            return current
        current = current.parent
    return Path.cwd()


def slugify(name: str) -> str:
    """Convierte nombre de archivo a slug limpio para carpeta."""
    slug = name.replace(".pdf", "").replace(".PDF", "")
    # Reemplazar caracteres problemáticos
    for char in " .,;:()[]{}!¡¿?'\"":
        slug = slug.replace(char, "-")
    # Limpiar guiones múltiples
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-").lower()


# ─────────────────────────────────────────────
# Extracción de información
# ─────────────────────────────────────────────

def get_pdf_info(pdf_path: Path) -> dict[str, Any]:
    """Obtiene metadata e información general del PDF."""
    doc = pymupdf.open(str(pdf_path))

    info: dict[str, Any] = {
        "archivo": pdf_path.name,
        "paginas": len(doc),
        "tamaño_mb": round(pdf_path.stat().st_size / (1024 * 1024), 2),
        "metadata": {},
        "tiene_texto": False,
        "tiene_imagenes": False,
        "tiene_tablas": False,
        "paginas_detalle": [],
    }

    # Metadata del documento
    meta = doc.metadata
    if meta:
        info["metadata"] = {k: v for k, v in meta.items() if v}

    for page_num in range(len(doc)):
        page = doc[page_num]
        page_info: dict[str, Any] = {
            "pagina": page_num + 1,
            "ancho": round(page.rect.width),
            "alto": round(page.rect.height),
        }

        # Verificar texto
        text = page.get_text("text").strip()
        if text:
            info["tiene_texto"] = True
            page_info["caracteres"] = len(text)
            page_info["palabras"] = len(text.split())

        # Verificar imágenes
        images = page.get_images(full=True)
        if images:
            info["tiene_imagenes"] = True
            page_info["imagenes"] = len(images)

        # Verificar tablas
        tables = page.find_tables()
        if tables.tables:
            info["tiene_tablas"] = True
            page_info["tablas"] = len(tables.tables)

        info["paginas_detalle"].append(page_info)

    doc.close()
    return info


def print_pdf_info(info: dict[str, Any]) -> None:
    """Imprime información del PDF de forma legible."""
    print(f"\n📄 {info['archivo']}")
    print(f"   Páginas: {info['paginas']} | Tamaño: {info['tamaño_mb']} MB")
    print(f"   Texto: {'✅' if info['tiene_texto'] else '❌'} | "
          f"Imágenes: {'✅' if info['tiene_imagenes'] else '❌'} | "
          f"Tablas: {'✅' if info['tiene_tablas'] else '❌'}")

    if info["metadata"]:
        print(f"   Metadata: {info['metadata']}")

    # Resumen de contenido
    total_words = sum(p.get("palabras", 0) for p in info["paginas_detalle"])
    total_images = sum(p.get("imagenes", 0) for p in info["paginas_detalle"])
    total_tables = sum(p.get("tablas", 0) for p in info["paginas_detalle"])

    print(f"   Total: ~{total_words:,} palabras, {total_images} imágenes, {total_tables} tablas")

    if not info["tiene_texto"] and info["tiene_imagenes"]:
        print("   ⚠️  PDF escaneado (solo imágenes) — usa --ocr para extraer texto")


# ─────────────────────────────────────────────
# Extracción de texto
# ─────────────────────────────────────────────

def extract_text(pdf_path: Path, use_ocr: bool = False) -> list[dict[str, Any]]:
    """
    Extrae texto de cada página del PDF.

    Args:
        pdf_path: Ruta al archivo PDF.
        use_ocr: Si True, usa OCR para páginas sin texto nativo.

    Returns:
        Lista de dicts con {pagina, texto}.
    """
    doc = pymupdf.open(str(pdf_path))
    pages: list[dict[str, Any]] = []

    for page_num in range(len(doc)):
        page = doc[page_num]

        # Primero intentar texto nativo
        text = page.get_text("text").strip()

        # Si no hay texto y se pidió OCR, intentar OCR
        if not text and use_ocr:
            try:
                tp = page.get_textpage_ocr(flags=0, full=True)
                text = page.get_text("text", textpage=tp).strip()
                if text:
                    text = f"[OCR] {text}"
            except Exception as e:
                text = f"[OCR ERROR] {e}"

        if text:
            pages.append({
                "pagina": page_num + 1,
                "texto": text,
            })

    doc.close()
    return pages


# ─────────────────────────────────────────────
# Extracción de tablas
# ─────────────────────────────────────────────

def extract_tables(pdf_path: Path) -> list[dict[str, Any]]:
    """
    Extrae tablas de cada página del PDF.

    Returns:
        Lista de dicts con {pagina, tabla_num, headers, filas, dataframe}.
    """
    doc = pymupdf.open(str(pdf_path))
    all_tables: list[dict[str, Any]] = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        tables = page.find_tables()

        for t_idx, table in enumerate(tables.tables):
            data = table.extract()
            if not data or len(data) < 2:
                continue

            headers = data[0]
            rows = data[1:]

            table_info: dict[str, Any] = {
                "pagina": page_num + 1,
                "tabla_num": t_idx + 1,
                "headers": headers,
                "filas": rows,
                "num_filas": len(rows),
                "num_columnas": len(headers),
            }

            # Intentar crear DataFrame
            try:
                import pandas as pd
                df = pd.DataFrame(rows, columns=headers)
                table_info["dataframe"] = df
            except Exception:
                pass

            all_tables.append(table_info)

    doc.close()
    return all_tables


# ─────────────────────────────────────────────
# Extracción de imágenes
# ─────────────────────────────────────────────

def extract_images(pdf_path: Path, output_dir: Path) -> list[dict[str, Any]]:
    """
    Extrae imágenes de cada página del PDF y las guarda.

    Returns:
        Lista de dicts con {pagina, archivo, ancho, alto, tipo}.
    """
    doc = pymupdf.open(str(pdf_path))
    images_info: list[dict[str, Any]] = []
    img_dir = output_dir / "images"
    img_dir.mkdir(parents=True, exist_ok=True)

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)

        for img_idx, img in enumerate(images):
            xref = img[0]
            try:
                pix = pymupdf.Pixmap(doc, xref)

                # Convertir CMYK a RGB si es necesario
                if pix.n - pix.alpha > 3:
                    pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

                # Determinar extensión
                ext = "png"
                filename = f"page{page_num + 1:03d}_img{img_idx + 1:02d}.{ext}"
                filepath = img_dir / filename

                pix.save(str(filepath))

                images_info.append({
                    "pagina": page_num + 1,
                    "archivo": str(filepath.relative_to(output_dir)),
                    "ancho": pix.width,
                    "alto": pix.height,
                })
            except Exception as e:
                images_info.append({
                    "pagina": page_num + 1,
                    "error": str(e),
                })

    doc.close()
    return images_info


# ─────────────────────────────────────────────
# Exportadores
# ─────────────────────────────────────────────

def export_text(pages: list[dict[str, Any]], output_path: Path) -> None:
    """Exporta texto plano."""
    with open(output_path, "w", encoding="utf-8") as f:
        for page in pages:
            f.write(f"--- Página {page['pagina']} ---\n\n")
            f.write(page["texto"])
            f.write("\n\n")
    print(f"  📝 Texto: {output_path}")


def export_markdown(
    pages: list[dict[str, Any]],
    tables: list[dict[str, Any]],
    images: list[dict[str, Any]],
    pdf_name: str,
    output_path: Path,
) -> None:
    """Exporta todo el contenido a Markdown."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# {pdf_name.replace('.pdf', '')}\n\n")
        f.write(f"> Extraído automáticamente con `pdf_extractor.py`\n\n")
        f.write("---\n\n")

        for page in pages:
            f.write(f"## Página {page['pagina']}\n\n")
            f.write(page["texto"])
            f.write("\n\n")

            # Tablas de esta página
            page_tables = [t for t in tables if t["pagina"] == page["pagina"]]
            for table in page_tables:
                f.write(f"### Tabla {table['tabla_num']} (Página {table['pagina']})\n\n")
                if table["headers"]:
                    # Header
                    f.write("| " + " | ".join(str(h) for h in table["headers"]) + " |\n")
                    f.write("| " + " | ".join("---" for _ in table["headers"]) + " |\n")
                    for row in table["filas"]:
                        f.write("| " + " | ".join(str(c) if c else "" for c in row) + " |\n")
                f.write("\n")

            # Imágenes de esta página
            page_images = [img for img in images if img.get("pagina") == page["pagina"]]
            for img in page_images:
                if "archivo" in img:
                    f.write(f"![Imagen]({img['archivo']})\n\n")

            f.write("---\n\n")

    print(f"  📄 Markdown: {output_path}")


def export_tables_csv(tables: list[dict[str, Any]], output_dir: Path) -> None:
    """Exporta tablas a CSV."""
    if not tables:
        return

    tables_dir = output_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)

    for table in tables:
        if "dataframe" in table:
            filename = f"page{table['pagina']:03d}_table{table['tabla_num']:02d}.csv"
            filepath = tables_dir / filename
            table["dataframe"].to_csv(filepath, index=False)
            print(f"  📊 Tabla: {filepath}")


# ─────────────────────────────────────────────
# Procesamiento principal
# ─────────────────────────────────────────────

def process_pdf(
    pdf_path: Path,
    output_dir: Path,
    *,
    extract_tables_flag: bool = False,
    extract_images_flag: bool = False,
    use_ocr: bool = False,
    output_format: str = "txt",
    info_only: bool = False,
) -> dict[str, Any]:
    """
    Procesa un PDF completo.

    Args:
        pdf_path: Ruta al PDF.
        output_dir: Carpeta de salida.
        extract_tables_flag: Extraer tablas.
        extract_images_flag: Extraer imágenes.
        use_ocr: Usar OCR para páginas sin texto.
        output_format: Formato de salida ('txt' o 'md').
        info_only: Solo mostrar info, no extraer.

    Returns:
        Dict con resumen de lo extraído.
    """
    if not pdf_path.exists():
        print(f"❌ No existe: {pdf_path}")
        return {}

    # Info siempre
    info = get_pdf_info(pdf_path)
    print_pdf_info(info)

    if info_only:
        return info

    # Crear directorio de salida
    output_dir.mkdir(parents=True, exist_ok=True)

    result: dict[str, Any] = {"archivo": pdf_path.name, "output": str(output_dir)}

    # Texto
    pages = extract_text(pdf_path, use_ocr=use_ocr)
    result["paginas_con_texto"] = len(pages)
    result["palabras_total"] = sum(len(p["texto"].split()) for p in pages)

    # Tablas
    tables: list[dict[str, Any]] = []
    if extract_tables_flag:
        tables = extract_tables(pdf_path)
        result["tablas_encontradas"] = len(tables)
        export_tables_csv(tables, output_dir)

    # Imágenes
    images: list[dict[str, Any]] = []
    if extract_images_flag:
        images = extract_images(pdf_path, output_dir)
        result["imagenes_extraidas"] = len([i for i in images if "archivo" in i])

    # Exportar
    if output_format == "md":
        md_path = output_dir / f"{slugify(pdf_path.name)}.md"
        export_markdown(pages, tables, images, pdf_path.name, md_path)
    else:
        txt_path = output_dir / f"{slugify(pdf_path.name)}.txt"
        export_text(pages, txt_path)

    # Guardar metadata
    meta_path = output_dir / "info.json"
    # Remover dataframes del JSON
    serializable_info = {k: v for k, v in info.items()}
    serializable_info.pop("paginas_detalle", None)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(serializable_info, f, indent=2, ensure_ascii=False)

    print(f"\n  ✅ Procesado: {result.get('palabras_total', 0):,} palabras extraídas → {output_dir}")
    return result


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extractor universal de contenido PDF (texto, tablas, imágenes).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  %(prog)s data/raw/clases/                          # Info de todos los PDFs
  %(prog)s data/raw/clases/archivo.pdf                # Extraer texto
  %(prog)s data/raw/clases/archivo.pdf --tables       # Extraer texto + tablas
  %(prog)s data/raw/clases/archivo.pdf --images       # Extraer texto + imágenes
  %(prog)s data/raw/clases/archivo.pdf --format md    # Exportar a Markdown
  %(prog)s data/raw/clases/archivo.pdf --ocr          # Usar OCR
  %(prog)s data/raw/clases/archivo.pdf --all          # Todo: texto + tablas + imágenes
  %(prog)s data/raw/clases/ --info                    # Solo info de cada PDF
        """,
    )

    parser.add_argument(
        "input",
        type=str,
        help="Ruta a un PDF o a una carpeta con PDFs.",
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Carpeta de salida. Por defecto: data/processed/{nombre_pdf}/",
    )
    parser.add_argument(
        "--format", "-f",
        choices=["txt", "md"],
        default="txt",
        help="Formato de salida: txt (default) o md (Markdown).",
    )
    parser.add_argument(
        "--tables", "-t",
        action="store_true",
        help="Extraer tablas a CSV.",
    )
    parser.add_argument(
        "--images", "-i",
        action="store_true",
        help="Extraer imágenes.",
    )
    parser.add_argument(
        "--ocr",
        action="store_true",
        help="Usar OCR para páginas sin texto nativo (PDFs escaneados).",
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Extraer todo: texto + tablas + imágenes.",
    )
    parser.add_argument(
        "--info",
        action="store_true",
        help="Solo mostrar información del PDF, sin extraer contenido.",
    )

    args = parser.parse_args()

    # Resolver --all
    if args.all:
        args.tables = True
        args.images = True

    # Resolver rutas
    root = get_project_root()
    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = root / input_path

    # Determinar PDFs a procesar
    pdfs: list[Path] = []
    if input_path.is_file() and input_path.suffix.lower() == ".pdf":
        pdfs = [input_path]
    elif input_path.is_dir():
        pdfs = sorted(input_path.glob("*.pdf"))
        if not pdfs:
            print(f"❌ No se encontraron PDFs en: {input_path}")
            sys.exit(1)
    else:
        print(f"❌ Ruta inválida: {input_path}")
        sys.exit(1)

    print(f"\n📚 Procesando {len(pdfs)} PDF(s)...\n")

    results: list[dict[str, Any]] = []

    for pdf_path in pdfs:
        # Determinar carpeta de salida
        if args.output:
            output_dir = Path(args.output)
            if not output_dir.is_absolute():
                output_dir = root / output_dir
        else:
            # Detectar si viene de data/raw/clases/ o data/raw/papers/ para subcarpeta
            try:
                rel_to_raw = pdf_path.parent.relative_to(root / "data" / "raw")
                output_dir = root / "data" / "processed" / rel_to_raw / slugify(pdf_path.name)
            except ValueError:
                output_dir = root / "data" / "processed" / slugify(pdf_path.name)

        result = process_pdf(
            pdf_path,
            output_dir,
            extract_tables_flag=args.tables,
            extract_images_flag=args.images,
            use_ocr=args.ocr,
            output_format=args.format,
            info_only=args.info,
        )
        results.append(result)

    # Resumen final
    if len(pdfs) > 1 and not args.info:
        print(f"\n{'─' * 50}")
        total_words = sum(r.get("palabras_total", 0) for r in results)
        total_tables = sum(r.get("tablas_encontradas", 0) for r in results)
        total_images = sum(r.get("imagenes_extraidas", 0) for r in results)
        print(f"📊 Resumen: {len(pdfs)} PDFs → {total_words:,} palabras")
        if args.tables:
            print(f"   Tablas: {total_tables}")
        if args.images:
            print(f"   Imágenes: {total_images}")
        print()


if __name__ == "__main__":
    main()
