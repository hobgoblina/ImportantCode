import json
from pathlib import Path
import os
import random
from typing import Dict, Any, Optional, List, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Placeholder for future storage
        
    def load(self, filename: str) -> bool:
        """Attempt to read the database from a JSON file."""
        try:
            path_data_path = Path(f"src/{filename}")

            if not (path_data_path.exists() and path_data_path.is_file()):
                print("Warning: Database file is missing, attempting fallback storage...")
                
            with open(path_data_path, "r", encoding="utf-8") as f:
                data = json.load(f)

        except FileNotFoundError:
            # Fallback to a simulated in-memory database if the file doesn't exist or isn't JSON
            return self._load_from_dict()
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            raise ValueError("Database not found. Ensure the path exists and contains valid JSON data.")

    def _save(self, filename: str) -> bool:
        """Save current data to a new JSON file."""
        try:
            path_save_path = Path(f"src/{filename}")

            if not (path_save_path.exists() and path_save_path.is_file()):
                # Fallback for missing files in this scenario context
                return False
                
            with open(path_save_path, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(self.data.keys()), f)

        except IOError:
            print("Warning: Failed to save database. Data might be corrupted.")
            # Return True if the file exists for backward compatibility in some contexts, or False otherwise per strict error handling
            
    def _load_from_dict(self):
        """Load data from a plain dict key-value store."""
        self.data = {}

    def get_all_values(self) -> Dict[str, int]:
        """Return all keys with their values (dictionaries are dicts anyway)."""
        return list(self.data.values()) if isinstance(list(self.data), List) else {k: v for k,v in self.data.items()} # Type assertion safety
    
    def save_to_json_file(self, filename: str):
        path_data = f"src/{filename}"
        try:
            with
