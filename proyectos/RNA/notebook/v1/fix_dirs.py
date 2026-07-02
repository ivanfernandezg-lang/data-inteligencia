import os, shutil
base = 'C:/Developer/data-inteligencia/proyectos/RNA/notebook/v1'
for d in ['figs', 'tabs']:
    nested = os.path.join(base, d, d)
    if os.path.exists(nested):
        for f in os.listdir(nested):
            src = os.path.join(nested, f)
            dst = os.path.join(base, d, f)
            if os.path.exists(dst):
                os.remove(dst)
            shutil.move(src, dst)
        os.rmdir(nested)
    files = sorted(os.listdir(os.path.join(base, d)))
    print(f'{d}: {len(files)} archivos - {files}')
