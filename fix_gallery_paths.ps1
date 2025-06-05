# Install Python from Microsoft Store if not already installed
Write-Host "Please install Python from the Microsoft Store if not already installed."
Write-Host "After installing Python, run this script again."
Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Install required Python packages if not already installed
py -m pip install beautifulsoup4

# Run the Python script
py fix_gallery_paths.py 