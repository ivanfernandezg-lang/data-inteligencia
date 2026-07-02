"""Merge: V1 auto-detected figures + manual coordinates for missing ones."""
import fitz, json, os
from PIL import Image
import io

PDF = r"proyectos/RNA/Material/paper-official/j199030years.pdf"
OUT = r"proyectos/RNA/paper-elegido/latex/figuras_recortadas"
JSON_PATH = os.path.join(OUT, "figuras.json")

# Load existing figures (run extract_figures.py first!)
with open(JSON_PATH) as f:
    existing = json.load(f)
existing_nums = {e["fig_num"] for e in existing}
print(f"Existing auto-detected: {sorted(existing_nums)} ({len(existing)})")

# Manual coordinates for hard-to-detect figures
# (fig_num, page_1idx, y0, y1, x0, x1) in PDF points
MANUAL = {
    1:  (3, 145, 255, 90, 285),
    2:  (3, 410, 600, 315, 528),
    7:  (6, 190, 370, 90, 285),
    8:  (6, 290, 530, 328, 542),
    9:  (6, 535, 690, 328, 542),
    13: (10, 290, 530, 325, 540),
    18: (16, 310, 610, 328, 542),
    28: (22, 425, 620, 93, 310),
    33: (25, 170, 680, 73, 545),
}

doc = fitz.open(PDF)
added = 0

for fig_num, (pg, yt, yb, xl, xr) in MANUAL.items():
    if fig_num in existing_nums:
        continue
    
    page = doc[pg - 1]
    pw, ph = page.rect.width, page.rect.height
    
    pix = page.get_pixmap(dpi=200)
    img_data = pix.tobytes("png")
    page_img = Image.open(io.BytesIO(img_data))
    
    sx, sy = pix.width / pw, pix.height / ph
    
    crop_box = (int(xl*sx), int(yt*sy), int(xr*sx), int(yb*sy))
    cropped = page_img.crop(crop_box)
    
    fname = f"fig_{fig_num:02d}.png"
    cropped.save(os.path.join(OUT, fname), "PNG")
    
    col = "full" if (xr - xl) > pw * 0.6 else ("right" if xl > pw * 0.48 else "left")
    
    existing.append({
        "fig_num": fig_num, "page": pg - 1, "file": fname,
        "caption": f"[Manual] Figure {fig_num}",
        "x0_rel": xl, "y0_rel": yt, "x1_rel": xr, "y1_rel": yb,
        "column": col, "size_px": f"{cropped.width}x{cropped.height}",
        "manual": True,
    })
    existing_nums.add(fig_num)
    added += 1
    print(f"  + Fig. {fig_num:2d} | Pg {pg} | {col:5s} | {cropped.width}x{cropped.height} px")

existing.sort(key=lambda x: x["fig_num"])

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(existing, f, ensure_ascii=False, indent=2)

doc.close()
print(f"\nAdded manually: {added}")
print(f"Total: {len(existing)} figures")
missing = set(range(1, 34)) - {e["fig_num"] for e in existing}
if missing:
    print(f"Still missing: {sorted(missing)}")
else:
    print("ALL 33 figures extracted!")
