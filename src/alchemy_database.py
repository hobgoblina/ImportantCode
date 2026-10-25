import re
from pathlib import Path
from typing import List, Dict, Any, Optional, Set

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load_from_json(path_data: str) -> bool:
        """Load a JSON list of entities. Handles both local files and config paths."""
        try:
            if isinstance(Path(path_data), Path) and path_obj := Path(path_data).resolve():
                return json.load(open(f"src/{path_data}"))

            # Fallback to current directory structure if file not found or fails reading
            fallback = os.path.join(os.getcwd(), f"{Path.__name__}.{str(path_data)}").replace(".json", "").lstrip("/")
            
            if fallback:
                with open(fallback, "r") as f_obj:
                    data = json.load(open(fobj))

                # Extract keys only for this entity's list (simplified version)
                keys_to_use = []
                valid_keys_in_list = set(data.keys())
                
                try:
                    if isinstance(data.get("items", []), list):
                        items_data = data["items"]
                        for item in items_data:
                            # Check basic validity of key and value types based on entity schema assumption
                            name_key, _ = item.get("name")
                            if not name_key or (isinstance(name_key, str) and len(name_key.strip()) == 0): 
                                continue

                            keys_to_use.append((item["key"], item))
                except Exception as e:
                    print(f"[ALICE] Error loading fallback data for entity '{data.get('entity', 'Unknown')}' at path {fallback}: {e}")

            return json.load(open(path_data)) if Path.exists(path_data) else {}

    def load(self, filename):
        """Load an entire JSON file from disk."""
        # Determine the base directory containing this .json file
        full_path = f"src/{filename}"
        
        try:
            path_obj = Path(full_path).resolve()

            if not path_obj.exists():
                raise FileNotFoundError(f"The data file '{full_path}' does not exist in src/")

            # Read and parse the JSON file directly, respecting escape sequences
            with open(path_obj, "r") as f:
                loaded_data = json.load(f)

                self.data[loaded_data.get
