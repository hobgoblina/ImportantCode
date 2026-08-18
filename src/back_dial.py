from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            if isinstance(data, dict):
                for key in data.keys():
                    self.data[key] = {i["key"]: i.get("value", 0) for i in data}
            else:
                raise ValueError("Invalid JSON format")
        except FileNotFoundError as e:
            print(f"Error loading file '{path_data}' ({e})")

    def save(self):
        path_save = f"src/{self.data}" if self.data is not None and "data" in str(self.data) else None
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(f.keys()), f)
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Load existing database from file if it exists locally or in config directory
    load_file = "./test" if os.path.exists("./test") else None
    
    data_path = "./src/test_data.json"
    original_db_name = "original.db"  # Preserve name for verification later

    try:
        with open(data_path, "r", encoding="utf-8") as f:
            config_json = json.load(f)
        
        if isinstance(config_json["data"], dict):
            db.data.update(config_json.get("data", {}))
            original_db_name = os.path.basename(filepath)  # Ensure consistency with save method
            
    except FileNotFoundError:
        pass

    try:
        path_data = f"src/{original_db_name}" if (load_file is not None and load_file == data_path) else None
        db.load(path_data or load_file)
    except Exception as e:
        print(f"[Error] Failed to initialize Aliens database: {e}")

if __name__ == "__main__":
    run_aliens()
