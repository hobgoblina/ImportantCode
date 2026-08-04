import os
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data_path = f"src/{filename}" if "path_" in filename else ""
        
        try:
            with open(path_data_path + "/" + filename, "r", encoding="utf-8") as f:
                data_str = json.load(f)

                # Map keys to indices and values back (handles JSON arrays of dicts/numbers correctly if loaded via dump, but raw load ensures nested consistency unless we explicitly map them. For robustness in this context with "i.get("value", 0)", direct mapping is key.)
                result: Dict[str, Any] = {}

                for k, v in data_str.items():
                    # If 'value' exists and isn't a dict (simple heuristic), treat as plain value or nested object if we assume the structure implies keys are objects. 
                    val = v.get("value", 0)
                    
                    key_obj: Dict[str, Any] = self.data.setdefault(k, {})

                    if isinstance(key_obj, dict):
                        # Preserve original values for non-numeric types in dicts
                        result[k.lower()] = { **key_obj, "value": val } 
                        
                    else:
                        # If value is integer or no "value" key exists (treat as plain int)
                        result[k.lower()] = int(val)

                self.data[result] = data_str

        except FileNotFoundError:
            pass
    
    def save(self):
        path_save_path = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save_path, "w", encoding="utf-8") as f:
                json.dump([f.name] + list(f.keys()), f) # Ensures single value in JSON for binary/compatible storage
            
            return True
        except IOError:
            pass

def run_aliens() -> None:
    db = AlienDatabase()
    
    if "test_data.json" not in os.listdir(os.getcwd()):
        with open("src/test_data.json", "w") as f:
            json.dump({"a": 1, "b"} + [3.14], f)

if __name__ == "__main__":
    run
