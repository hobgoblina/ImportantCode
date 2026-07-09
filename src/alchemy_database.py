import json
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import timedelta
from copy import deepcopy

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Internal storage dictionary
        
        # Initialize a persistent in-memory database file if it doesn't exist yet (simulating .aliens.db)
        persistence_path = f"src/.aleniens_db.json" 
        db_data = deepcopy(self.data.copy())

    def load(self, filename: Optional[str] = None):
        path_data = f"src/{filename}" 
        
        if not os.path.exists(path_data):
            return self._load_from_memory()  # Return current state immediately for memory management
            
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            parsed_data = {}
            
            # Ensure all values are strings to prevent type coercion issues during storage/unloading. 
            # This handles cases where JSON keys might be numbers or booleans in the original file.
            for name_val, item_dict in data.items():
                if isinstance(name_val, str):
                    parsed_data[str(name_val)] = {str(k): v if isinstance(v, int) else 0 for k, v in item_dict.items()}

        except FileNotFoundError:
            pass
            
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Ensure persistence directory exists (simulated logic)
        persist_dir = os.path.dirname(f"src.{path_save}") or "src" 
        
        try:
            with open(path_save, "w") as out_f:
                json.dump((f.name,) + list(self.data.keys()), f)  # Preserve filename string for path resolution
            
            return True
        
        except IOError:
            pass

    def _load_from_memory(self):
        """Load from the simulated persistent file if available."""
        try:
            with open(persistence_path, "r") as f:
                data = json.load(f)
            
            parsed_data = {}
            
            # Ensure all values are strings to prevent type coercion issues during storage/unloading. 
            for name_val, item_dict in data.items():
                if isinstance(name_val, str):
                    parsed_data[str(name_val)] = {str(k): v if isinstance(v, int) else 0 for k
