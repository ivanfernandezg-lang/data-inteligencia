#!/usr/bin/env python3
"""
Explorador eficiente de libros y PDFs pesados.

Diseñado para `data/raw/Libros/` (Bishop, Hastie, Han, Haykin, etc.) donde los
archivos pueden superar los 50 MB y miles de páginas. Permite obtener contexto
útil del libro **sin cargarlo completo en memoria** ni extraer todo el texto.

Modos disponibles:
  --info            Metadata + resumen rápido (páginas, tamaño, tiene_toc)
  --toc             Tabla de contenidos (índice) si está embebida en el PDF
  --first-pages N   Extrae las primeras N páginas (default 10) — útil para portada,
                    prefacio e índice manual
  --pages a-b       Extrae un rango específico de páginas
  --search "term"   Busca un término y devuelve páginas + snippets de contexto
  --outline-md      Genera un Markdown de outline (TOC + primeras líneas de cada
                    capítulo detectado en el TOC)

Salida:
  Por defecto a stdout (resumido). Con --save guarda en
  `data/processed/libros/<slug>/<modo>.md` o `.json`.

Uso:
  python scripts/utils/book_explorer.py "data/raw/Libros/" --info
  python scripts/utils/book_explorer.py "data/raw/Libros/Bishop.pdf" --toc
  python scripts/utils/book_explorer.py "data/raw/Libros/Bishop.pdf" --first-pages 20 --save
  python scripts/utils/book_explorer.py "data/raw/Libros/Bishop.pdf" --search "backpropagation"
  python scripts/utils/book_explorer.py "data/raw/Libros/Haykin.pdf" --pages 100-120

Notas de eficiencia:
  - Abre el PDF una sola vez por modo y cierra inmediatamente.
  - Para --search, recorre página a página y descarta el texto tras buscar
    (no acumula el documento en memoria).
  - Para libros sin TOC embebido, sugiere usar --first-pages para leer el
    índice impreso manualmente.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

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
    for char in " .,;:()[]{}!¡¿?'\"":
        slug = slug.replace(char, "-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-").lower()


def collect_pdfs(target: Path) -> list[Path]:
    """Si target es un directorio devuelve todos los .pdf, si es archivo lo devuelve."""
    if target.is_file() and target.suffix.lower() == ".pdf":
        return [target]
    if target.is_dir():
        return sorted(target.rglob("*.pdf"))
    return []


def output_dir_for(pdf_path: Path, root: Path) -> Path:
    """Carpeta de salida en data/processed/libros/<slug>/."""
    out = root / "data" / "processed" / "libros" / slugify(pdf_path.name)
    out.mkdir(parents=True, exist_ok=True)
    return out


# ─────────────────────────────────────────────
# Modo: info
# ─────────────────────────────────────────────

def book_info(pdf_path: Path) -> dict[str, Any]:
    """Resumen rápido sin leer el contenido de las páginas."""
    doc = pymupdf.open(str(pdf_path))
    try:
        toc = doc.get_toc(simple=True)  # liviano: solo títulos
        meta = {k: v for k, v in (doc.metadata or {}).items() if v}
        info = {
            "archivo": pdf_path.name,
            "ruta": str(pdf_path),
            "paginas": len(doc),
            "tamano_mb": round(pdf_path.stat().st_size / (1024 * 1024), 2),
            "metadata": meta,
            "tiene_toc_embebido": bool(toc),
            "entradas_toc": len(toc),
            "max_nivel_toc": max((lvl for lvl, *_ in toc), default=0),
        }
    finally:
        doc.close()
    return info


def print_info(info: dict[str, Any]) -> None:
    print(f"\n📚 {info['archivo']}")
    print(f"   Páginas: {info['paginas']:,} | Tamaño: {info['tamano_mb']} MB")
    print(f"   TOC embebido: {'✅' if info['tiene_toc_embebido'] else '❌'}", end="")
    if info["tiene_toc_embebido"]:
        print(f" ({info['entradas_toc']} entradas, profundidad {info['max_nivel_toc']})")
    else:
        print(" — usar --first-pages para leer el índice impreso")
    if info["metadata"]:
        autor = info["metadata"].get("author", "?")
        titulo = info["metadata"].get("title", "?")
        print(f"   Autor: {autor} | Título: {titulo}")


# ─────────────────────────────────────────────
# Modo: TOC
# ─────────────────────────────────────────────

def book_toc(pdf_path: Path) -> list[dict[str, Any]]:
    """Tabla de contenidos embebida (si existe)."""
    doc = pymupdf.open(str(pdf_path))
    try:
        toc = doc.get_toc(simple=True)
    finally:
        doc.close()
    return [{"nivel": lvl, "titulo": title, "pagina": page} for lvl, title, page in toc]


def format_toc(toc: list[dict[str, Any]]) -> str:
    if not toc:
        return "_(Este PDF no tiene tabla de contenidos embebida)_\n"
    lines: list[str] = []
    for entry in toc:
        indent = "  " * (entry["nivel"] - 1)
        lines.append(f"{indent}- p.{entry['pagina']:>4}  {entry['titulo']}")
    return "\n".join(lines)


# ─────────────────────────────────────────────
# Modo: first-pages / pages
# ─────────────────────────────────────────────

def extract_pages(pdf_path: Path, page_range: Iterable[int]) -> list[dict[str, Any]]:
    """Extrae texto de un rango de páginas (1-indexed)."""
    doc = pymupdf.open(str(pdf_path))
    pages: list[dict[str, Any]] = []
    try:
        total = len(doc)
        for n in page_range:
            if n < 1 or n > total:
                continue
            page = doc[n - 1]
            text = page.get_text("text").strip()
            pages.append({"pagina": n, "texto": text})
    finally:
        doc.close()
    return pages


def parse_range(text: str) -> list[int]:
    """Parsea '1-10' o '5,7,12' a lista de enteros."""
    out: list[int] = []
    for chunk in text.split(","):
        chunk = chunk.strip()
        if "-" in chunk:
            a, b = chunk.split("-", 1)
            out.extend(range(int(a), int(b) + 1))
        elif chunk:
            out.append(int(chunk))
    return out


def format_pages_md(pages: list[dict[str, Any]], titulo: str) -> str:
    out = [f"# {titulo}\n"]
    for p in pages:
        out.append(f"\n## Página {p['pagina']}\n")
        out.append(p["texto"] if p["texto"] else "_(página vacía o solo imágenes)_")
        out.append("\n")
    return "\n".join(out)


# ─────────────────────────────────────────────
# Modo: search
# ─────────────────────────────────────────────

def search_term(pdf_path: Path, term: str, context_chars: int = 240,
                max_hits: int = 50) -> list[dict[str, Any]]:
    """
    Busca `term` (case-insensitive, regex permitida) y devuelve hits con snippet.
    Recorre página por página sin acumular el texto del libro completo.
    """
    pattern = re.compile(term, re.IGNORECASE)
    doc = pymupdf.open(str(pdf_path))
    hits: list[dict[str, Any]] = []
    try:
        for n in range(len(doc)):
            text = doc[n].get_text("text")
            if not text:
                continue
            for m in pattern.finditer(text):
                start = max(0, m.start() - context_chars // 2)
                end = min(len(text), m.end() + context_chars // 2)
                snippet = text[start:end].replace("\n", " ").strip()
                hits.append({
                    "pagina": n + 1,
                    "match": m.group(0),
                    "snippet": snippet,
                })
                if len(hits) >= max_hits:
                    return hits
    finally:
        doc.close()
    return hits


def format_hits(hits: list[dict[str, Any]], term: str) -> str:
    if not hits:
        return f"_Sin coincidencias para «{term}»._\n"
    out = [f"# Resultados de búsqueda: «{term}» ({len(hits)} hits)\n"]
    for h in hits:
        out.append(f"\n### Página {h['pagina']}")
        out.append(f"`{h['match']}` → {h['snippet']}")
    return "\n".join(out)


# ─────────────────────────────────────────────
# Modo: outline-md
# ─────────────────────────────────────────────

def build_outline(pdf_path: Path, lines_per_section: int = 3) -> str:
    """Genera Markdown con TOC + primeras líneas de cada capítulo del TOC."""
    info = book_info(pdf_path)
    toc = book_toc(pdf_path)

    out = [f"# Outline — {info['archivo']}\n"]
    out.append(f"- Páginas: {info['paginas']:,} | Tamaño: {info['tamano_mb']} MB")
    out.append(f"- TOC embebido: {info['tiene_toc_embebido']} ({info['entradas_toc']} entradas)\n")

    if not toc:
        out.append("_(Sin TOC embebido — usa `--first-pages` para revisar el índice impreso)_\n")
        return "\n".join(out)

    out.append("## Tabla de Contenidos\n")
    out.append(format_toc(toc))
    out.append("\n## Primeras líneas por sección de nivel 1\n")

    nivel1 = [e for e in toc if e["nivel"] == 1]
    doc = pymupdf.open(str(pdf_path))
    try:
        for entry in nivel1:
            n = entry["pagina"]
            if n < 1 or n > len(doc):
                continue
            text = doc[n - 1].get_text("text").strip()
            primeras = "\n".join(text.splitlines()[:lines_per_section])
            out.append(f"\n### p.{n} · {entry['titulo']}\n")
            out.append(primeras if primeras else "_(página vacía)_")
    finally:
        doc.close()

    return "\n".join(out)


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Explorador eficiente de libros/PDFs pesados.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument("target", type=Path, help="Archivo PDF o carpeta")
    grp = ap.add_mutually_exclusive_group(required=False)
    grp.add_argument("--info", action="store_true", help="Resumen rápido")
    grp.add_argument("--toc", action="store_true", help="Tabla de contenidos embebida")
    grp.add_argument("--first-pages", type=int, metavar="N", help="Extrae las primeras N páginas")
    grp.add_argument("--pages", type=str, metavar="RANGE", help="Rango: 1-10 o 5,7,12")
    grp.add_argument("--search", type=str, metavar="TERM", help="Buscar término (regex)")
    grp.add_argument("--outline-md", action="store_true", help="Outline (TOC + primeras líneas)")
    ap.add_argument("--save", action="store_true",
                    help="Guarda salida en data/processed/libros/<slug>/")
    ap.add_argument("--max-hits", type=int, default=50,
                    help="Máximo de coincidencias para --search (default 50)")

    args = ap.parse_args()
    root = get_project_root()
    pdfs = collect_pdfs(args.target)
    if not pdfs:
        print(f"❌ No se encontraron PDFs en {args.target}", file=sys.stderr)
        return 1

    # Modo por defecto: --info
    if not any([args.info, args.toc, args.first_pages, args.pages, args.search, args.outline_md]):
        args.info = True

    for pdf in pdfs:
        try:
            if args.info:
                info = book_info(pdf)
                print_info(info)
                if args.save:
                    (output_dir_for(pdf, root) / "info.json").write_text(
                        json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8"
                    )

            elif args.toc:
                toc = book_toc(pdf)
                md = f"# TOC — {pdf.name}\n\n" + format_toc(toc)
                if args.save:
                    (output_dir_for(pdf, root) / "toc.md").write_text(md, encoding="utf-8")
                    print(f"✅ {pdf.name}: TOC guardado ({len(toc)} entradas)")
                else:
                    print(md)

            elif args.first_pages:
                pages = extract_pages(pdf, range(1, args.first_pages + 1))
                md = format_pages_md(pages, f"Primeras {args.first_pages} páginas — {pdf.name}")
                if args.save:
                    (output_dir_for(pdf, root) / f"first-{args.first_pages}.md").write_text(md, encoding="utf-8")
                    print(f"✅ {pdf.name}: {len(pages)} páginas guardadas")
                else:
                    print(md)

            elif args.pages:
                rng = parse_range(args.pages)
                pages = extract_pages(pdf, rng)
                md = format_pages_md(pages, f"Páginas {args.pages} — {pdf.name}")
                if args.save:
                    safe = args.pages.replace(",", "_").replace("-", "to")
                    (output_dir_for(pdf, root) / f"pages-{safe}.md").write_text(md, encoding="utf-8")
                    print(f"✅ {pdf.name}: {len(pages)} páginas guardadas")
                else:
                    print(md)

            elif args.search:
                hits = search_term(pdf, args.search, max_hits=args.max_hits)
                md = format_hits(hits, args.search)
                if args.save:
                    safe = re.sub(r"[^a-zA-Z0-9]+", "-", args.search).strip("-").lower()
                    (output_dir_for(pdf, root) / f"search-{safe}.md").write_text(md, encoding="utf-8")
                    print(f"✅ {pdf.name}: {len(hits)} hits guardados para «{args.search}»")
                else:
                    print(md)

            elif args.outline_md:
                md = build_outline(pdf)
                if args.save:
                    (output_dir_for(pdf, root) / "outline.md").write_text(md, encoding="utf-8")
                    print(f"✅ {pdf.name}: outline guardado")
                else:
                    print(md)

        except Exception as e:
            print(f"❌ Error procesando {pdf.name}: {e}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
