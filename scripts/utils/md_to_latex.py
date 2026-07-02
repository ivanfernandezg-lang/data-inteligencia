#!/usr/bin/env python3
"""Convierte el Markdown extraído de j199030years.pdf a LaTeX compilable."""

import re
import os

INPUT_MD = r"proyectos/RNA/paper-elegido/latex/extracted/j199030years.md"
OUTPUT_TEX = r"proyectos/RNA/paper-elegido/latex/widrow1990_clean.tex"
IMAGES_DIR = "images"

PREAMBLE = r"""\documentclass[11pt,a4paper,twocolumn]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{geometry}
\usepackage{float}
\usepackage{caption}
\usepackage{hyperref}
\usepackage{cite}
\geometry{margin=2.2cm,columnsep=0.7cm}
\hypersetup{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue}

\title{30 Years of Adaptive Neural Networks:\\Perceptron, Madaline, and Backpropagation}
\author{Bernard Widrow, Fellow, IEEE, and Michael A. Lehr\\
Information Systems Laboratory, Department of Electrical Engineering,\\
Stanford University, Stanford, CA 94305-4055, USA}
\date{Proceedings of the IEEE, Vol. 78, No. 9, September 1990}

\begin{document}
\maketitle
\begin{abstract}
Fundamental developments in feedforward artificial neural networks
from the past thirty years are reviewed. The central theme of this
paper is a description of the history, origination, operating
characteristics, and basic theory of several supervised neural
network training algorithms including the Perceptron rule, the LMS
algorithm, three Madaline rules, and the backpropagation technique.
These methods were developed independently, but with the perspective
of history they can all be related to each other. The concept
underlying these algorithms is the ``minimal disturbance principle,''
which suggests that during training it is advisable to inject new
information into a network in a manner that disturbs stored
information to the smallest extent possible.
\end{abstract}
"""

POSTAMBLE = r"""\end{document}
"""


def extract_sections_and_pages(lines):
    """Parse the markdown into pages and identify section boundaries."""
    pages = []
    current_page = {"num": 0, "lines": [], "figures": [], "sections": []}
    
    section_pattern = re.compile(
        r'^\s*(I{1,3}|IV|VI{0,3}|IX|XI{0,2})\s*\.\s{2,}([A-Z][A-Z\s,/-]{5,})'
    )
    subsection_pattern = re.compile(
        r'^\s*([A-Z])\.\s{2,}([A-Z][A-Za-z\s,/-]{5,})'
    )
    
    for line in lines:
        # Detect page breaks
        page_match = re.match(r'^##\s+Página\s+(\d+)', line)
        if page_match:
            if current_page["lines"]:
                pages.append(current_page)
            current_page = {
                "num": int(page_match.group(1)),
                "lines": [],
                "figures": [],
                "sections": [],
            }
            continue
        
        # Skip horizontal rules
        if line.strip() == '---':
            continue
        
        # Detect images
        img_match = re.match(r'!\[Imagen\]\(images\\(.+?)\)', line)
        if img_match:
            current_page["figures"].append(img_match.group(1))
            continue
        
        # Detect sections
        sec_match = section_pattern.match(line)
        if sec_match:
            current_page["sections"].append({
                "type": "section",
                "numeral": sec_match.group(1),
                "title": sec_match.group(2).strip().title(),
            })
        
        # Detect subsections (A., B., C., etc.)
        sub_match = subsection_pattern.match(line)
        if sub_match:
            current_page["sections"].append({
                "type": "subsection",
                "letter": sub_match.group(1),
                "title": sub_match.group(2).strip().title(),
            })
        
        current_page["lines"].append(line)
    
    if current_page["lines"]:
        pages.append(current_page)
    
    return pages


def clean_text(text):
    """Clean up OCR artifacts and prepare for LaTeX."""
    # Fix common OCR issues
    text = text.replace('&', r'\&')
    text = text.replace('%', r'\%')
    text = text.replace('#', r'\#')
    text = text.replace('$', r'\$')
    
    # Fix backslash artifacts from OCR (broken LaTeX commands)
    # "Vol." → "Vol.", "\ol." → "Vol.", etc.
    text = re.sub(r'\\ol\.', 'Vol.', text)
    text = re.sub(r'\\Ol\.', 'Vol.', text)
    
    # Fix other backslash-in-text artifacts  
    text = re.sub(r'\\([a-z]{1,3})\.', r'\1.', text)  # "\etc." → "etc."
    
    # Fix subscript/superscript artifacts from two-column extraction
    text = text.replace('_', r'\_')
    text = text.replace('^', r'\^{}')
    text = text.replace('~', r'\~{}')
    
    # Fix dashes  
    text = text.replace('---', '---')
    text = text.replace('--', '--')
    
    # Fix quotation marks
    text = text.replace('``', '``')
    text = text.replace("''", "''")
    
    # Fix common superscript issues
    text = re.sub(r'(\d+)\s*(st|nd|rd|th)\b', r'\1\textsuperscript{\2}', text)
    
    # Fix references: [I] → [1], [7l → [7] (OCR errors)
    text = re.sub(r'\[([A-Z])\]', lambda m: f'[{ord(m.group(1)) - ord("A") + 1}]', text)
    text = re.sub(r'\[(\d+)l\b', r'[\1]', text)
    
    # Fix broken words from column splitting (hyphenated at line break)
    # Words ending with "- " at end of line in the original two-column layout
    text = re.sub(r'(\w+)-\s+', r'\1', text)
    
    return text


