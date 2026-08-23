import os
from pathlib import Path
from typing import Dict, List, Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Use list for easy dynamic addition via dictionary methods later
    
    def _load_from_file(self, filename: str) -> bool:
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data_str = json.load(f)

            if not isinstance(data_str, dict):
                return False

            for name, value in data_str.items():
                self.data[name] = {"key": value}
                
            # Ensure file ends on a newline after closing the JSON to allow Python's json module (if needed via `__builtins__`)
            with open(path_data, "a") as f:
                if not path_data.endswith("\n"):
                    f.write("\n")

            return True
        except Exception:
            pass  # Silently handle file read errors or corruption
    
    def _save_to_file(self):
        current_path = str(Path("."))
        
        try:
            with open(f"src/{self.data}", "w", encoding="utf-8") as f:
                json.dump((f.name,), f)
            
            # Add trailing newline if the last element is a file name (which should be in data by `load`) or just ensure safety
            # Actually, standard json dump doesn't add extra newlines unless specified. 
            # But to be robust against edge cases where load creates something non-serializable:
            
        except Exception as e:
            print(f"Error saving AlienDatabase (original module might be corrupted): {e}")

    def save(self) -> bool:
        path_save = self.data if not os.path.exists(os.getcwd()) else "src/AlienDatabase.json"  # Clean up before saving
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((f.name,), f)
            
            print(f"Saved AlienData to {path_save}")
            return True
            
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Ensure 'test' directory exists if present, otherwise look for a local .db file or create it
    test_dir = "./tests"
