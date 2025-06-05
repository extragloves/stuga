import os
import re

# Directory to start from (current directory)
START_DIR = os.path.dirname(os.path.abspath(__file__))

# Patterns to replace
PATTERNS = [
    (re.compile(r'(src|href|data-src-fg)="/wp-content/'), r'\1="wp-content/'),
]

def fix_paths_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content
    for pattern, replacement in PATTERNS:
        new_content = pattern.sub(replacement, new_content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {filepath}")

def main():
    for root, dirs, files in os.walk(START_DIR):
        for file in files:
            if file.endswith('.html'):
                fix_paths_in_file(os.path.join(root, file))

if __name__ == "__main__":
    main() 