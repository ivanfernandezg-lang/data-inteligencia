#!/usr/bin/env python3
"""
Regenera automáticamente las secciones de estructura en:
  - .github/copilot-instructions.md  (sección 1: ESTRUCTURA DEL PROYECTO)
  - README.md                        (sección: Estructura del proyecto)
  - documentation/README.md          (sección: Estructura de Documentación)

Uso:
  python scripts/utils/update_structure.py          # desde la raíz del proyecto
  python scripts/utils/update_structure.py --dry-run # solo muestra cambios, no escribe

El script lee la estructura real de carpetas y archivos, genera el árbol
actualizado, y reemplaza las secciones correspondientes en cada archivo.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

# ─────────────────────────────────────────────
# Configuración
# ─────────────────────────────────────────────

# Carpetas a ignorar al generar el árbol
IGNORE_DIRS: set[str] = {
    ".git", ".venv", "venv", "__pycache__", ".ipynb_checkpoints",
    "node_modules", ".DS_Store", ".idea",
}

# Archivos a ignorar
IGNORE_FILES: set[str] = {
    ".DS_Store", "Thumbs.db", ".gitkeep",
}

# Extensiones que se cuentan pero no se listan individualmente
BULK_EXTENSIONS: set[str] = {".pdf", ".csv", ".xlsx", ".xls", ".json", ".xml"}

# Máximo de archivos a listar por carpeta antes de resumir
MAX_FILES_PER_DIR: int = 8

# Descripciones conocidas de carpetas (se usan en copilot-instructions)
FOLDER_DESCRIPTIONS: dict[str, str] = {
    "data/raw/clases": "PDFs de presentaciones de clase",
    "data/raw/papers": "Papers y artículos de referencia",
    "data/raw/datasets": "Datasets para ejercicios y proyectos",
    "data/raw/docs": "Fuentes de información y links",
    "data/processed": "Datos procesados",
    "data/processed/clases": "Clases extraídas (MD, tablas CSV, imágenes)",
    "data/exports": "Datos para reportes o entregas",
    "notebooks/exploratory": "EDA y análisis exploratorio",
    "notebooks/ejercicios": "Ejercicios resueltos",
    "notebooks/reports": "Notebooks de entrega",
    "scripts/analysis": "Scripts de análisis y modelos",
    "scripts/utils": "Funciones reutilizables",
    "scripts/etl": "Procesamiento de datos",
    "documentation/reports": "Informes y entregas",
    "documentation/resumen-clases": "Resúmenes por clase",
    "documentation/investigacion": "Investigación bibliográfica",
    "documentation/proyectos": "Documentación por proyecto",
    "proyectos": "Código de proyectos y trabajos",
    "tests": "Tests de validación",
}


def get_project_root() -> Path:
    """Determina la raíz del proyecto (donde está .github/)."""
    # Intentar desde el script hacia arriba
    current = Path(__file__).resolve().parent
    for _ in range(5):
        if (current / ".github").is_dir():
            return current
        current = current.parent

    # Fallback: directorio actual
    cwd = Path.cwd()
    if (cwd / ".github").is_dir():
        return cwd

    print("❌ No se encontró la raíz del proyecto (.github/)")
    sys.exit(1)


def scan_tree(root: Path, base: Path, depth: int = 0, max_depth: int = 5) -> list[str]:
    """
    Escanea recursivamente y genera líneas de árbol estilo tree.

    Returns:
        Lista de líneas con formato de árbol.
    """
    if depth > max_depth:
        return []

    lines: list[str] = []
    try:
        entries = sorted(root.iterdir(), key=lambda e: (not e.is_dir(), e.name.lower()))
    except PermissionError:
        return []

    # Filtrar
    dirs = [e for e in entries if e.is_dir() and e.name not in IGNORE_DIRS]
    files = [e for e in entries if e.is_file() and e.name not in IGNORE_FILES]

    all_items = dirs + files
    for i, entry in enumerate(all_items):
        is_last = i == len(all_items) - 1
        prefix = "└── " if is_last else "├── "
        connector = "    " if is_last else "│   "

        if entry.is_dir():
            rel = entry.relative_to(base)
            desc = FOLDER_DESCRIPTIONS.get(str(rel), "")
            suffix = f"  # {desc}" if desc else ""
            lines.append(f"{prefix}{entry.name}/{suffix}")
            subtree = scan_tree(entry, base, depth + 1, max_depth)
            for subline in subtree:
                lines.append(f"{connector}{subline}")
        else:
            lines.append(f"{prefix}{entry.name}")

    # Si hay muchos archivos de un tipo, resumir
    if len(files) > MAX_FILES_PER_DIR:
        ext_counts: dict[str, int] = {}
        for f in files:
            ext = f.suffix.lower()
            ext_counts[ext] = ext_counts.get(ext, 0) + 1

        # Reconstruir solo si hay bulk files
        bulk_present = any(ext in BULK_EXTENSIONS for ext in ext_counts)
        if bulk_present:
            lines_filtered: list[str] = []
            for line in lines:
                # Mantener directorios y archivos no-bulk
                keep = True
                for ext in BULK_EXTENSIONS:
                    if line.strip().endswith(ext):
                        keep = False
                        break
                if keep:
                    lines_filtered.append(line)

            for ext, count in sorted(ext_counts.items()):
                if ext in BULK_EXTENSIONS and count > 3:
                    lines_filtered.append(f"├── ({count} archivos {ext})")

            return lines_filtered

    return lines


def generate_tree_string(root: Path) -> str:
    """Genera el string completo del árbol del proyecto."""
    tree_lines = scan_tree(root, root)
    project_name = root.name
    return f"{project_name}/\n" + "\n".join(tree_lines)


def generate_copilot_structure(root: Path) -> str:
    """
    Genera la sección de estructura para copilot-instructions.md.
    Formato: ruta → descripción
    """
    lines: list[str] = []
    for folder, desc in sorted(FOLDER_DESCRIPTIONS.items()):
        folder_path = root / folder
        if folder_path.exists():
            # Contar contenido
            count = sum(1 for f in folder_path.rglob("*") if f.is_file() and f.name not in IGNORE_FILES)
            count_str = f" ({count} archivos)" if count > 0 else ""
            lines.append(f"{folder + '/':<40} → {desc}{count_str}")
        else:
            lines.append(f"{folder + '/':<40} → {desc}")

    # Detectar carpetas nuevas no registradas en FOLDER_DESCRIPTIONS
    new_folders = detect_new_folders(root)
    if new_folders:
        lines.append("")
        lines.append("# --- Carpetas detectadas sin descripción ---")
        for folder in new_folders:
            lines.append(f"{folder + '/':<40} → ⚠️ Sin descripción (agregar en update_structure.py)")

    return "\n".join(lines)


def detect_new_folders(root: Path) -> list[str]:
    """Detecta carpetas con contenido que no están en FOLDER_DESCRIPTIONS."""
    known = set(FOLDER_DESCRIPTIONS.keys())
    # Carpetas de nivel 1 y 2 relevantes
    scan_roots = ["data", "notebooks", "scripts", "documentation", "proyectos", "tests"]

    new_folders: list[str] = []
    for scan_root in scan_roots:
        scan_path = root / scan_root
        if not scan_path.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(scan_path):
            # Filtrar directorios ignorados
            dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and d not in {"md", "mmd"}]

            rel = str(Path(dirpath).relative_to(root))
            if rel not in known and rel != scan_root:
                # Ignorar subcarpetas generadas por pdf_extractor dentro de processed/
                if "/processed/clases/" in rel or rel.startswith("data/processed/clases/"):
                    # Solo reportar data/processed/clases, no sus hijos
                    continue
                # Solo reportar si tiene archivos reales
                real_files = [f for f in filenames if f not in IGNORE_FILES]
                if real_files:
                    new_folders.append(rel)

    return sorted(new_folders)


def generate_class_table(root: Path) -> str:
    """Genera la tabla de materiales de clase del README."""
    clases_dir = root / "data" / "raw" / "clases"
    if not clases_dir.is_dir():
        return ""

    pdfs = sorted([f.name for f in clases_dir.iterdir() if f.suffix.lower() == ".pdf"])
    if not pdfs:
        return ""

    lines: list[str] = [
        "| # | Archivo | Tema |",
        "| --- | --- | --- |",
    ]

    for pdf in pdfs:
        # Intentar extraer número de clase
        match = re.match(r"^(\d+)", pdf)
        num = match.group(1) if match else "—"
        # Limpiar nombre para descripción
        name_clean = pdf.replace(".pdf", "").strip()
        # Remover número y separadores del inicio
        desc = re.sub(r"^\d+[\s\-\.]*", "", name_clean).strip()
        if not desc:
            desc = name_clean
        lines.append(f"| {num} | `{pdf}` | {desc} |")

    return "\n".join(lines)


def replace_section(
    content: str,
    start_marker: str,
    end_marker: str,
    new_content: str,
    wrap_in_code_block: bool = False,
) -> str:
    """
    Reemplaza el contenido entre dos marcadores en un string.
    Si wrap_in_code_block es True, envuelve new_content en ```...```
    """
    if wrap_in_code_block:
        new_content = f"```\n{new_content}\n```"

    pattern = re.compile(
        rf"({re.escape(start_marker)})\s*\n```[\s\S]*?```",
        re.MULTILINE,
    )

    if pattern.search(content):
        return pattern.sub(f"{start_marker}\n\n{new_content}", content, count=1)

    # Fallback: buscar entre marcadores simples
    pattern2 = re.compile(
        rf"({re.escape(start_marker)})\s*\n[\s\S]*?(?={re.escape(end_marker)})",
        re.MULTILINE,
    )
    if pattern2.search(content):
        return pattern2.sub(f"{start_marker}\n\n{new_content}\n\n", content, count=1)

    return content


# ─────────────────────────────────────────────
# Actualizadores por archivo
# ─────────────────────────────────────────────

def update_copilot_instructions(root: Path, dry_run: bool = False) -> bool:
    """Actualiza la sección ESTRUCTURA DEL PROYECTO en copilot-instructions.md."""
    filepath = root / ".github" / "copilot-instructions.md"
    if not filepath.exists():
        print(f"  ⚠️  No existe: {filepath}")
        return False

    content = filepath.read_text(encoding="utf-8")
    structure = generate_copilot_structure(root)

    # Buscar y reemplazar el bloque de código de la sección 1
    pattern = re.compile(
        r"(## 1\) ESTRUCTURA DEL PROYECTO\s*\n\s*\n```)\n[\s\S]*?(```)",
        re.MULTILINE,
    )

    if not pattern.search(content):
        print("  ⚠️  No se encontró la sección '## 1) ESTRUCTURA DEL PROYECTO' con bloque de código")
        return False

    new_content = pattern.sub(rf"\1\n{structure}\n\2", content)

    if new_content == content:
        print("  ✅ Sin cambios en copilot-instructions.md")
        return False

    if dry_run:
        print("  🔍 [DRY RUN] Cambios detectados en copilot-instructions.md:")
        print(f"     Estructura generada con {len(FOLDER_DESCRIPTIONS)} carpetas")
        new_folders = detect_new_folders(root)
        if new_folders:
            print(f"     ⚠️  Carpetas nuevas sin descripción: {', '.join(new_folders)}")
    else:
        filepath.write_text(new_content, encoding="utf-8")
        print("  ✅ Actualizado: copilot-instructions.md")

    return True


def update_readme(root: Path, dry_run: bool = False) -> bool:
    """Actualiza la sección Estructura del proyecto y tabla de clases en README.md."""
    filepath = root / "README.md"
    if not filepath.exists():
        print(f"  ⚠️  No existe: {filepath}")
        return False

    content = filepath.read_text(encoding="utf-8")
    changed = False

    # 1. Actualizar árbol de estructura
    tree = generate_tree_string(root)
    pattern_tree = re.compile(
        r"(## Estructura del proyecto\s*\n\s*\n```)\n[\s\S]*?(```)",
        re.MULTILINE,
    )

    if pattern_tree.search(content):
        new_content = pattern_tree.sub(rf"\1\n{tree}\n\2", content)
        if new_content != content:
            content = new_content
            changed = True

    # 2. Actualizar tabla de materiales de clase
    class_table = generate_class_table(root)
    if class_table:
        pattern_table = re.compile(
            r"(\| #[^\n]*\n\| ---[^\n]*\n)(\|[\s\S]*?)(?=\n\n|\n##|\Z)",
            re.MULTILINE,
        )
        if pattern_table.search(content):
            # Extraer solo las filas de datos de la tabla nueva
            table_rows = "\n".join(class_table.split("\n")[2:])
            new_content = pattern_table.sub(rf"\g<1>{table_rows}", content)
            if new_content != content:
                content = new_content
                changed = True

    if not changed:
        print("  ✅ Sin cambios en README.md")
        return False

    if dry_run:
        print("  🔍 [DRY RUN] Cambios detectados en README.md")
    else:
        filepath.write_text(content, encoding="utf-8")
        print("  ✅ Actualizado: README.md")

    return True


def update_documentation_readme(root: Path, dry_run: bool = False) -> bool:
    """Actualiza la sección de estructura en documentation/README.md."""
    filepath = root / "documentation" / "README.md"
    if not filepath.exists():
        print(f"  ⚠️  No existe: {filepath}")
        return False

    content = filepath.read_text(encoding="utf-8")
    doc_root = root / "documentation"

    # Generar árbol solo de documentation/
    tree_lines = scan_tree(doc_root, doc_root, max_depth=3)
    tree = "documentation/\n" + "\n".join(tree_lines)

    pattern = re.compile(
        r"(## 📂 Estructura de Documentación\s*\n\s*\n```)\n[\s\S]*?(```)",
        re.MULTILINE,
    )

    if not pattern.search(content):
        print("  ⚠️  No se encontró la sección de estructura en documentation/README.md")
        return False

    new_content = pattern.sub(rf"\1\n{tree}\n\2", content)

    if new_content == content:
        print("  ✅ Sin cambios en documentation/README.md")
        return False

    if dry_run:
        print("  🔍 [DRY RUN] Cambios detectados en documentation/README.md")
    else:
        filepath.write_text(new_content, encoding="utf-8")
        print("  ✅ Actualizado: documentation/README.md")

    return True


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Regenera las secciones de estructura en los archivos de documentación del proyecto."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Solo muestra qué cambiaría, sin escribir archivos.",
    )
    args = parser.parse_args()

    root = get_project_root()
    print(f"\n📁 Proyecto: {root.name}")
    print(f"📍 Ruta: {root}\n")

    # Detectar carpetas nuevas
    new_folders = detect_new_folders(root)
    if new_folders:
        print("⚠️  Carpetas nuevas detectadas sin descripción:")
        for f in new_folders:
            print(f"   → {f}/")
        print(f"   💡 Agrégalas en FOLDER_DESCRIPTIONS en {Path(__file__).name}\n")

    print("🔄 Actualizando archivos...\n")

    results = {
        ".github/copilot-instructions.md": update_copilot_instructions(root, args.dry_run),
        "README.md": update_readme(root, args.dry_run),
        "documentation/README.md": update_documentation_readme(root, args.dry_run),
    }

    changes = sum(1 for v in results.values() if v)
    print(f"\n{'─' * 40}")
    if args.dry_run:
        print(f"🔍 Dry run completado: {changes} archivo(s) con cambios pendientes")
    elif changes:
        print(f"✅ {changes} archivo(s) actualizado(s)")
    else:
        print("✅ Todo está al día, sin cambios necesarios")
    print()


if __name__ == "__main__":
    main()
