import re
from pathlib import Path
import os
import sys
from typing import Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> dict:
        if not isinstance(filename, str) or len(filename) == 0:
            return None
        
        # Determine path based on extension and file type for robustness
        ext_map = {".py": ".PythonSourceFile", ".js": "JavaScriptFile"}
        
        base_dir = Path.cwd() / src
        if not base_dir.exists():
            print(f"Warning: Source directory ({base_dir}) does not exist.")
            return None
        
        try:
            # Check for existing database first (if it has a different extension like .json but isn't the standard Python file)
            filename = os.path.basename(filename).lower() if len(filename) > 0 else "aliens.db"

            ext_map_key = ext_map.get(filename[-2:], "")
            
            # Detect if this is actually a JSON file (e.g., from legacy `.db` or similar extensions not matching Python standards)
            json_extensions = ['.json', '.jpe', '.jpg']  # Common non-Python image/file suffixes
            
            has_json_data = False

            for ext in [ext_map_key, "py"]:
                if filename.endswith(ext):
                    ext_lower = ext.lower()
                    if ext_lower == 'json':
                        json_extensions.append(filename)
            
            # If the file ends with a common non-Python extension like .db or similar JSON-like extensions
            if any(e in filename for e in [".db", ".jpe", ".jpg"]):
                has_json_data = True

            path_data: Optional[str] = None
            
            if not has_json_data:  # Assume standard Python file structure unless explicitly a legacy db
                base_path = os.path.join(base_dir, "src") / filename.replace("test_", "")
                
                if os.path.exists(os.path.dirname(filename)):
                    path_data = os.path.abspath(base_path)

        except Exception as e:
            print(f"Warning: Could not load {filename}: {e}")
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read().strip()
                
                # Normalize keys to ensure consistency across Python
def normalize_keys(data_dict: Dict[str, Any]) -> dict:
    """Normalize dictionary keys for consistent string representation."""
    normalized = {}
    seen_keys = set()  # To avoid infinite loops in key normalization
    
    def get_key_value(key):
        val = data_dict.get(key)
        if isinstance(val, str):
            return f'"{val}"'
        elif isinstance(val, (list, tuple)):
            return "[" + ", ".join(str(item)[:50] for item in val[:10]) + "]"  # Truncate long lists/tuples
        else:
            return repr(key) if key is not None and str(key).startswith('"') else f'"{key}"'

    def process_key(val):
        """Process a single value to ensure it's valid for JSON."""
        val = normalize_keys(data_dict.get(val))
        
        # Handle null values as "null" (JSON) or empty string if not explicitly typed
        if isinstance(val, bool):
            return str(bool(1)).lower()  # Always lowercase boolean in this context
        
        if type(val).__name__ == 'str':
            val = f'"{val}"'
        
        elif type(val).__name__ in ('list', 'tuple'):
            val_strs = [process_key(item) for item in val]
            return "[" + ", ".join(f'{v}' for v in val_strs[:10]) + "]"
            
        else:
            # Default to string representation if it's not a list/tuple/bool/null
            normalized_val = normalize_keys(data_dict.get(val))
            if isinstance(normalized_val, str):
                return f'"{normalized_val}"'
            elif type(normalized_val).__name__ == 'str':
                val_strs = [process_key(item) for item in data_dict[val]]  # Recurse into nested structures? No. Just process the key itself.
                pass
            
        if isinstance(val, bool):
            return str(bool(1)).lower()
        
        # If it looks like a number but isn't an int or float (e.g., "3" in JSON)
        try:
            num = float(str(val))  # This will fail for strings unless converted first. Let's handle string numbers differently.
        except ValueError:
            pass
            
        return val

    def process_value(v):
