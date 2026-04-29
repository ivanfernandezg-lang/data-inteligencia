"""
split_chapters.py
=================

Corta el PDF `InteligenciaComputacional-Livro Official.pdf` en archivos
independientes para los capítulos 1, 2, 3, 5 y 6, y extrae el texto plano
de cada uno.

Mapeo de páginas (verificado contra el sumário del libro):

    Cap 1  INTRODUÇÃO ............... PDF p.  10 –  30
    Cap 2  PRÉ-PROCESSAMENTO ........ PDF p.  31 –  78
    Cap 3  REGRESSÃO LINEAR ......... PDF p.  79 – 116
    Cap 5  CLASSIFICAÇÃO ............ PDF p. 149 – 189
    Cap 6  ANÁLISE DE AGRUPAMENTOS . PDF p. 190 – 236

El libro contiene texto seleccionable (PDF digital, no escaneado), por lo
que no es necesario aplicar OCR: se usa la extracción nativa de PyMuPDF.

Salida (relativa a la carpeta del libro):

    capitulos_pdf/cap{N}_{slug}.pdf      ← PDF recortado
    capitulos_txt/cap{N}_{slug}.txt      ← texto plano extraído
    capitulos_txt/cap{N}_{slug}.meta.json ← rangos + tamaños
"""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
PDF_SRC = ROOT / "InteligenciaComputacional-Livro Official.pdf"
DIR_PDF = ROOT / "capitulos_pdf"
DIR_TXT = ROOT / "capitulos_txt"


@dataclass
class Capitulo:
    numero: int
    titulo: str
    slug: str
    pdf_inicio: int  # 1-indexed inclusive
    pdf_fin: int     # 1-indexed inclusive


CAPITULOS: list[Capitulo] = [
    Capitulo(1, "Introdução",                "introducao",          10,  30),
    Capitulo(2, "Pré-processamento",         "pre-processamento",   31,  78),
    Capitulo(3, "Regressão Linear",          "regressao-linear",    79, 116),
    Capitulo(5, "Classificação",             "classificacao",      149, 189),
    Capitulo(6, "Análise de Agrupamentos",   "analise-agrupamentos", 190, 236),
]


def limpiar_texto(txt: str) -> str:
    """Quita el header repetitivo 'INTELIGÊNCIA COMPUTACIONAL <num>'."""
    lineas = txt.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lineas):
        l = lineas[i].strip()
        # Header de página: 'INTELIGÊNCIA COMPUTACIONAL' + número solo
        if l == "INTELIGÊNCIA COMPUTACIONAL" and i + 1 < len(lineas):
            siguiente = lineas[i + 1].strip()
            if re.fullmatch(r"\d{1,3}", siguiente):
                i += 2
                continue
        out.append(lineas[i])
        i += 1
    # Compactar líneas vacías múltiples
    texto = "\n".join(out)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


def cortar_y_extraer() -> None:
    DIR_PDF.mkdir(exist_ok=True)
    DIR_TXT.mkdir(exist_ok=True)

    src = pymupdf.open(PDF_SRC)
    print(f"Origen: {PDF_SRC.name}  ({src.page_count} pgs)\n")

    for cap in CAPITULOS:
        nombre = f"cap{cap.numero}_{cap.slug}"
        out_pdf = DIR_PDF / f"{nombre}.pdf"
        out_txt = DIR_TXT / f"{nombre}.txt"
        out_meta = DIR_TXT / f"{nombre}.meta.json"

        # 1. Cortar PDF
        nuevo = pymupdf.open()
        nuevo.insert_pdf(src, from_page=cap.pdf_inicio - 1, to_page=cap.pdf_fin - 1)
        nuevo.save(out_pdf, deflate=True, garbage=4)
        nuevo.close()

        # 2. Extraer texto
        partes = []
        for i in range(cap.pdf_inicio - 1, cap.pdf_fin):
            partes.append(src[i].get_text())
        texto = limpiar_texto("\n".join(partes))
        out_txt.write_text(texto, encoding="utf-8")

        # 3. Metadatos
        meta = asdict(cap) | {
            "n_paginas": cap.pdf_fin - cap.pdf_inicio + 1,
            "n_caracteres_texto": len(texto),
            "n_palabras_aprox": len(texto.split()),
            "pdf_salida": out_pdf.name,
            "txt_salida": out_txt.name,
        }
        out_meta.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

        print(
            f"Cap {cap.numero}: {cap.titulo:30s} "
            f"págs {cap.pdf_inicio:3d}-{cap.pdf_fin:3d} "
            f"({meta['n_paginas']:2d} pgs, {meta['n_palabras_aprox']:,} palabras)"
        )
        print(f"   → {out_pdf.relative_to(ROOT)}")
        print(f"   → {out_txt.relative_to(ROOT)}\n")

    src.close()
    print("Listo.")


if __name__ == "__main__":
    cortar_y_extraer()
