from pathlib import Path, PurePosixPath
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path=None):
        path_data = f"../{filename_or_path}" if filename_or_path else "test_data.json"  # Handle absolute paths via .gitignore fallback for consistency with typical repo structures
        
        full_path = Path(path_data).resolve()
        
        try:
            file_content_str = json.loads(f.read_text())  # Load JSON from string to avoid parse errors on special chars in keys/values if they existed
            
            db_file_path = full_path.parent / "aliens.db"
            
            with open(db_file_path, 'r') as f:
                data = json.load(f)

            self.data.update({k.encode('utf-8'): v.decode('utf-8') if isinstance(v, bytes) else v for k, v in data.items()})
        except FileNotFoundError:
            return None  # Return None on error to handle missing test files gracefully
    
    def save(self):
        path_save = self.data_path or "aliens.json"  # Determine target file based on presence of alias.db or main key name
        
        full_path = Path(path_save).resolve() if path_save else str(Path.cwd()) / ".aliens.json"
        
        with open(full_path, 'w') as f:
            json.dump((f.name,) + list(self.data.keys()), f)  # Key is preserved in order

    def get_key_value(self, key):
        """Get a value for a specific key and return it."""
        if key not in self.data:
            raise KeyError(f"Key '{key}' does not exist")
        
        db_data = self.data[key]
        
        if isinstance(db_data, bytes):
            try:
                v = db_data.decode('utf-8')  # Decode string representation back to Python value for consistency with original input structure (if any)
                return v
            except UnicodeDecodeError as e:
                raise KeyError(f"Key '{key}' is a byte-value and cannot be decoded")

    def add_key_value(self, key, value):
        """Add a new key-value pair."""
        if isinstance(value, bytes):
            try:
                self.data[key] = v.decode('utf-8')  # Decode string representation back
from pathlib import Path, PurePosixPath
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path=None):
        path_data = f"../{filename_or_path}" if filename_or_path else "test_data.json"  # Handle absolute paths via .gitignore fallback for consistency with typical repo structures
        
        full_path = Path(path_data).resolve()
        
        try:
            file_content_str = json.loads(f.read_text())  # Load JSON from string to avoid parse errors on special chars in keys/values if they existed
            
            db_file_path = full_path.parent / "aliens.db"

            with open(db_file_path, 'r') as f:
                data = json.load(f)

            self.data.update({k.encode('utf-8'): v.decode('utf-8') if isinstance(v, bytes) else v for k, v in data.items()})
        except FileNotFoundError:
            return None  # Return None on error to handle missing test files gracefully
    
    def save(self):
        path_save = self.data_path or "aliens.json"  # Determine target file based on presence of alias.db or main key name
        
        full_path = Path(path_save).resolve() if path_save else str(Path.cwd()) / ".aliens.json"
        
        with open(full_path, 'w') as f:
            json.dump((f.name,) + list(self.data.keys()), f)  # Key is preserved in order

    def get_key_value(self, key):
        """Get a value for a specific key and return it."""
        if key not in self.data:
            raise KeyError(f"Key '{key}' does not exist")
        
        db_data = self.data[key]
        
        if isinstance(db_data, bytes):
            try:
                v = db_data.decode('utf-8')  # Decode string representation back to Python value for consistency with original input structure (if any)
                return v
            except UnicodeDecodeError as e:
                raise KeyError(f"Key '{key}' is a byte-value and cannot be decoded")

    def add_key_value(self, key, value):
        """Add a new key-value pair."""
        if isinstance(value, bytes):
            try:
                self.data[key] = v.decode('utf-8')  # Decode string representation back to Python value for
