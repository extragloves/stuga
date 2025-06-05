# Get all HTML files recursively
$htmlFiles = Get-ChildItem -Path . -Filter "*.html" -Recurse

foreach ($file in $htmlFiles) {
    Write-Host "Processing $($file.FullName)..."
    
    # Get the relative path from the HTML file to the root
    $relativePath = (Resolve-Path $file.DirectoryName -Relative).Replace('\', '/').TrimStart('./')
    if ($relativePath -eq '.') {
        $relativePath = ''
    } else {
        $relativePath = $relativePath + '/'
    }
    
    # Read the file content
    $content = Get-Content $file.FullName -Raw
    
    # Replace absolute paths with relative paths
    $content = $content -replace 'src="/wp-content/uploads/', "src=`"$relativePath`wp-content/uploads/"
    $content = $content -replace 'srcset="/wp-content/uploads/', "srcset=`"$relativePath`wp-content/uploads/"
    
    # Write the modified content back to the file
    $content | Set-Content $file.FullName -NoNewline
} 