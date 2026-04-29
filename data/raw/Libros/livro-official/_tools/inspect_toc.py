"""Inspecciona páginas del TOC y encuentra inicios de capítulos."""
import re
import sys
from pathlib import Path
import pymupdf

PDF = Path(__file__).resolve().parent.parent / "InteligenciaComputacional-Livro Official.pdf"


def dump_toc():
    d = pymupdf.open(PDF)
    print(f"Total páginas: {d.page_count}\n")
    for i in range(3, 8):  # PDF pp 4-8 son el sumario
        print(f"=== PDF PAGE {i+1} ===")
        print(d[i].get_text())
    d.close()


def find_chapter_starts():
    """Busca páginas donde aparece el patrón de inicio de capítulo: 'N    TÍTULO'."""
    d = pymupdf.open(PDF)
    # Patrón: número solo seguido de título en mayúsculas (header de capítulo)
    chapter_pat = re.compile(r"^\s*(\d{1,2})\s+([A-ZÁÉÍÓÚÂÊÔÃÕÇ][A-ZÁÉÍÓÚÂÊÔÃÕÇ\s]{4,})\s*$", re.MULTILINE)
    for i in range(8, d.page_count):
        txt = d[i].get_text()
        # Tomamos solo las primeras 5 líneas no vacías
        lines = [l.strip() for l in txt.splitlines() if l.strip()]
        head = "\n".join(lines[:5])
        m = chapter_pat.search(head)
        if m:
            print(f"PDF p.{i+1:>3} → Cap {m.group(1)}: {m.group(2)[:60]}")
    d.close()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "starts":
        find_chapter_starts()
    else:
        dump_toc()
