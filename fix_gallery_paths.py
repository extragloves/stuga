import os
import re
import shutil
import urllib.request
import zipfile
import io
import tempfile
from bs4 import BeautifulSoup

def fix_gallery_paths(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    modified = False
    for img in soup.find_all('img'):
        if img.get('src') and img['src'].startswith('wp-content/'):
            img['src'] = '/' + img['src']
            modified = True
    if modified:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Fixed paths in {html_file}")

def fix_all_image_paths():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_file = os.path.join(root, file)
                fix_gallery_paths(html_file)

def copy_gallery_assets():
    # Create necessary directories
    os.makedirs('wp-content/plugins/foogallery/extensions/default-templates/shared/css', exist_ok=True)
    os.makedirs('wp-content/plugins/foogallery/extensions/default-templates/shared/js', exist_ok=True)
    os.makedirs('wp-content/plugins/foobox-image-lightbox/free/css', exist_ok=True)
    os.makedirs('wp-content/plugins/foobox-image-lightbox/free/js', exist_ok=True)

    # List of required files
    required_files = [
        'wp-content/plugins/foogallery/extensions/default-templates/shared/css/foogallery.min.css',
        'wp-content/plugins/foogallery/extensions/default-templates/shared/js/foogallery.min.js',
        'wp-content/plugins/foobox-image-lightbox/free/css/foobox.free.min.css',
        'wp-content/plugins/foobox-image-lightbox/free/js/foobox.free.min.js'
    ]

    # Check if files exist in WordPress installation
    for file in required_files:
        if os.path.exists(file):
            print(f"File {file} already exists, skipping...")
        else:
            print(f"Warning: {file} not found in WordPress installation")

def setup_gallery_assets():
    # Create necessary directories
    os.makedirs('wp-content/plugins/foogallery/extensions/default-templates/shared/css', exist_ok=True)
    os.makedirs('wp-content/plugins/foogallery/extensions/default-templates/shared/js', exist_ok=True)
    os.makedirs('wp-content/plugins/foobox-image-lightbox/free/css', exist_ok=True)
    os.makedirs('wp-content/plugins/foobox-image-lightbox/free/js', exist_ok=True)

    # Download required files
    files_to_download = {
        'wp-content/plugins/foogallery/extensions/default-templates/shared/css/foogallery.min.css': 'https://raw.githubusercontent.com/fooplugins/foogallery/master/extensions/default-templates/shared/css/foogallery.min.css',
        'wp-content/plugins/foogallery/extensions/default-templates/shared/js/foogallery.min.js': 'https://raw.githubusercontent.com/fooplugins/foogallery/master/extensions/default-templates/shared/js/foogallery.min.js',
        'wp-content/plugins/foobox-image-lightbox/free/css/foobox.free.min.css': 'https://raw.githubusercontent.com/fooplugins/foobox/master/free/css/foobox.free.min.css',
        'wp-content/plugins/foobox-image-lightbox/free/js/foobox.free.min.js': 'https://raw.githubusercontent.com/fooplugins/foobox/master/free/js/foobox.free.min.js'
    }

    for file_path, url in files_to_download.items():
        if not os.path.exists(file_path):
            try:
                urllib.request.urlretrieve(url, file_path)
                print(f"Downloaded {file_path}")
            except Exception as e:
                print(f"Error downloading {file_path}: {e}")

def main():
    # Fix paths in all HTML files
    fix_all_image_paths()
    # Setup gallery assets
    setup_gallery_assets()

if __name__ == '__main__':
    main() 