"""
Reconstruye el LaTeX del paper Widrow 1990, reemplazando
los pantallazos completos de página por las figuras individuales recortadas.
"""

import re
import json
import os

INPUT_TEX = r"proyectos/RNA/paper-elegido/latex/widrow1990_clean.tex"
OUTPUT_TEX = r"proyectos/RNA/paper-elegido/latex/widrow1990_final.tex"
FIGURES_JSON = r"proyectos/RNA/paper-elegido/latex/figuras_recortadas/figuras.json"
FIGURES_DIR = "figuras_recortadas"  # relative to .tex location


def load_figure_map():
    """Load figure metadata and deduplicate, keeping best version per fig_num."""
    with open(FIGURES_JSON, 'r', encoding='utf-8') as f:
        figures = json.load(f)
    
    # Deduplicate: for figs appearing multiple times, keep the larger one (more content)
    best = {}
    for fig in figures:
        fn = fig['fig_num']
        w, h = map(int, fig['size_px'].split('x'))
        area = w * h
        if fn not in best or area > best[fn]['area']:
            best[fn] = {**fig, 'area': area}
    
    # Build page -> figures mapping
    page_figs = {}
    for fn, fig in best.items():
        pg = fig['page'] + 1  # 1-indexed
        page_figs.setdefault(pg, []).append(fig)
    
    # Sort figures on each page
    for pg in page_figs:
        page_figs[pg].sort(key=lambda f: f['y0_rel'])
    
    return best, page_figs


def build_figure_latex(fig):
    """Generate LaTeX code for a single figure."""
    caption = fig.get('caption', f'Figure {fig["fig_num"]}')
    # Clean caption for LaTeX
    caption = caption.replace('&', r'\&').replace('%', r'\%').replace('#', r'\#')
    caption = caption.replace('_', r'\_').replace('$', r'\$')
    # Truncate long captions
    if len(caption) > 150:
        caption = caption[:147] + '...'
    
    width = '0.85' if fig['column'] == 'full' else '0.45'
    
    return f"""\\begin{{figure}}[H]
\\centering
\\includegraphics[width={width}\\textwidth]{{{FIGURES_DIR}/{fig['file']}}}
\\caption{{{caption}}}
\\label{{fig:{fig['fig_num']:02d}}}
\\end{{figure}}
"""


def main():
    best_figs, page_figs = load_figure_map()
    
    print(f"Unique figures: {len(best_figs)}")
    for pg in sorted(page_figs):
        figs = [f['fig_num'] for f in page_figs[pg]]
        print(f"  Page {pg:2d}: {figs}")
    
    # Read input LaTeX
    with open(INPUT_TEX, 'r', encoding='utf-8') as f:
        tex = f.read()
    
    # Replace full-page image blocks with individual figures
    # Pattern: \begin{figure}[H]...pageXXX_img01.png...\end{figure}
    def replace_page_figure(match):
        block = match.group(0)
        # Extract page number from image filename
        pg_match = re.search(r'page(\d+)_img', block)
        if not pg_match:
            return block
        page_num = int(pg_match.group(1))
        
        if page_num not in page_figs:
            return ''  # Remove full-page figure if we have no individual ones
        
        # Build replacement with individual figures
        figs_latex = []
        for fig in page_figs[page_num]:
            figs_latex.append(build_figure_latex(fig))
        
        return '\n'.join(figs_latex)
    
    # Find and replace all full-page figure environments
    pattern = r'\\begin\{figure\}\[H\].*?page\d+_img01\.png.*?\\end\{figure\}'
    tex = re.sub(pattern, replace_page_figure, tex, flags=re.DOTALL)
    
    # Also remove any remaining \newpage commands that were for page-image figures
    # (Keep only \newpage between sections, not after empty figure blocks)
    
    # Write output
    with open(OUTPUT_TEX, 'w', encoding='utf-8') as f:
        f.write(tex)
    
    print(f"\nOutput: {OUTPUT_TEX}")
    print(f"Size: {len(tex):,} chars, {tex.count(chr(10)):,} lines")


if __name__ == '__main__':
    main()
