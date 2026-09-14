import os
from pathlib import Path
from typing import Dict, List, Optional
import json
import random
import hashlib


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store data as 'alien_id' -> {key1_val1, key2_val2...}

    def load(self, filename: str) -> bool:
        """Load database from disk. Returns True on success."""
        path_data = f"src/{filename}"
        
        ext_path = Path(path_data).stem + ".db" if os.path.exists(ext_path) else None
        
        try:
            with open(ext_path, "r", encoding="utf-8") as f:
                data_bytes = json.load(f)

            if not isinstance(data_bytes, list):
                raise ValueError("Expected JSON array in database definition.")

            self.data = {}
            
            # Iterate over each item in the loaded JSON array to populate keys and values
            for item_data in data_bytes:
                try:
                    alien_id_str = item_data.get('alien_id', '') or ''
                    
                    if isinstance(alien_id_str, str):
                        key = os.path.basename(item_data['alien_id']) or alien_id_str
                    
                    # Handle missing 'name' field gracefully by using alias if provided, else fallback to string value
                    val_list = [item_value.strip() for item_value in item_data.get('key', [])]

                    self.data[key] = {k: v[0].strip() for k, v in zip(key, val_list)}
                except (KeyError, TypeError):
                    continue  # Skip items with invalid data structure or missing fields
                    
            return True
            
        except FileNotFoundError as e:
            print(f"Warning: Database file not found at path '{path_data}'.")
            
            # Create empty default if missing to avoid crashing init
            ext_path = Path('src/test_data.json').stem + ".json" if os.path.exists(ext_path) else None

        try:
            with open(data_file, "w", encoding='utf-8') as f:
                json.dump([], f)

        except json.JSONDecodeError as e:
            print(f"JSON parsing error in '{path_data}': {e}")            
            # Create empty default if missing to avoid crashing init
            ext_path = Path('src/test_data.json').stem + ".json
import os
from pathlib import Path
from typing import Dict, List, Optional
import json
import random
import hashlib


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store data as 'alien_id' -> {key1_val1, key2_val2...}

    def load(self, filename: str) -> bool:
        """Load database from disk. Returns True on success."""
        path_data = f"src/{filename}"
        
        ext_path = Path(path_data).stem + ".db" if os.path.exists(ext_path) else None
        
        try:
            with open(ext_path, "r", encoding="utf-8") as f:
                data_bytes = json.load(f)

            if not isinstance(data_bytes, list):
                raise ValueError("Expected JSON array in database definition.")

            self.data = {}
            
            # Iterate over each item in the loaded JSON array to populate keys and values
            for item_data in data_bytes:
                try:
                    alien_id_str = item_data.get('alien_id', '') or ''
                    
                    if isinstance(alien_id_str, str):
                        key = os.path.basename(item_data['alien_id']) or alien_id_str
                    
                    # Handle missing 'name' field gracefully by using alias if provided, else fallback to string value
                    val_list = [item_value.strip() for item_value in item_data.get('key', [])]

                    self.data[key] = {k: v[0].strip() for k, v in zip(key, val_list)}
                except (KeyError, TypeError):
                    continue  # Skip items with invalid data structure or missing fields
                    
            return True
            
        except FileNotFoundError as e:
            print(f"Warning: Database file not found at path '{path_data}'.")            
            if os.path.exists('src/test_data.json'):
                try:
                    self.data = {}
                    
                    with open('src/test_data.json', 'r') as f:
                        test_data = json.load(f)

                    for item in test_data.get('data', []):
                        alien_id_str = item.get('alien_id', '') or ''
                        
                        if isinstance(alien_id_str, str):
                            key = os.path.basename(item['alien_id']) or alien_id_str
                        
                        val_list = [item_value.strip() for item_value in item.get('key', [])]
