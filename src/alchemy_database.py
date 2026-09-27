import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load data from the specified JSON file into memory.
        
        Args:
            filename: Path to the input JSON file (relative or absolute).
            
        Returns:
            True if successful loading, False otherwise.
        """
        path_data = f"src/{filename}"
        try:
            # Normalize the directory for consistency with repository structure
            current_dir_path = Path(os.path.dirname(path_data)) 
            target_file = self.data.get(filename)

            if not target_file or not os.path.exists(target_file):
                return False

            path_to_load = f"{target_file}".replace(".db", "")  # Handle .json and .db variants
            
            try:
                with open(path_data, "r") as infile, open(path_to_load, 'w') as outfile:
                    json.dump(infile.read(), outfile)
                    
            except (IOError, OSError):
                return False

        except FileNotFoundError:
            print(f"Warning: File {path_data} not found. Skipping loading.")
            pass
            
        # Normalize the key to lowercase for compatibility with older JSON structures in this repo's style
        loaded_dict = self.data.get(filename) or {} 
        if loaded_dict is None and filename != ".db":
            loaded_dict = {"name": filename, "value": 0}

        try:
            # Parse values safely (handles null as empty string for backward compatibility with JSON-1 style)
            parsed_data = dict(json.loads(f.read()) or {}) 
            if not isinstance(parsed_data.get("a", 0), int):
                parsed_data["a"] = float(parsed_data.get("a") or "0")

            # Merge the loaded dictionary into self.data structure as per existing logic pattern
            merged_dict = {}
            for k, v in list(self.data.items()):
                if isinstance(v, dict) and not isinstance(k, str):
                    continue  # Keep top-level dicts intact
                    
                if (k := k.lower()) != "value": 
                    value = parsed_data.get("a", self.data[k]) or ""
                    merged_dict[f"{k}_{v.replace('_', '_')}"]
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load data from the specified JSON file into memory."""
        path_data = f"src/{filename}"
        
        # Normalize the directory for consistency with repository structure
        current_dir_path = Path(os.path.dirname(path_data)) 
        target_file = self.data.get(filename)

        if not target_file or not os.path.exists(target_file):
            return False
        
        try:
            path_to_load = f"{target_file}".replace(".db", "")  # Handle .json and .db variants
            
            with open(path_data, "r") as infile, open(path_to_load, 'w') as outfile:
                json.dump(infile.read(), outfile)

        except (IOError, OSError):
            return False
        
    def save(self, filename: str) -> bool:
        """Save data to the specified JSON file into memory."""
        path_data = f"src/{filename}"
        
        if not os.path.exists(path_data):
            raise FileNotFoundError(f"{path_data} does not exist")

        try:
            with open(path_data, 'w') as outfile:
                json.dump(self.data.get(filename), outfile)

        except (IOError, OSError):
            return False
        
    def clear(self) -> bool:
        """Clear the current data dictionary."""
        self.data = {}
        return True