def format_page_for_latex(page, is_first=False):
    """Convert a page's content to LaTeX."""
    output = []
    
    # Skip page 0 (metadata only)
    if page["num"] == 0:
        return ''
    
    output.append(f'\n% ----- Page {page["num"]} -----\n')
    
    # Add sections that start on this page
    for sec in page.get("sections", []):
        if sec["type"] == "section":
            output.append(f'\n\\section{{{sec["title"]}}}\n')
        elif sec["type"] == "subsection":
            output.append(f'\n\\subsection{{{sec["title"]}}}\n')
    
    # --- Filters for boilerplate / running headers ---
    skip_patterns = [
        # Running headers
        r'^WIDROW AND LEHR: PERCEPTRON, MADALINE, AND BACKPROPAGATION',
        r'^PROCEEDINGS OF THE IEEE, VOL\.?\s*78,?\s*NO\.?\s*9,?\s*SEPTEMBER\s*1990',
        # DOI / page numbers on their own
        r'^\d{4}\s*$',  
        r'^0018-9219',
        r'^IEEE Log Number',
        r'^Manuscript received',
        r'^The authors are with',
        r'^\d{4}\s+IEEE\s*$',
    ]
    
    skip_res = [re.compile(p, re.IGNORECASE) for p in skip_patterns]
    
    # Title/author content to skip from body (already in preamble)
    title_skip_patterns = [
        r'^30 Years of Adaptive Neural Networks',
        r'^Perceptron, Madaline, and Backpropagation\s*$',
        r'^BERNARD WIDROW, FELLOW, IEEE,\s*$',
        r'^AND MICHAEL A\. LEHR\s*$',
        r'^Fundamental developments in feedforward.*$',
    ]
    title_skip_res = [re.compile(p, re.IGNORECASE) for p in title_skip_patterns]
    
    # Process text lines
    skip_line = False
    for line_text in page["lines"]:
        stripped = line_text.strip()
        
        # Skip empty lines
        if not stripped:
            output.append('\n')
            continue
        
        # Skip boilerplate
        skip = False
        for pat in skip_res:
            if pat.match(stripped):
                skip = True
                break
        if skip:
            continue
        
        # Skip title/author content from page 1
        if page["num"] <= 2:
            for pat in title_skip_res:
                if pat.match(stripped):
                    skip = True
                    break
        if skip:
            continue
        
        # Skip the "I.  INTRODUCTION" inline text (we already have \section)
        sec_inline = re.match(r'^[IVX]+\.\s{2,}[A-Z][A-Z\s]{5,}$', stripped)
        if sec_inline:
            continue
        
        # Skip "A.  Some Title" inline text (we emit \subsection already)
        sub_inline = re.match(r'^[A-Z]\.\s{2,}[A-Z][A-Za-z\s/-]{5,}$', stripped)
        if sub_inline:
            continue
        
        # Clean the text
        cleaned = clean_text(line_text)
        output.append(cleaned + '\n')
    
    # Add figures for this page
    for fig_file in page.get("figures", []):
        fig_name = fig_file.replace('.png', '')
        output.append('\n\\begin{figure}[H]\n')
        output.append('\\centering\n')
        output.append(f'\\includegraphics[width=0.85\\linewidth]{{{IMAGES_DIR}/{fig_file}}}\n')
        output.append(f'\\caption{{Figure from page {page["num"]}}}\n')
        output.append('\\end{figure}\n')
    
    output.append('\n\\newpage\n')
    return ''.join(output)


def main():
    # Read input
    with open(INPUT_MD, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Parse structure
    pages = extract_sections_and_pages(lines)
    print(f'Parsed {len(pages)} pages with {sum(len(p["figures"]) for p in pages)} figures')
    
    # Build LaTeX output
    latex_content = [PREAMBLE]
    
    # Add table of contents
    latex_content.append('\\tableofcontents\n\\newpage\n')
    
    for i, page in enumerate(pages):
        latex_content.append(format_page_for_latex(page, is_first=(i == 0)))
    
    latex_content.append(POSTAMBLE)
    
    # Write output
    output_dir = os.path.dirname(OUTPUT_TEX)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    full_latex = ''.join(latex_content)
    
    with open(OUTPUT_TEX, 'w', encoding='utf-8') as f:
        f.write(full_latex)
    
    print(f'LaTeX escrito: {OUTPUT_TEX}')
    print(f'Tamaño: {len(full_latex):,} caracteres | {full_latex.count(chr(10)):,} líneas')


if __name__ == '__main__':
    main()
