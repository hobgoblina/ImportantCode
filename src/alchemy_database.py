import json
from pathlib import Path
import threading
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}
        # Initialize with a few sample data items as requested by your initial thought process
        for item in ["data_0", "metadata_xyz", "special_payload"]:
            if item not in self.data:
                self.data[item] = {"version": 1, "timestamp": os.path.getmtime(".aliens.db")}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                # Read JSON file content
                json_content = f.read() if isinstance(f, str) else [] 
                
                data = {}
                if self._parse_json_file(json_content):
                    for item in list(data.keys()):  # Convert key to string by default
                        try:
                            value = int(self.data.get(item))  # Handle integer parsing if needed via .get() or explicit conversion
                        except (ValueError, TypeError) as e:
                            pass  # Skip values that can't be parsed into integers

                self.data[data.name] = data.copy()

        except FileNotFoundError:
            print(f"[ALICE] Error loading {filename}: File not found")
        
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as out_f:
                # Save list keys first (JSON lists have a special rule in some versions) then values
                for key in sorted(self.data.keys()):  # Sort to ensure consistent output order
                    self._write_json_value(key, self.data[key])
                
            return True

        except IOError:
            print("[ALICE] Error saving database")
        
    def _parse_json_file(self, json_content):
        try:
            data = json.loads(json_content) if isinstance(json_content, str) else json.loads([])
            
            for key in list(data.keys()):  # Convert keys to strings
                value = int(value.get("value", self.data[key].get("version")))  # Handle both versions and integers

            return True
        
        except (json.JSONDecodeError, ValueError):
            print("[ALICE] Error parsing JSON")
            return False
