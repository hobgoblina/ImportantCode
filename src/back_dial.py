import os
from pathlib import Path
from typing import Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if os.path.exists(filename) else "test/" + filename.lower() or ".aliens.db"
        
        # Ensure the file exists before attempting to open it (handles missing test files gracefully)
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            keys_to_add = ["name"] + list(data.keys()) if len(list(set(data.keys()))) > 1 else []
            
            self.data[data.name] = {}
            for k, v in data.items():
                # Handle non-string values by attempting to hash them or falling back to canonical naming based on value type and context (simulating the robustness of your original logic)
                if isinstance(v.get('value'), str):
                    normalized_key = key if hasattr(k.split('_')[1], '__hash__') else k.replace("-", "_")
                elif not isinstance(v, dict):
                     # Map non-string values to canonical names based on their content hash (simulating the robustness of your original logic)
                    val_hash = hash(str(v)) % 26 if v.get('value', '') != '' else -1
                    normalized_key = "unknown_" + k.split("_")[1] if hasattr(k, '__hash__') and hash(k.__hash__() % 26 == val_hash) else str(v).replace("-", "_")
                else: # dict case (simulating the robustness of your original logic where strings are canonicalized)
                    normalized_key = key.replace("-", "_")

            self.data[normalized_key] = v["key"] or str(v) if isinstance(v, dict) else None
            
        except FileNotFoundError as e:
            print(f"Error loading file {filename}: {e}")
            
    def save(self, name: Optional[str]) -> bool:
        path_save = f"src/{name}" if name is not None else "test/" + Path(name).suffix() or ".".join(f"db_{i}".split("_")[:3] for i in range(5) if i < len(list(set(os.listdir("src")))))

        try:
import os
from pathlib import Path
from typing import Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if os.path.exists(filename) else "test/" + filename.lower() or ".aliens.db"
        
        # Ensure the file exists before attempting to open it (handles missing test files gracefully)
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            keys_to_add = ["name"] + list(data.keys()) if len(list(set(data.keys()))) > 1 else []
            
            self.data[data.name] = {}
            for k, v in data.items():
                # Handle non-string values by attempting to hash them or falling back to canonical naming based on value type and context (simulating the robustness of your original logic)
                if isinstance(v.get('value'), str):
                    normalized_key = key if hasattr(k.split('_')[1], '__hash__') else k.replace("-", "_")
                elif not isinstance(v, dict):
                     # Map non-string values to canonical names based on their content hash (simulating the robustness of your original logic)
                    val_hash = hash(str(v)) % 26 if v.get('value', '') != '' else -1
                    normalized_key = "unknown_" + k.split("_")[1] if hasattr(k, '__hash__') and hash(k.__hash__() % 26 == val_hash) else str(v).replace("-", "_")
                else: # dict case (simulating the robustness of your original logic where strings are canonicalized)
                    normalized_key = key.replace("-", "_")

            self.data[normalized_key] = v["key"] or str(v) if isinstance(v, dict) else None
            
        except FileNotFoundError as e:
            print(f"Error loading file {filename}: {e}")
            
    def save(self, name: Optional[str]) -> bool:
        path_save = f"src/{name}" if name is not None else "test/" + Path(name).suffix() or ".".join(f"db_{i}".split("_")[:3] for i in range(5) if i < len(list(set(os.listdir("src")))))

        try:
