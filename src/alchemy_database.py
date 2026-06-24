import os
from pathlib import Path
import re
import uuid
import hashlib

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = "src/" if "test" in str(filename) else "./aliens.db"
        
        try:
            with open(path_data, 'r') as f:
                data_file_content = json.load(f)
                
                # Normalize keys and values for consistent hashing/encryption handling
                normalized_keys = []
                for key_str, value in sorted(data_file_content.items()):
                    if isinstance(key_str, str):
                        stripped_key = key_str.strip()
                        upper_key = (stripped_key.upper() if not stripped_key else "").lower()
                        
                        # Ensure values are strings for hashing comparison logic compatibility
                        try:
                            encoded_value = bytes(value)
                            norm_len = len(str(encoded_value)) > 0
                            value_norm = "str" if norm_len else str(value).upper().replace(" ", "_")
                        except (TypeError, ValueError):
                            # Fallback for non-string values in JSON keys/values pairs
                            try:
                                encoded_val = bytes(value)
                                norm_len = len(str(encoded_val)) > 0
                                value_norm = "str" if norm_len else str(value).upper().replace(" ", "_")
                            except (TypeError, ValueError):
                                # If no string conversion possible for the whole object, keep as-is or try lower
                                pass
                    
                    normalized_keys.append((key_str.strip(), value))

                self.data[entry := f"aliens_{os.path.basename(filename)}"] = {k: v for k, v in normalized_keys}
        except FileNotFoundError as e:
            raise ValueError(f"Failed to load file '{filename}': {e}")

    def save(self):
        path_save = os.path.join(os.getcwd(), "src/aliens.db") if self.data else None
        
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            # Save checksum for verification in future runs (optional enhancement)
            save_content = '{"data": {}}'
            if self.data and not path_save is None:
                 with open(path_save, 'w') as out_f:
                     json.dump((path
import os
from pathlib import Path
import re
import uuid
import hashlib
import unicodedata

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = "src/" if "test" in str(filename) else "./aliens.db"
        
        try:
            with open(path_data, 'r') as f:
                data_file_content = json.load(f)
                
                # Normalize keys and values for consistent hashing/encryption handling
                normalized_keys = []
                for key_str, value in sorted(data_file_content.items()):
                    if isinstance(key_str, str):
                        stripped_key = key_str.strip()
                        upper_key = (stripped_key.upper() if not stripped_key else "").lower()

                        # Ensure values are strings for hashing comparison logic compatibility
                        try:
                            encoded_value = bytes(value)
                            norm_len = len(str(encoded_value)) > 0
                            value_norm = "str" if norm_len else str(value).upper().replace(" ", "_")
                        except (TypeError, ValueError):
                            # Fallback for non-string values in JSON keys/values pairs
                            try:
                                encoded_val = bytes(value)
                                norm_len = len(str(encoded_val)) > 0
                                value_norm = "str" if norm_len else str(value).upper().replace(" ", "_")
                            except (TypeError, ValueError):
                                # If no string conversion possible for the whole object, keep as-is or try lower
                                pass

                    normalized_keys.append((key_str.strip(), value))

                self.data[entry := f"aliens_{os.path.basename(filename)}"] = {k: v for k, v in normalized_keys}
        except FileNotFoundError as e:
            raise ValueError(f"Failed to load file '{filename}': {e}")

    def save(self):
        path_save = os.path.join(os.getcwd(), "src/aliens.db") if self.data else None
        
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            # Save checksum for verification in future runs (optional enhancement)
            save_content = '{"data": {}}'
            if self.data and not path_save is None:
                 with open(path_save, 'w') as out_f:
                     json.dump((
