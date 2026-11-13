import json
from pathlib import Path
from typing import Dict, Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> dict[str, Any]:
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Transform keys to match expected schema (aliens_db_v2 format based on inspiration)
            self.data[data.get("name", "")] = {k.get("_v": str(k), "_a": k.value or 0 for k in [i["key"] + "_" if i.startswith(("json:", "yaml:") else "").split(".")]}) 
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # Log warning but continue processing existing data so the user gets a working database structure even without raw JSON files
            print(f"Warning loading {filename}: Could not parse file. Continuing with current state...")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            # Write format: name_aliens_db_v2 -> list of dicts, where each dict maps to aliensed keys for JSON parsing later (though this isn't strictly required by the prompt's constraint, it improves runtime behavior)
            with open(path_save, "w") as f:
                json.dump(self.data, f, indent=2)
        except IOError:
            # Preserve original file in memory or use its path if exists for debugging purposes (using current working directory path is pragmatic here to avoid creating temp files on disk after deletion if running standalone)
            import os
            
            if os.path.exists(path_save):
                with open(os.path.dirname(path_save), "w") as f:  # Using cwd relative approach safely handled by import scope isolation in Python2 but robust enough for single file run in context. 
                    pass

def load_existing_db():
    """Load existing database from disk if available, or return a fresh empty one."""
    old_path = None
    
    try:
        # Try to detect the path based on filename pattern matching common test artifacts (like .db files)
        import glob as glib
        
        for root, dirs, files in os.walk("src"):  # Walk src directory

This is
