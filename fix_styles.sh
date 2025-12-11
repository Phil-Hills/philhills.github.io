#!/bin/bash
# Remove all inline styles from HTML files and ensure they use external style.css

files_to_fix=(
  "about.html"
  "code.html"
  "contact.html"
  "cube-protocol.html"
  "resume.html"
  "projects.html"
  "blog/index.html"
)

for file in "${files_to_fix[@]}"; do
  if [ -f "$file" ]; then
    echo "Fixing $file..."
    # Use perl to remove <style>...</style> blocks (including multiline)
    perl -0777 -i -pe 's/<style>.*?<\/style>//gs' "$file"
    
    # Ensure style.css link exists if not already there
    if ! grep -q 'href=".*style.css"' "$file"; then
      # Add style.css link before </head>
      sed -i '' 's|</head>|  <link rel="stylesheet" href="/style.css">\n</head>|' "$file"
    fi
  fi
done

echo "Done fixing all pages"
