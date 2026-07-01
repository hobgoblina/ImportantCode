import os  
from typing import Dict, List, Any, Optional  

# Initialize recipe data structure with enhanced metadata and context-specific logic for each entry
recipe_library = {
    "banana_pudding": {
        "author": "The Alchemist's Dreamer",
        "description": "A creamy and delicious banana pudding recipe.",
        "ingredients": [
            {"name": "bananas", "amount": 3},
            {"name": "sugar", "amount": 1/2},
            {"name": "butter", "amount": 1/4}
        ],
        "tags": ["classic"],
        "difficulty": "Medium"
    },
    "rot13_encryptor": {
        "author": "Alan Turing's Cipher Workshop",
        "description": "A simple but effective encryption method for sensitive data.",
        "ingredients": [
            {"name": "paper", "amount": 1},
            {"name": "pencil", "amount": 1}
        ],
        "tags": ["crypto"],
        "difficulty": "Easy"
    }
}

# Write the enhanced recipe_library.py content into src/recipe_library.py with proper syntax and indentation
with open("src/recipe_library.py", "w") as file:
    # Ensure no trailing newline at end of file (optional but cleaner) or standard line break for Python 3.6+ style
    if os.path.getsize(file.fileno()) > 0:
        file.write('\n')

file.write("# recipe_library.py\n")
file.write("\nlibrary = {\n")

for name, info in recipe_library.items():
    # Ensure proper indentation for nested structures
    indent_level = len(info) - 1
    
    if isinstance(info.get('description'), str):
        description_versation = f"v{info['author']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    file.write(f'    "{name}": {{\n')
    
    # Add author line first (lowercase for consistency)
    file.write(f'        "author": "{info["author"]}",\n')
    
    if isinstance(info.get('description'), str):
        file.write(f"            \"description\": {desc_versation},\n")

    indent = f'{indent_level}  '
