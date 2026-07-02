import os, re

tabs_dir = r'C:\Developer\data-inteligencia\proyectos\RNA\notebook\v1\tabs'

for fname in os.listdir(tabs_dir):
    fpath = os.path.join(tabs_dir, fname)
    with open(fpath, 'r') as f:
        content = f.read()
    
    # Step 1: Replace literal \n (2 chars: backslash + n) with actual newlines
    content = content.replace('\\n', '\n')
    
    # Step 2: Fix double-backslash commands.
    # In LaTeX: \begin, \toprule, etc. need ONE backslash.
    # But \\ at end of lines is the line break (TWO backslashes).
    # Strategy: replace \\ at start of line or after newline (commands) with \
    # but preserve \\ at end of lines
    
    lines = content.split('\n')
    fixed_lines = []
    for line in lines:
        # Replace \\X with \X for LaTeX commands at start of line or after spaces
        # Commands: begin, end, toprule, midrule, bottomrule, alpha, mu, pm, times, |, ( 
        line = re.sub(r'\\\\(begin|end|toprule|midrule|bottomrule|alpha|mu|pm|times|cdots|text|hline)', r'\\\1', line)
        # Fix \% (should be \%)
        line = line.replace('\\\\%', '\\%')
        fixed_lines.append(line)
    
    fixed = '\n'.join(fixed_lines)
    
    with open(fpath, 'w') as f:
        f.write(fixed)
    print(f'Fixed: {fname}')
