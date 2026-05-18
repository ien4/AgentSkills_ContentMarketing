import os

skill_dir = r'd:\bbo_team\Ct_Mr\agentic-ai-content-marketing-skill'

mappings = {
    'â€œ': '“',
    'â€': '”',
    'â€™': '’',
    'â€˜': '‘',
    'â€“': '–',
    'â€”': '—',
    'â€¦': '…',
    'ï»¿': '',
    'khÃ´ng': 'không',
    'cáº§n': 'cần',
    'pháº§n': 'phần',
    'tháº¥y': 'thấy',
    'sá»\xad': 'sử',
    'Ä‘': 'đ',
    'Äƒ': 'ă',
    'â€ ': '” ',  # usually 'â€ ' might be followed by a quote
    'â€\n': '”\n', 
    'â€\r': '”\r',
    'â€': '”', # fallback, will catch 'â€.'
}

# The files we found previously
files_to_fix = [
    r"10-system\control\PACKAGING_CHECKLIST.md",
    r"10-system\guides\FIRST_WORKFLOW_TEST_PLAN.md",
    r"10-system\guides\OPERATOR_PLAYBOOK.md",
    r"10-system\guides\USAGE_GUIDE.md",
    r"10-system\handoff\FINAL_PACKAGING_SNAPSHOT.md",
    r"10-system\handoff\HANDOFF_SUMMARY.md",
    r"10-system\safety\DATA_INGESTION_SAFETY.md",
    r"INGESTION_LOG.md",
    r"README.md",
    r"SKILL.md",
    r"10-system\safety\INGESTION_SOP.md"
]

fixed_files = []
fixed_patterns = set()

# Or we can just loop over all md files to be safe
for root, _, files in os.walk(skill_dir):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            file_fixed_patterns = set()
            
            # Apply mappings in order
            for bad, good in mappings.items():
                if bad in new_content:
                    new_content = new_content.replace(bad, good)
                    file_fixed_patterns.add(bad)
                    fixed_patterns.add(bad)
                    
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                relpath = os.path.relpath(filepath, skill_dir)
                fixed_files.append((relpath, file_fixed_patterns))
                print(f"Fixed {relpath}: {file_fixed_patterns}")

print(f"\nTotal files fixed: {len(fixed_files)}")
print(f"Fixed patterns: {fixed_patterns}")
