"""Analiza páginas específicas que tienen figuras no detectadas."""
import fitz, re, json

doc = fitz.open(r"proyectos/RNA/Material/paper-official/j199030years.pdf")

# Load existing figures to know what we already have
with open(r"proyectos/RNA/paper-elegido/latex/figuras_recortadas/figuras.json") as f:
    existing = json.load(f)
existing_nums = {e['fig_num'] for e in existing}
print(f"Already extracted: {sorted(existing_nums)}")

# Check pages with missing figures
missing_pages = [3, 6, 10, 11, 16, 22, 23, 25]  # 1-indexed

for pn in missing_pages:
    page = doc[pn-1]
    blocks = page.get_text('blocks')
    page_w = page.rect.width
    
    print(f"\n=== Page {pn} (w={page_w:.0f}) ===")
    
    # Show all blocks with figure references
    for b in blocks:
        text = b[4]
        if 'Fig.' in text:
            figs = re.findall(r'Fig\.\s+(\d+)', text)
            # Check if it's a caption (text after Fig. X)
            cap_match = re.search(r'(Fig\.\s+\d+\.?\s{2,}.{10,})', text)
            label = "CAPTION" if cap_match else "mention"
            print(f"  [{label}] y={b[1]:.0f}-{b[3]:.0f} x={b[0]:.0f}-{b[2]:.0f} figs={figs}")
            if cap_match:
                # Show blocks above this one
                blocks_above = sorted(
                    [bl for bl in blocks if bl[3] < b[1] and bl[4].strip()],
                    key=lambda x: x[3], reverse=True
                )[:3]
                for ba in blocks_above:
                    print(f"         ABOVE: y={ba[1]:.0f}-{ba[3]:.0f} x={ba[0]:.0f}-{ba[2]:.0f} | {ba[4][:60].strip()}")

doc.close()
