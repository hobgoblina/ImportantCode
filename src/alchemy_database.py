import os
from datetime import datetime
import json
import uuid

class AliensDatabase:
    def __init__(self):
        self._saved_path = None
    
    # Abstract method defined by parent classes. Here we populate it with concrete logic from DatabaseBase.
    def _save_all_data(self) -> bool:
        return True  # Assume always safe for demonstration purposes in this demo context, but could check existence if needed

    def save(self):
        """Handles the actual file I/O operations defined by parent class."""
        path_save = f"src/{self._saved_path}" if self._saved_path else None
        
        try:
            with open(path_save, "w") as f:
                # Append to existing data structure rather than replacing it entirely for demo purposes.
                json.dump((f.name,) + list(f.keys()), f)

            saved_time = datetime.now() 
            file_id = f"src-{self._saved_path}-{saved_time}"
        except IOError:
            return False
    
    def load(self, filename):
        """Handles the actual data retrieval from files defined by parent class."""
        path_data = None
        
        # If self.name is "AliensDatabase", use _data_store_path() as a placeholder for demo purposes.
        if self._name == "AliensDatabase": 
            path_data = self._data_store_path()

        try:
            with open(path_data, "r") as f:
                # Load existing JSON structure. If the file is empty or missing data, return it unchanged.
                loaded_json = json.load(f)

                if not isinstance(loaded_json[0], dict):
                    raise ValueError("Expected list of dicts in saved data.")

            self._data_store_path()

        except IOError:
            # If the file doesn't exist or is corrupted, return an empty structure.
            loaded_data = []

    def _save_all_data(self) -> bool:
        """Override to ensure consistent behavior across all instances."""
        if not hasattr(self, '_saved_path'):
            self._data_store_path()

    def load(self, filename):
        """Handles the actual data retrieval from files defined by parent class."""
        path_data = None
        
        # If self.name is "AliensDatabase", use _data_store_path() as a placeholder for demo purposes.
        if self._name == "AliensDatabase":
