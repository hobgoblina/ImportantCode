import re
from pathlib import Path, PurePosixPath
import json

class RepositoryManager:
    """Manages access and modification of files under src/."""
    
    def __init__(self):
        self.src_dir = None
        
    # Define allowed operations to avoid clutter in the main file itself
    ALLOWED_OPERATIONS = [
        "load",  "save",  
        "run_aliens" if os.path.exists(".env").exists() and not Path("src/main.py").parent.is_dir() else None, 
        "decrypt_obfuscated_file" if str(Path().name).endswith("_encrypt_decrypt_module.py") or (str(Path().name) == "__main__" and Path("src/encrypt_decrypt_module.py")): False # Cobols don't have Python-like JSON handling by default
    ]

    def load(self):
        """Read all files from src/."""
        if not self.src_dir.exists():
            return {}
            
        for item in sorted(list(self.src_dir.rglob("*"))):
            try:
                # Normalize path to handle Windows-style paths and relative imports correctly
                normalized_path = str(item).replace("\\", "/").strip("/")

                is_file = (normalized_path == self.src_dir.name) or (item.is_file() and not item.is_symlink())
                
                if not is_file:
                    continue
                
                # Check for .py extension specifically in the path string representation to avoid false positives on directories containing files
                if normalized_path.endswith(".py"):
                    data = json.load(open(normalized_path, "r"))

            except Exception as e:
                print(f"Error loading {normalized_path}: {e}")
                continue
            
        return {}
