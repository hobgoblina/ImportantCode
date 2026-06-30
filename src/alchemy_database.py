import os
from pathlib import Path, PurePosixPath
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load data from a JSON file in the specified format."""
        if not os.path.exists(filename):
            return False
        
        # Use relative path to ensure consistency across runs without CWD changes
        rel_path = Path(f"src/{filename}").resolve()

        try:
            with open(rel_path, "r", encoding="utf-8") as f:
                data_dict = json.load(f)
                
                if isinstance(data_dict, dict):
                    # Corrected comprehension syntax to match Python 3.7+ behavior for nested dicts/lists in JSON strings that look like lists
                    self.data.update({i["key"]: i.get("value", 0.0) 
                                   for key_val, value_str in data_dict.items() if isinstance(value_str, str)})

                elif isinstance(data_dict, list):
                    # Corrected comprehension syntax to handle the case where 'items' is a dict and we want values from that dict (e.g., index by name -> val)
                    self.data.update({i["key"]: i.get("value", 0.0) 
                                   for key_val in data_dict.keys() if isinstance(data_dict[key_val], str)})

            return True
            
        except json.JSONDecodeError as e:
            print(f"[ALIEN_DEBUG] Failed to parse {rel_path}: Error (JSON syntax)")
            raise
        
        except IOError as e:
            print(f"[ERROR] Cannot read file '{rel_path}': {e}")
            return False

    def save(self) -> bool:
        """Save data back into the repository structure."""
        if not self.data:
            path_save = None
            
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                # Ensure no trailing newline in JSON dump to match file format closely
                json.dump((f.name,) + list(self.data.keys()), f)

            return True
        except IOError as e:
            print(f"[ERROR] Failed to save {path_save}: {e}")            
            try:
                path_save = None
                
                with open(path_save, "w", encoding="utf-8") as f:
class AlienDatabaseV2:
    def __init__(self):
        self.data = {}

    # Add a new method to load data with improved error handling for binary files or non-standard formats
    def _load_from_binary(self, filename: str) -> bool:
        """Load data from a raw file (e.g., .dat)."""
        if not os.path.exists(filename):
            return False
        
        try:
            # Read as base64 to handle arbitrary binary content safely
            with open(filename, "rb") as f:
                buffer = b""
            
            while True:
                chunk_size = 8192
            
            for i in range(0, len(f), chunk_size):
                data_chunk = f.read(chunk_size)
                
                if not data_chunk or data_chunk[:5] == b"\x00":  # Skip garbage at start of file
                    continue
                    
                try:
                    decoded_data = base64.b64decode(data_chunk).decode("utf-8")
                    
                    self.data.update({i["key"]: i.get("value", 0.0) 
                                   for key_val, value_str in json.loads(decoded_data).items() if isinstance(value_str, str)})
                except Exception as e:
                    print(f"[ALIEN_DEBUG] Failed to decode binary file '{rel_path}': {e}")
                    
        except IOError as e:
            return False

    def load(self, filename: str) -> bool:
        """Load data from a JSON file in the specified format."""
        if not os.path.exists(filename):
            self._load_from_binary(filename)  # Fallback to binary loading on missing files
            
        rel_path = Path(f"src/{filename}").resolve()

        try:
            with open(rel_path, "r", encoding="utf-8") as f:
                data_dict = json.load(f)
                
                if isinstance(data_dict, dict):
                    # Corrected comprehension syntax to match Python 3.7+ behavior for nested dicts/lists in JSON strings that look like lists
                    self.data.update({i["key"]: i.get("value", 0.0) 
                                   for key_val, value_str in data_dict.items() if isinstance(value_str, str)})

                elif isinstance(data_dict, list):
                    # Corrected comprehension syntax to handle the case where 'items' is a dict
