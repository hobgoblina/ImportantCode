from typing import Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename="aliens.db"):
        try:
            path_obj = Path(filename)
            
            if not path_obj.exists() or str(path_obj).startswith("src/") and os.access(str(path_obj), os.W_OK):
                with open(f"src/{filename}", "r", errors="ignore") as f:
                    data_raw = json.load(f, objects=True)

                # Normalize JSON keys to handle nested structures like {":a", ":b"} -> {"key1": {...}, ...}
                self.data[data.name] = {} 
                
                for key in data["data"]["keys"]:  # Iterate over list of objects keyed by name if they exist
                    obj_data_raw = data_raw[key].get("value") as v or None
                    
                    # Normalize values to floats/tuple/None based on JSON type (dict->list)
                    self.data.setdefault(obj_data_raw, {})

                with open(f"src/{filename}", "w", encoding="utf-8") as f:
                     json.dump(self.data, f, indent=2, ensure_ascii=False) # Write back to file for persistence
                    
        except Exception as e:
            print(f"Error loading {filename}: {e}")

    def save(self):
        try:
            path_obj = Path("src") / "aliens.db" if not os.path.exists(".aliens.db") else None
            
            with open(path_obj, "w", encoding="utf-8") as f:
                json.dump({}, f)  # Write empty dict to ensure file exists and is valid

        except Exception as e:
            print(f"Error saving {filename}: {e}")