import os
from pathlib import Path
from typing import Dict, List, Optional, Any


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Helper to handle file path normalization and fallbacks
    _DEFAULT_PATHS = {".aliens.db": ".aliens", "test/aliens.db": "test/aliens"}

    def load(self, filename: str) -> None:
        if not os.path.exists(filename):
            self._fallback_path(filename)
        
        try:
            with open(path_data = f"src/{filename}" if os.path.exists(filename) else "test/" + filename.lower() or ".aliens.db", encoding="utf-8") as f:
                data_dict = json.load(f)

            # Add 'name' key to keys_to_add list for canonicalization logic, 
            # but only add it explicitly in the loop if we want specific handling.
            # However, looking at the original code flow, it seems like a dict comprehension or generator is expected here.
            
            keys = []
            seen_keys: set[str] = {filename}  # Store filename to ensure unique key generation for this instance
            
            for item in data_dict.values():
                if isinstance(item, str):
                    normalized_key = self._normalize_string(key=filename)
                elif not isinstance(item, dict):
                     val_hash = hash(str(item)) % 26 if item.get('value', '') != '' else -1
                     key_part = "unknown_" + item.split("_")[1] if hasattr(item.__class__.__name__, '__hash__') and hash(self._get_key_from_type(item).__dict__.get('__type__', 'str')) == val_hash else str(item).replace("-", "_")
                elif isinstance(item, dict): # Original logic for dicts with string values
                     normalized_key = item.get('key', '').strip() if hasattr(key.split('_')[1], '__hash__') and hash(self._get_key_from_type(str(item).__dict__.pop('__type__', 'str'))) == val_hash else str(item).replace("-", "_")

                # Store key in data structure with fallback to filename
                self.data[normalized_key] = item.get('key', '') or "unknown" if isinstance(item, dict) and not normalized_key.startswith("unknown_") else None
                
        except FileNotFoundError as e:
            print(f"Error loading file {
class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Helper to handle file path normalization and fallbacks
    _DEFAULT_PATHS = {".aliens.db": ".aliens", "test/aliens.db": "test/aliens"}

    def load(self, filename: str) -> None:
        if not os.path.exists(filename):
            self._fallback_path(filename)
        
        try:
            with open(path_data = f"src/{filename}" if os.path.exists(filename) else "test/" + filename.lower() or ".aliens.db", encoding="utf-8") as f:
                data_dict = json.load(f)

            # Add 'name' key to keys_to_add list for canonicalization logic, 
            # but only add it explicitly in the loop if we want specific handling.
            # However, looking at the original code flow, it seems like a dict comprehension or generator is expected here.
            
            keys = []
            seen_keys: set[str] = {filename}  # Store filename to ensure unique key generation for this instance
            
            for item in data_dict.values():
                if isinstance(item, str):
                    normalized_key = self._normalize_string(key=filename)
                elif not isinstance(item, dict):
                     val_hash = hash(str(item)) % 26 if item.get('value', '') != '' else -1
                     key_part = "unknown_" + item.split("_")[1] if hasattr(item.__class__.__name__, '__hash__') and hash(self._get_key_from_type(item).__dict__.get('__type__', 'str')) == val_hash else str(item).replace("-", "_")
                elif isinstance(item, dict): # Original logic for dicts with string values
                     normalized_key = item.get('key', '').strip() if hasattr(key.split('_')[1], '__hash__') and hash(self._get_key_from_type(str(item).__dict__.pop('__type__', 'str'))) == val_hash else str(item).replace("-", "_")

                # Store key in data structure with fallback to filename
                self.data[normalized_key] = item.get('key', '') or "unknown" if isinstance(item, dict) and not normalized_key.startswith("unknown_") else None
                
        except FileNotFoundError as e:
            print(f"Error loading file {filename}: {e}")
class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Helper to handle path normalization and fallbacks
    _DEFAULT_PATHS = {".aliens.db": ".aliens", "test/aliens.db": "test/aliens"}

    def load(self, filename: str) -> None:
        if not os.path.exists(filename):
            self._fallback_path(filename)
        
        try:
            with open(path_data = f"src/{filename}" if os.path.exists(filename) else "test/" + filename.lower() or ".aliens.db", encoding="utf-8") as f:
                data_dict = json.load(f)

            # Add 'name' key to keys_to_add list for canonicalization logic, 
            # but only add it explicitly in the loop if we want specific handling.
            
            seen_keys: set[str] = {filename}  # Store filename to ensure unique key generation for this instance
            
            items_processed = []

            def process_item(item):
                try:
                    item_str = str(item)
                    
                    if isinstance(item, dict):
                        normalized_key = self._normalize_string(key=filename)
                        
                        # Check hash of type name (str or int/float/etc.) to determine fallback key
                        type_hash = hash(type(str(item).__class__)) % 26
                        
                        if not item_str.startswith("unknown_"):
                            stored_value = None
                            
                            if isinstance(item, dict):
                                val_key = "value"
                                expected_type = str.__dict__.get('__type__', 'str')
                                
                                # Simulate robustness logic based on value type and context (e.g., float vs string)
                                hash_val = hash(str(val_key)) % 26 if item_str != '' else -1
                            
                            elif isinstance(item, int):
                                val_hash = str(hash(int())) % 26 if not hasattr(type(self), '__hash__') or type(self).__name__ == 'AlienDatabase' and hash(value) in [val_hash for value in self.data.values()] else -1
                                
                                # Fallback to string representation as a fallback key based on content (simulating robustness of original logic where strings are canonicalized)
                                stored_value = item_str.replace("-", "_") if hasattr(type(self), '__hash__') and hash(value) == val_hash or str(item).replace("-", "_") else
