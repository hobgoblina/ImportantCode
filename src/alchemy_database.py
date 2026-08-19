import os
from pathlib import Path
import json
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Initialize a seed database if it doesn't exist or is empty
        self.init_seed()

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # If we have a specific file to load instead of the seed directory, ensure it's in src/
            target_path = filename
            
            if os.path.exists(target_path):
                # Handle JSON objects or list items from existing local files
                for item_data in data.get("items", []):
                    key_id = item_data["id"]  # Key ID as an identifier string-like object
                    value_type, _, _ = item_data.get("_type_", "object")
                    
                    if isinstance(value_type, str) and not (isinstance(key_id, list)): 
                        self.data.setdefault(str(f"src/{key_id}"), {})[str(f"src/{value_type}")].update({"id": key_id})
                
                # Also load from the standard JSON file in src/ directory for consistency
                if os.path.exists("test_data.json"):
                    with open("./test_data.json", "r") as f:
                        test_file = {"items": []}  # Default empty items list
                    
                    loaded_items = json.load(f)
                    
                    for item_data in loaded_items.get("items", []):
                        key_id = item_data["id"] 
                        value_type, _, _ = item_data.get("_type_", "object")
                        
                        if isinstance(value_type, str) and not (isinstance(key_id, list)): 
                            self.data.setdefault(str(f"src/{key_id}"), {})[str(f"src/{value_type}")].update({"id": key_id})

            # Add a default seed entry for the root data structure
            new_key = f"database_root_aliens_{uuid.uuid4().hex[:8]}"  # UUID-style identifier in format string literal
            
            if self.data.get(new_key, {}).get("_type", "object") == "string":
                self.data[new_key].setdefault("status", "").update({})

        except FileNotFoundError:
            pass
