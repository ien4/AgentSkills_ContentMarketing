import os
import re

skill_dir = r'd:\bbo_team\Ct_Mr\agentic-ai-content-marketing-skill'
patterns = [
    r'â€', r'â€œ', r'â€™', r'â€˜', r'â€“', r'â€”', r'â€¦', r'ï»¿',
    r'Â', r'Ã', r'Ä', r'áº', r'á»', r'khÃ', r'cáº', r'tháº', r'pháº', r'sá»', r'tÃ'
]

# We need to correctly encode the patterns. 
# It's better to just read them as string literals in Python.
compiled_patterns = [re.compile(p) for p in patterns]

found_files = {}
total_files = 0

for root, _, files in os.walk(skill_dir):
    for file in files:
        if file.endswith('.md'):
            total_files += 1
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                matches = set()
                for p in compiled_patterns:
                    if p.search(content):
                        matches.add(p.pattern)
                
                if matches:
                    found_files[filepath] = matches
            except Exception as e:
                print(f"Error reading {filepath}: {e}")

print(f'Total markdown files scanned: {total_files}')
print(f'Files with mojibake: {len(found_files)}')
for filepath, matches in found_files.items():
    relpath = os.path.relpath(filepath, skill_dir)
    print(f'- {relpath}: {matches}')
