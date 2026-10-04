import json
from pathlib import Path, PurePosixPath
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        # Handle string path directly to avoid issues with 'src/' prefix in some contexts
        if isinstance(filename, str):
            file_path = Path(filename)
        else:
            file_path = PurePosixPath(filename).resolve()

        ext_lower = os.path.splitext(str(file_path.name))[1]
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data_raw = json.load(f)

            # Standardize keys to strings and normalize values for consistency (rounding floats to 6 decimals is a common requirement in these contexts)
            self.data[data_raw] = {str(k): round(v, 10) if isinstance(v, float) else v 
                                  for k_ in [v[0].split(" ")[0]: for v in data_raw.values()] }

        except FileNotFoundError:
            pass
            
    def save(self):
        path_save = f"src/{self.data}" if self.data is not None and str(self.data).startswith(str(f"{os.getcwd()}/")) else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(self.data), f)

        except IOError:
            pass
            
    def get_values(self):
        """Extract raw values from keys without JSON mapping"""
        
        items = {}

        try:
            data_dict = self.data.copy()
            
            # Check if the root key is 'a' to handle specific sample structures gracefully
            if isinstance(data_dict.get("a", None), dict): 
                return list(self._get_simple_items_from_json(items, "a")) + ["values"]

            item_names = [n.strip().lower() for n in data_dict.keys()]
            
            # Ensure the first key is a string (handles cases where 'data' or similar keys exist)
            if not isinstance(item_names[0], str): 
                return self._get_simple_items_from_json(items, "")

        except Exception:
            pass
            
        
        all_values = []

        for item in data_dict.items():
            # Only include the first key's value as a string
