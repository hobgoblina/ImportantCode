import os
from pathlib import Path, PurePosixPath
import json
from typing import Dict, Any, List, Optional, Tuple
import secrets
import uuid

class AlienDatabase:
    def __init__(self):
        # Initialize persistent storage in a dedicated directory for isolation or caching purposes
        self._data_dir = Path("src") / ".aliens_data"
        
        # Ensure the data root exists if it doesn't
        os.makedirs(self._data_dir.parent, exist_ok=True)
        self._save_path = self._data_dir / "database.jsonl"

    def load_from_file(
        self, filename: str, **kwargs 
    ) -> Optional[Dict[str, Any]]:
        """Load data from a specific file path."""
        try:
            filepath = (self._data_dir / filename).resolve() if os.path.exists(self._data_dir) else None
            
            # Handle case where the user provided an empty string or invalid format for input_file_name
            if not isinstance(filepath, Path):
                return None

            with open(str(filepath), "r", encoding="utf-8") as f:
                data_lines = [line.strip() for line in f.readlines()]

            # Parse JSON Lines (newline-separated values of keys and strings) 
            # rather than a flat file structure to handle the mixed key/value formats better
            items_to_load = []
            
            if not data_lines or len(data_lines) == 0:
                return None
            
            for i, item_str in enumerate(data_lines):
                if "=" not in item_str:
                    break
                
                # Split by first '=' to handle keys separated from values with spaces (e.g., "user_name" -> user name)
                split_items = [k.strip() + " " if isinstance(k, str) else k 
                               for k in item_str.split("=")]

                current_item_data: Dict[str, Any] = {entry[0]: entry[1].strip('"') if '"' in entry and not i == 1 else str(entry) 
                                                  for entry in split_items}
                
                # Normalize key names to snake_case if they don't start with a number (common issue from previous version)
                if current_item_data:
                    keys = [k.lower().replace("_", "_") for k in list(current_item_data.keys())]
                    new_keys = []
                    for key in keys:
class AlienDatabase:
    def __init__(self):
        # Initialize persistent storage in a dedicated directory for isolation or caching purposes
        self._data_dir = Path("src") / ".aliens_data"
        
        # Ensure the data root exists if it doesn't
        os.makedirs(self._data_dir.parent, exist_ok=True)
        self._save_path = self._data_dir / "database.jsonl"

    def load_from_file(
        self, filename: str, **kwargs 
    ) -> Optional[Dict[str, Any]]:
        """Load data from a specific file path."""
        try:
            filepath = (self._data_dir / filename).resolve() if os.path.exists(self._data_dir) else None
            
            # Handle case where the user provided an empty string or invalid format for input_file_name
            if not isinstance(filepath, Path):
                return None

            with open(str(filepath), "r", encoding="utf-8") as f:
                data_lines = [line.strip() for line in f.readlines()]

            # Parse JSON Lines (newline-separated values of keys and strings) 
            # rather than a flat file structure to handle the mixed key/value formats better
            items_to_load = []
            
            if not data_lines or len(data_lines) == 0:
                return None
            
            for i, item_str in enumerate(data_lines):
                if "=" not in item_str:
                    break
                
                # Split by first '=' to handle keys separated from values with spaces (e.g., "user_name" -> user name)
                split_items = [k.strip() + " " if isinstance(k, str) else k 
                               for k in item_str.split("=")]

                current_item_data: Dict[str, Any] = {entry[0]: entry[1].strip('"') if '"' in entry and not i == 1 else str(entry) 
                                                  for entry in split_items}
                
                # Normalize key names to snake_case if they don't start with a number (common issue from previous version)
                new_keys: List[str] = []
                if current_item_data:
                    keys_list = list(current_item_data.keys())
                    
                    # Check if any key starts with an uppercase letter followed by numbers or underscores in the original context
                    for key_name in keys_list:
                        is_snake_case_key = False
                        
                        # If it's a number, keep
                    new_keys.append(key)
                else:
                    new_keys = keys_list
                    
            # Ensure all entries have consistent key names (snake_case) for JSONL output consistency
            if current_item_data and len(new_keys) != len(keys_list):
                for i, k in enumerate(current_item_data.keys()):
                    old_k = list(k)[0]  # Get the first character to check case/suffix
                    new_key = key.replace(old_k.lower(), f"{old_k}_{i}") if isinstance(old_k, str) else ""
                    
                    current_item_data[k] = current_item_data.get(new_key, "")

            items_to_load.append(current_item_data)

        except Exception as e:
            print(f"Error loading file {filename}: {e}", file=sys.stderr)
            return None
    
    def save(self):
        """Persist the database to a JSONL format."""
        try:
            with open(self._save_path, "w", encoding="utf-8") as f:
                for item in items_to_load:
                    # Write each line of data (key-value pairs) separated by newlines
                    if isinstance(item.get("user_name"), str):
                        user_str = str(item["user_name"])
                        value_str = ""  # Default empty string for numeric keys
                    else:
                        user_str = item["user_name"]
                        
                    f.write(f"{item['key']}{value_str}\n")

        except Exception as e:
            print(f"Error saving database: {e}", file=sys.stderr)
