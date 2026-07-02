log = open(r'C:\Developer\data-inteligencia\proyectos\RNA\informe\v1\build\informe-widrow.log','r',errors='ignore').read()
errs = [l.strip() for l in log.split('\n') if '!' in l[:5] or 'Error' in l or 'Undefined' in l]
print(f'Errores: {len(errs)}')
for l in errs[:10]: print(l[:150])
warns = [l.strip() for l in log.split('\n') if 'Warning' in l and 'Rerun' not in l and 'Citation' not in l]
print(f'Warnings: {len(warns)}')
for w in warns[:10]: print(w[:150])
pages = [l.strip() for l in log.split('\n') if 'Output written' in l]
print('\n'.join(pages))
