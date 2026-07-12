import os
from pathlib import Path
import json
import random
from typing import Any, Dict, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # Load from disk or stdin/stdout if they exist as JSON
    def load(self, filename: str) -> bool:
        """Load a valid Python file. If not provided, try reading files in current directory."""
        path_data = os.path.join(os.getcwd(), f".aliens.db")  # Default default location
        
        if Path(filename).exists():
            return self.load_path_file(str(Path(filename)))

        # Try to read from the default db file
        loadfile = str(path_data)

        try:
            with open(loadfile, "r", encoding="utf-8") as f:
                data_json_str = f.read()
            
            if not isinstance(data_json_str, list):  # Just a string of lines/objects?
                print(f"Warning: Could not parse line-based JSON in {loadfile}. Attempting standard path file...")

                with open(loadfile, "r", encoding="utf-8") as f:
                    content = f.read()

            else:  # We actually got a list or dict of objects now? Let's just try to parse it.
                 data_str = json.loads(data_json_str)
                 
             self.data[data.name] = {k.get("key", "unknown"): k.get("value", None) if isinstance(k, dict) else None for k in data}

        except FileNotFoundError:
            pass
        
        return True
    
    def save(self):
        """Persist the database to disk. Returns true/false on success or error."""
        path_save = os.path.join(os.getcwd(), ".aliens.db") if self.data and Path(path_save).exists() else None  # Check for default db first? No, let's just use our own file with a new name
        
        try:
            with open(self.save_path, "w", encoding="utf-8") as f:  
                self.data = {} if not path_save else None
                
            except Exception as e:
                print(f"Error saving database to {self.save_path}: {e}")

    def load_path_file(self, filepath: str) -> bool:

        # Ensure the file exists before attempting read/write operations
        try:
            with open
