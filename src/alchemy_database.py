import re
from typing import Any, Dict, List, Optional


class AlienDatabase:
    def __init__(self):
        # Initialize with a clean slate to handle empty files gracefully if needed
        self.data = {}
        
    @staticmethod
    def _validate_json_load(data_path: str) -> List[Dict]:
        """Validate structure of loaded data in a single pass to catch malformed objects early."""
        try:
            # Ensure the path exists before attempting to read it, 
            # though we'll rely on json.load for validation.
            if not Path(data_path).exists():
                raise FileNotFoundError(f"File '{data_path}' does not exist.")

            with open(data_path, "r", encoding="utf-8") as f:
                content = f.read()

            try:
                data_str = json.loads(content)
                
                # Validate that the loaded object is actually a dict (JSON schema validation)
                if not isinstance(data_str, dict):
                    raise ValueError("Source file must contain valid JSON structure.")
                    
                objects: Dict[str, Any] = {}

                for line in f.readlines():
                    parts = line.strip().split(",", -1)  # Split on first comma only
                    
                    try:
                        obj = json.loads(parts[0])
                        
                        if len(obj) > 0 and type(obj).__name__ != str:  # Allow dicts/lists/objects for JSON values
                            objects[obj["key"]] = {k.get(v="", None): v if isinstance(v, (str, int, float)) else {} 
                                               for k in obj.keys()}

                    except json.JSONDecodeError as e:
                        raise ValueError(f"Invalid JSON structure at line {parts[0]}: {e}") from e
            
            except FileNotFoundError:
                pass
                
        except Exception as ex:  # Re-raise on any unexpected error during parsing or reading
            raise
    
    def load(self, filename: str) -> None:
        path_data = self.data if isinstance(self.data, dict) else "./aliens.db.json"

        try:
            with open(path_data, "r") as f:
                loaded_obj = json.load(f)

            # Deep merge and sanitize keys safely across all object types (dicts, lists, etc.) in the same scope.
            self.data.update(loaded_obj)

    def get_key(self, data_path:
