import os
import re
from pathlib import Path

def fix_image_paths(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get the relative path from the HTML file to the root
    relative_path = os.path.relpath('.', os.path.dirname(html_file))
    if relative_path == '.':
        relative_path = ''
    else:
        relative_path = relative_path.replace('\\', '/') + '/'
    
    # Replace absolute paths with relative paths
    modified_content = re.sub(
        r'src="/wp-content/uploads/',
        f'src="{relative_path}wp-content/uploads/',
        content
    )
    
    # Also fix srcset attributes
    modified_content = re.sub(
        r'srcset="/wp-content/uploads/',
        f'srcset="{relative_path}wp-content/uploads/',
        modified_content
    )
    
    # Write the modified content back to the file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)

def main():
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    # Process each HTML file
    for html_file in html_files:
        print(f"Processing {html_file}...")
        fix_image_paths(html_file)

if __name__ == '__main__':
    main() 