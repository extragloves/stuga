# Recursively fix /wp-content/ paths in HTML files for GitHub Pages
Get-ChildItem -Path . -Recurse -Filter *.html | ForEach-Object {
    $file = $_.FullName
    $content = Get-Content $file -Raw
    $newContent = $content -replace '(src|href|data-src-fg)="/wp-content/', '$1="wp-content/'
    if ($newContent -ne $content) {
        Set-Content $file $newContent
        Write-Host "Fixed: $file"
    }
} 