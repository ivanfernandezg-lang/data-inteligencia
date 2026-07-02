"""Analiza el PDF original para ver si tiene imágenes individuales embebidas."""
import fitz
import json

PDF_PATH = r"proyectos/RNA/Material/paper-official/j199030years.pdf"

doc = fitz.open(PDF_PATH)
print(f"Total pages: {doc.page_count}")

# Check first few pages for embedded images
for page_num in range(min(5, doc.page_count)):
    page = doc[page_num]
    images = page.get_images(full=True)
    
    print(f"\n--- Page {page_num + 1} ---")
    print(f"  Embedded images: {len(images)}")
    for i, img in enumerate(images[:3]):
        xref = img[0]
        base_image = doc.extract_image(xref)
        print(f"  Image {i}: xref={xref}, size={base_image['width']}x{base_image['height']}, ext={base_image['ext']}")
    
    # Get text blocks with positions
    blocks = page.get_text('blocks')
    print(f"  Text blocks: {len(blocks)}")
    for b in blocks[:3]:
        bbox = b[:4]
        text = b[4][:100].replace('\n', ' ') if b[4].strip() else "(empty)"
        block_type = "image" if b[6] == 0 else "text"
        print(f"    [{block_type}] bbox=({bbox[0]:.0f},{bbox[1]:.0f},{bbox[2]:.0f},{bbox[3]:.0f}) text='{text}'")

# Check which pages have "Fig. " text
print("\n\n--- Figure locations (by text search) ---")
for page_num in range(doc.page_count):
    page = doc[page_num]
    text = page.get_text()
    if 'Fig. ' in text:
        # Find all figure mentions
        import re
        figs = re.findall(r'Fig\.\s+\d+', text)
        if figs:
            print(f"Page {page_num + 1}: {', '.join(set(figs))}")

doc.close()
