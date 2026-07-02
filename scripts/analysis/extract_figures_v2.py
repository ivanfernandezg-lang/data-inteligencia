"""
V2: Extrae figuras del PDF buscando leyendas "Fig. X." DENTRO de los bloques de texto.
Más robusto que V1 — captura figuras pequeñas e inline.
"""

import fitz
import re
import json
import os
from PIL import Image
import io

PDF_PATH = r"proyectos/RNA/Material/paper-official/j199030years.pdf"
OUTPUT_DIR = r"proyectos/RNA/paper-elegido/latex/figuras_recortadas"
OUTPUT_JSON = r"proyectos/RNA/paper-elegido/latex/figuras_recortadas/figuras.json"


def extract_all_figures(pdf_path, output_dir):
    doc = fitz.open(pdf_path)
    os.makedirs(output_dir, exist_ok=True)
    all_figures = []
    seen = {}  # fig_num -> page (keep first occurrence)
    
    # Manually curated info for figures that are hard to detect
    # Format: (fig_num, page_1indexed, y_top, y_bottom, x_left, x_right)
    # Values in PDF points (approx)
    MANUAL_FIGS = {
        # Fig 1: Adaptive linear combiner — small diagram in left col, page 3
        1:  (3, 145, 255, 90, 295),
        # Fig 2: Adaline — diagram in right col, page 3  
        2:  (3, 410, 600, 315, 530),
        # Fig 7: Elliptical boundary — left col, page 6
        7:  (6, 190, 380, 90, 290),
        # Fig 8: Two-Adaline Madaline — right col, page 6
        8:  (6, 290, 530, 330, 545),
        # Fig 9: Separating lines for Madaline — right col, page 6
        9:  (6, 535, 700, 330, 545),
        # Fig 13: Rosenblatt's α-Perceptron — right col, page 10
        13: (10, 290, 540, 325, 540),
        # Fig 18: Sigmoid Adaline — right col, page 16
        18: (16, 305, 620, 330, 545),
        # Fig 28: Truck backup — left col bottom, page 22-23
        28: (22, 420, 640, 93, 310),
        # Fig 33: Taxonomy (full-width) — page 25
        33: (25, 166, 690, 73, 545),
    }
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        page_w = page.rect.width
        page_h = page.rect.height
        
        # Determine column boundary (approximate middle)
        col_boundary = page_w * 0.48
        
        # Get all text blocks
        blocks = page.get_text('blocks')
        
        # Search for "Fig. X" captions WITHIN text blocks
        for b in blocks:
            text = b[4]
            bx0, by0, bx1, by1 = b[:4]
            
            # Find all "Fig. X" or "Fig. X." patterns
            for m in re.finditer(r'Fig\.\s+(\d+)\.?\s{2,}([A-Z][^.]{10,}\.)', text):
                fig_num = int(m.group(1))
                caption = m.group(0)
                
                if fig_num in seen and seen[fig_num] != page_num:
                    continue  # already found on another page
                
                # The figure is ABOVE this text block
                fig_bottom = by0 - 3
                
                # Find the figure top: look at text blocks above
                blocks_above = [bl for bl in blocks 
                               if bl[3] < by0 - 5 and bl[4].strip()]
                
                if blocks_above:
                    fig_top = max(bl[3] for bl in blocks_above) + 3
                else:
                    fig_top = 65  # near page top
                
                # Determine column
                mid_x = (bx0 + bx1) / 2
                if mid_x < col_boundary:
                    col = 'left'
                    fig_left = 65
                    fig_right = col_boundary - 8
                elif bx1 - bx0 > page_w * 0.6:
                    col = 'full'
                    fig_left = 65
                    fig_right = page_w - 65
                else:
                    col = 'right'
                    fig_left = col_boundary + 8
                    fig_right = page_w - 65
                
                fig_height = fig_bottom - fig_top
                
                # Skip if too small or too large
                if fig_height < 15:
                    # Try expanding upward
                    fig_top = max(50, fig_top - 30)
                    fig_height = fig_bottom - fig_top
                if fig_height < 15 or fig_height > page_h * 0.85:
                    continue
                
                # Render page and crop
                pix = page.get_pixmap(dpi=200)
                img_data = pix.tobytes("png")
                page_img = Image.open(io.BytesIO(img_data))
                
                scale_x = pix.width / page_w
                scale_y = pix.height / page_h
                
                crop_box = (
                    int(fig_left * scale_x),
                    int(fig_top * scale_y),
                    int(fig_right * scale_x),
                    int(fig_bottom * scale_y),
                )
                
                cropped = page_img.crop(crop_box)
                
                fname = f"fig_{fig_num:02d}.png"
                fpath = os.path.join(output_dir, fname)
                cropped.save(fpath, "PNG")
                
                all_figures.append({
                    'fig_num': fig_num,
                    'page': page_num,
                    'file': fname,
                    'caption': caption[:200],
                    'x0_rel': fig_left,
                    'y0_rel': fig_top,
                    'x1_rel': fig_right,
                    'y1_rel': fig_bottom,
                    'column': col,
                    'size_px': f"{cropped.width}x{cropped.height}",
                })
                seen[fig_num] = page_num
                print(f"  ✅ Fig. {fig_num:2d} | Pg {page_num+1:2d} | {col:5s} | {cropped.width}x{cropped.height} px | {caption[:60].strip()}")
        
        # Check for manual figures on this page
        for fig_num, (pg, yt, yb, xl, xr) in MANUAL_FIGS.items():
            if pg == page_num + 1 and fig_num not in seen:
                pix = page.get_pixmap(dpi=200)
                img_data = pix.tobytes("png")
                page_img = Image.open(io.BytesIO(img_data))
                
                scale_x = pix.width / page_w
                scale_y = pix.height / page_h
                
                crop_box = (
                    int(xl * scale_x),
                    int(yt * scale_y),
                    int(xr * scale_x),
                    int(yb * scale_y),
                )
                
                cropped = page_img.crop(crop_box)
                
                fname = f"fig_{fig_num:02d}.png"
                fpath = os.path.join(output_dir, fname)
                cropped.save(fpath, "PNG")
                
                col = 'full' if (xr - xl) > page_w * 0.6 else ('right' if xl > col_boundary else 'left')
                
                all_figures.append({
                    'fig_num': fig_num,
                    'page': page_num,
                    'file': fname,
                    'caption': f'[Manual] Figure {fig_num}',
                    'x0_rel': xl,
                    'y0_rel': yt,
                    'x1_rel': xr,
                    'y1_rel': yb,
                    'column': col,
                    'size_px': f"{cropped.width}x{cropped.height}",
                    'manual': True,
                })
                seen[fig_num] = page_num
                print(f"  🔧 Fig. {fig_num:2d} | Pg {page_num+1:2d} | {col:5s} | {cropped.width}x{cropped.height} px | MANUAL")
    
    doc.close()
    return all_figures


def main():
    print("🔍 V2: Extrayendo TODAS las figuras (búsqueda dentro de bloques)...\n")
    
    # Clear previous extractions
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith('.png'):
            os.remove(os.path.join(OUTPUT_DIR, f))
    
    figures = extract_all_figures(PDF_PATH, OUTPUT_DIR)
    
    # Sort by figure number
    figures.sort(key=lambda x: x['fig_num'])
    
    # Deduplicate by fig_num (keep best — prefer non-manual)
    deduped = {}
    for f in figures:
        fn = f['fig_num']
        if fn not in deduped or (not f.get('manual') and deduped[fn].get('manual')):
            deduped[fn] = f
    figures = list(deduped.values())
    figures.sort(key=lambda x: x['fig_num'])
    
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(figures, f, ensure_ascii=False, indent=2)
    
    print(f"\n📊 Total: {len(figures)} figuras únicas extraídas")
    missing = set(range(1, 34)) - {f['fig_num'] for f in figures}
    if missing:
        print(f"⚠️  Faltantes: {sorted(missing)}")
    else:
        print("🎉 ¡Las 33 figuras extraídas!")


if __name__ == '__main__':
    main()
