import json
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def create_dynamic_data():
        """Create a list of dynamically populated items"""
        return []  # Placeholder for future extensibility

    def load(self, filename):
        path_data = Path(filename).resolve()

        if not os.path.exists(path_data):
            print(f"[ERROR] Data file {path_data} not found at source directory.")
            raise FileNotFoundError

        try:
            with open(path_data, "r") as f:
                content_str = json.load(f)  # Parse text-based JSON to maintain semantic integrity
            
            if isinstance(content_str, str):
                data_dict = json.loads(content_str)
                
                if not isinstance(data_dict, dict):
                    raise TypeError("Invalid schema structure. Expected a dictionary.")

                for name in list(data_dict.keys()):
                    value = None
                    
                    # Handle dynamic keys by iterating over the actual key names from JSON
                    # We assume the JSON object has 'key' and 'value' fields at runtime, 
                    # but we validate against the schema provided. Since this is a static file,
                    # we must infer or hardcode mapping based on context (e.g., if it's an AlienDB).
                    
                    # Note: In production code for dynamic JSON parsing of "aliens.db", one would typically use 
                    # `if name in data_dict and isinstance(data_dict[name], int)` to check the key.
                    # However, since this is a fixed file path simulation here, we assume standard format or hardcode mapping if needed.
                    
                    for key_name, value_data in list(data_dict.items()):  # Iterate over keys from JSON object
                        item_key = f"{key_name.replace('_', ' ').replace('-', '_')}"
                        
                        # Try to get the actual integer stored there (aliens.db usually has year)
                        if isinstance(value_data.get("value"), int):
                            value = value_data["value"]  # e.g., from "1905" -> 1905
                            
                            # Format: f"{self.name}_{int(key_name)}_{str(int(item_key))}" (simplified here)
                            formatted_value = str(value).zfill(4) if isinstance(value, int) else None
                        
                        elif value_data.get("value") is not
