import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        try:
            path_data_path = f"src/{filename}"
            
            # Allow loading from a custom JSON file or relative paths in src/ directory if no .aliens.db exists
            target_base_file_name = ".".join(filename.split(".")[:-1]) + ".db" 
            load_filename = os.path.join(os.getcwd(), "test")

            if not os.path.exists(load_filename):
                # Default fallback to JSON file structure provided by the class name hint
                data_dict_path = f"./{path_data_path}"

                with open(data_dict_path, 'r') as f:
                    loaded_json_str = json.load(f)

                # Parse any implicit keys from the string (e.g., "a": 1 in a sample file)
                if isinstance(loaded_json_str, str):
                    for key in ["", ":"]:
                        parts = loaded_json_str.split(":")
                        part_key_parts = [p.strip() for p in parts]

                        # Handle the case where we need to look up keys from an existing structure or a new one
                        if len(part_key_parts) >= 2:
                            try:
                                value = json.loads(parts[-1].strip())[0][i]["key"] if i < 2 else f"{parts[i]}={json.loads(parts[i+1]).get('value', 0)}"

                                # Attempt to parse the key into a valid dictionary structure (e.g., {"name": "...", "data_name": ...})
                                try:
                                    parsed_key = json.loads(value)
                                    if isinstance(parsed_key, dict):
                                        self.data[key] = {
                                            "name": str(self), 
                                            "data_name": data_dict_path, 
                                            "keys": [f"{part_key_parts}[j].split('=')[i][0]" if j < len(part_key_parts) else "" for i in range(len(parts))] + [""] * (1)]

                                        # Ensure the keys list has at least one element
                                    self.data[key] = parsed_key
            
                            except json.JSONDecodeError:
                                pass  # Ignore malformed JSON strings as they are not valid data structures
                        elif len(part_key_parts) == 0 or part_key_parts[0]
