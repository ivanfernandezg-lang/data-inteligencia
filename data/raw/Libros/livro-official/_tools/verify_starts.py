"""Verifica páginas de inicio de cada capítulo en el PDF."""
from pathlib import Path
import pymupdf

PDF = Path(__file__).resolve().parent.parent / "InteligenciaComputacional-Livro Official.pdf"

d = pymupdf.open(PDF)
for p in [10, 31, 79, 117, 149, 190, 237, 281, 347]:
    txt = d[p - 1].get_text()
    head = "\n".join([l for l in txt.splitlines() if l.strip()][:5])
    print(f"--- PDF p.{p} ---")
    print(head)
    print()
d.close()
