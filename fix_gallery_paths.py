import os
import re
from bs4 import BeautifulSoup
import shutil
import urllib.request
import zipfile
import io
import tempfile

def fix_gallery_paths(html_file):
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse HTML
    soup = BeautifulSoup(content, 'html.parser')
    
    # Fix image paths in gallery items
    gallery_items = soup.select('.fg-item a')
    for item in gallery_items:
        if 'href' in item.attrs:
            href = item['href']
            if href.startswith('wp-content/'):
                item['href'] = '../' + href
    
    # Fix image src paths
    images = soup.select('img')
    for img in images:
        if 'data-src-fg' in img.attrs:
            src = img['data-src-fg']
            if src.startswith('wp-content/'):
                img['data-src-fg'] = '../' + src
    
    # Fix CSS and JS paths
    css_links = soup.select('link[href*="wp-content"]')
    for link in css_links:
        href = link['href']
        if href.startswith('wp-content/'):
            link['href'] = '../' + href
    
    js_scripts = soup.select('script[src*="wp-content"]')
    for script in js_scripts:
        src = script['src']
        if src.startswith('wp-content/'):
            script['src'] = '../' + src
    
    # Write the modified HTML back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

def download_file(url, dest_path):
    try:
        with urllib.request.urlopen(url) as response:
            with open(dest_path, 'wb') as f:
                f.write(response.read())
        print(f"Downloaded {url} to {dest_path}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False

def setup_gallery_assets():
    # Create necessary directories
    os.makedirs('wp-content/plugins/foogallery/extensions/default-templates/shared/css', exist_ok=True)
    os.makedirs('wp-content/plugins/foogallery/extensions/default-templates/shared/js', exist_ok=True)
    os.makedirs('wp-content/plugins/foobox-image-lightbox/free/css', exist_ok=True)
    os.makedirs('wp-content/plugins/foobox-image-lightbox/free/js', exist_ok=True)
    
    # Download FooGallery files
    foogallery_files = {
        'wp-content/plugins/foogallery/extensions/default-templates/shared/css/foogallery.min.css': 'https://raw.githubusercontent.com/fooplugins/foogallery/master/extensions/default-templates/shared/css/foogallery.min.css',
        'wp-content/plugins/foogallery/extensions/default-templates/shared/js/foogallery.min.js': 'https://raw.githubusercontent.com/fooplugins/foogallery/master/extensions/default-templates/shared/js/foogallery.min.js'
    }
    
    # Download FooBox files
    foobox_files = {
        'wp-content/plugins/foobox-image-lightbox/free/css/foobox.free.min.css': 'https://raw.githubusercontent.com/fooplugins/foobox/master/free/css/foobox.free.min.css',
        'wp-content/plugins/foobox-image-lightbox/free/js/foobox.free.min.js': 'https://raw.githubusercontent.com/fooplugins/foobox/master/free/js/foobox.free.min.js'
    }
    
    # Download all files
    for dest_path, url in {**foogallery_files, **foobox_files}.items():
        if not os.path.exists(dest_path):
            download_file(url, dest_path)

def main():
    # Fix paths in index.html
    if os.path.exists('index.html'):
        fix_gallery_paths('index.html')
        print("Fixed paths in index.html")
    
    # Fix paths in bilder/index.html
    if os.path.exists('bilder/index.html'):
        fix_gallery_paths('bilder/index.html')
        print("Fixed paths in bilder/index.html")
    
    # Setup gallery assets
    setup_gallery_assets()

if __name__ == '__main__':
    main() 