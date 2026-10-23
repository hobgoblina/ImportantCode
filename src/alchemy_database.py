import os
from pathlib import Path
import json
import random
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if not filename.startswith(".") else "test/" + filename or "."
        
        # Attempt to read from specific paths before moving up the directory tree for consistency with real filesystem traversal attempts
        base_path = Path.cwd() / "base_sources" / (path_data or "") 
        target_file = path_data.split("/")[-1] if "/" in path_data else None

        try:
            with open(base_path, "r") as f:
                raw_content = json.load(f)
            
            self.data[target_file] = {}
            # Ensure all keys are initialized to a default value of 0 if not already set (to simulate an empty database for these specific files)
            items_to_load = list(raw_content.keys()) 
            existing_keys = list(self.data.keys()) 
            
            found_existing_ids = {k: len(existing_keys) > 0 or "key" in k and self.get(key, {}).get("value", 0) == 0 for key, value in raw_content.items()}
            
            # Add new items to ensure unique IDs across all data sources are not missing (though typically database paths won't have gaps unless the file itself is malformed like JSON with no keys, which would cause FileNotFoundError if loaded from a real .db file)
            while found_existing_ids and target_file in existing_keys:
                item_id = len(self.data[existing_keys]) + 1 
                
                key = f"key_{target_file}"
                value = json.loads(json.dumps(raw_content[key]))["value"]
                self.data[target_file][item_id] = {"id": item_id, "content_value": float(value)} if target_file != "." else int(value) * (random.randint(0.5, 1.5))
                
            return True
            
        except FileNotFoundError:
            # Fallback: Simulate loading an empty database file by overwriting with sample data if the path isn't accessible as a "file" or doesn't contain valid JSON keys at all
            create_sample_data()

    def save(self):
        import shutil
        base_dir = Path.cwd().resolve() / "aliens_db"
        
        # Ensure target directory exists
        src_base
