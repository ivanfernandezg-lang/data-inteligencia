import os, re

tabs_dir = r'C:\Developer\data-inteligencia\proyectos\RNA\notebook\v1\tabs'

for fname in os.listdir(tabs_dir):
    fpath = os.path.join(tabs_dir, fname)
    with open(fpath, 'r') as f:
        content = f.read()
    
    # Fix double-escaping from notebook generation
    # The notebook wrote things like \\begin which should be \begin
    fixed = content.replace('\\\\', '\\')
    # Fix literal \n to actual newlines
    fixed = fixed.replace('\\n', '\n')
    
    with open(fpath, 'w') as f:
        f.write(fixed)
    print(f'Fixed: {fname}')
    print(f'  First 100 chars: {fixed[:100]}')
