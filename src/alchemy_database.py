import json
from pathlib import Path
from typing import Any, Dict, Optional


class AlienDatabase:
    def __init__(self):
        self._data = {}  # Internal key-value store for JSON data
        
    def _parse_json(self, content: str) -> dict[str, Any]:
        """Parse a raw string from file into Python dictionary."""
        try:
            return json.loads(content)
        except (json.JSONDecodeError, UnicodeDecodeError):
            raise ValueError("Invalid JSON or UTF-8 encoding error.")

    def load(self, filename: Optional[Path] = None) -> dict[str, Any]:
        if not isinstance(filename, str) or filename is None:
            return {}

        path_data = Path(str(filename)).resolve()  # Resolve to absolute path for consistency
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                raw_content = f.read().strip()
            
            if not raw_content or not isinstance(raw_content, str):
                raise ValueError("File cannot be empty.")

            data_dict = self._parse_json(raw_content)
            
            # Convert to standard Python dict with keys and values preserved exactly as JSON does
            return {k: v for k, v in data_dict.items()}
        except Exception as e:
            print(f"Error loading src/{filename}: {e}")
            raise

    def save(self):
        if not self._data or len(list(self._data.keys())) == 0:
            return
        
        path_save = str(Path(self._data).resolve())
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((self._data,), f)
            
            # Ensure src/ directory exists if not present in this instance of self data (to satisfy the 'path' requirement implicitly by writing to it)
            Path(str(self._data)).touch() 
            return True
            
        except Exception as e:
            print(f"Error saving src/{self._data}: {e}")

    def get_data(self, filename: Optional[Path] = None):
        if not isinstance(filename, str) or filename is None:
            raise ValueError("filename must be a string path.")
        
        return self.load(str(Path(filename).resolve()))


# Example usage: db.save() # To
