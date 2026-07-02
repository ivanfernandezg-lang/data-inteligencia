"""
Extrae figuras individuales de un PDF escaneado (Acrobat Capture).
Usa los bloques de texto OCR para identificar huecos donde están las figuras,
y las leyendas "Fig. X" como anclas para ubicar cada figura.

Output: imagenes_recortadas/fig_XX.png + JSON con metadatos de posición.
"""

import fitz
import re
import json
import os
from pathlib import Path
from PIL import Image
import io

PDF_PATH = r"proyectos/RNA/Material/paper-official/j199030years.pdf"
OUTPUT_DIR = r"proyectos/RNA/paper-elegido/latex/figuras_recortadas"
OUTPUT_JSON = r"proyectos/RNA/paper-elegido/latex/figuras_recortadas/figuras.json"


def extract_figures_from_pdf(pdf_path, output_dir):
    """Extrae figuras individuales del PDF usando las posiciones de bloques de texto OCR."""
    
    doc = fitz.open(pdf_path)
    os.makedirs(output_dir, exist_ok=True)
    
    all_figures = []
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        page_w = page.rect.width
        page_h = page.rect.height
        
        # Get text blocks with positions
        blocks = page.get_text('blocks')
        
        # Separate text blocks from image blocks
        text_blocks = []
        for b in blocks:
            x0, y0, x1, y1 = b[:4]
            text = b[4] if len(b) > 4 else ""
            block_type = b[6] if len(b) > 6 else 0
            text_blocks.append({
                'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1,
                'text': text.strip(),
                'type': block_type,
            })
        
        # Find "Fig. X" captions
        fig_captions = []
        for tb in text_blocks:
            match = re.search(r'Fig\.\s+(\d+)\.?\s', tb['text'])
            if match:
                fig_num = int(match.group(1))
                # Get full caption (may span multiple blocks)
                caption_start = match.start()
                caption_text = tb['text'][caption_start:]
                fig_captions.append({
                    'fig_num': fig_num,
                    'caption': caption_text[:150],
                    'y0': tb['y0'],
                    'y1': tb['y1'],
                    'x0': tb['x0'],
                    'x1': tb['x1'],
                })
        
        if not fig_captions:
            continue
        
        # Detect column boundaries for two-column layout
        # Find the column separator (middle of page)
        all_x0 = [tb['x0'] for tb in text_blocks if tb['text']]
        if all_x0:
            # Cluster x0 positions to find column boundaries
            col_boundary = page_w * 0.48  # approximate middle
            
        # Determine which figures have already been found on this page
        found_figs = set()
        
        # For each figure caption, find the figure region above it
        for cap in sorted(fig_captions, key=lambda c: c['fig_num']):
            fig_num = cap['fig_num']
            if fig_num in found_figs:
                continue
            
            cap_y0 = cap['y0']
            cap_x0 = cap['x0']
            cap_x1 = cap['x1']
            
            # Determine if this is left column, right column, or full-width
            if cap_x0 < col_boundary and cap_x1 < col_boundary:
                col = 'left'
                col_width = col_boundary - 60
            elif cap_x0 > col_boundary:
                col = 'right'
                col_width = page_w - col_boundary - 60
            else:
                col = 'full'
                col_width = page_w - 120
            
            # Find the figure region ABOVE the caption
            # Search upward for the nearest text block edge
            fig_top = cap_y0 - 20  # start just above caption
            
            # Look for text blocks above this caption in the same column
            blocks_above = [
                tb for tb in text_blocks
                if tb['y1'] < cap_y0 - 5
                and tb['text']
                and abs(tb['x0'] - cap_x0) < col_width * 0.7
            ]
            
            if blocks_above:
                # Figure starts below the lowest text block above
                fig_top = max(tb['y1'] for tb in blocks_above) + 3
            else:
                # No text above in this column — figure starts near page top
                fig_top = 60
            
            # Find the bottom of the figure region (just above the caption)
            fig_bottom = cap_y0 - 5
            
            # Horizontal boundaries
            if col == 'left':
                fig_left = 60
                fig_right = col_boundary - 10
            elif col == 'right':
                fig_left = col_boundary + 10
                fig_right = page_w - 60
            else:
                fig_left = 60
                fig_right = page_w - 60
            
            # Check if this figure region overlaps with another already found
            # (e.g., Fig. 2 and Fig. 3 are the same figure with sub-labels)
            overlap = False
            for prev in all_figures:
                if prev['page'] == page_num:
                    if (abs(fig_top - prev['y0_rel']) < 30 and 
                        abs(fig_left - prev['x0_rel']) < 100):
                        overlap = True
                        break
            
            if overlap:
                continue
            
            # Validate the region
            fig_height = fig_bottom - fig_top
            if fig_height < 30:  # too small
                continue
            if fig_height > page_h * 0.8:  # too large (probably full page)
                continue
            
            # Render the full page to an image
            pix = page.get_pixmap(dpi=200)
            img_data = pix.tobytes("png")
            page_img = Image.open(io.BytesIO(img_data))
            
            # Convert PDF coordinates to image coordinates
            scale_x = pix.width / page_w
            scale_y = pix.height / page_h
            
            crop_box = (
                int(fig_left * scale_x),
                int(fig_top * scale_y),
                int(fig_right * scale_x),
                int(fig_bottom * scale_y),
            )
            
            cropped = page_img.crop(crop_box)
            
            # Save
            safe_caption = re.sub(r'[^\w\s-]', '', cap['caption'][:60]).strip()
            fname = f"fig_{fig_num:02d}.png"
            fpath = os.path.join(output_dir, fname)
            cropped.save(fpath, "PNG")
            
            figure_info = {
                'fig_num': fig_num,
                'page': page_num,
                'file': fname,
                'caption': cap['caption'],
                'x0_rel': fig_left,
                'y0_rel': fig_top,
                'x1_rel': fig_right,
                'y1_rel': fig_bottom,
                'column': col,
                'size_px': f"{cropped.width}x{cropped.height}",
            }
            all_figures.append(figure_info)
            found_figs.add(fig_num)
            print(f"  ✅ Fig. {fig_num:2d} | Page {page_num+1:2d} | {col:5s} | {cropped.width}x{cropped.height} px | {safe_caption[:50]}")
    
    doc.close()
    return all_figures


def main():
    print("🔍 Extrayendo figuras del PDF...\n")
    figures = extract_figures_from_pdf(PDF_PATH, OUTPUT_DIR)
    
    # Save metadata
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(figures, f, ensure_ascii=False, indent=2)
    
    print(f"\n📊 Total: {len(figures)} figuras extraídas")
    print(f"📁 Output: {OUTPUT_DIR}/")
    print(f"📋 Metadata: {OUTPUT_JSON}")
    
    # Summary by page
    pages_with_figs = {}
    for f in figures:
        p = f['page'] + 1
        pages_with_figs.setdefault(p, []).append(f['fig_num'])
    
    print("\n📄 Distribución por página:")
    for p in sorted(pages_with_figs):
        print(f"  Page {p:2d}: {pages_with_figs[p]}")


if __name__ == '__main__':
    main()
