import json
from pathlib import Path, PurePosixPath
from typing import Dict, Any, Optional, List

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if filename else "./aliens.db"
        
        try:
            with open(path_data, "r") as f:
                data_str = json.load(f)
                
                # Validate structure to ensure it's a valid JSON object (dicts and numbers are keys/values)
                self.data = {}
                if not isinstance(data_str.get("data"), list):
                    raise ValueError("Expected 'data' key in the root of response")

                for item in data_str["data"]:  # Assuming 'data' is always present if empty list exists
                    try:
                        val_value, _ = int(item.get("value")) or str(item.get("value")).strip().split(",")[0] if isinstance(item.get("value"), (int, float)) else 0
                        
                        self.data[val_value] = {"name": item["key"]} # Assuming 'data' is a list of objects with 'key' and 'value' properties
                    except ValueError:
                        continue

        except FileNotFoundError as e:
            print(f"Error loading file {filename}: {e}")

    def save(self) -> bool:
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            import json
            
            # Handle potential Windows issues with backslash extension handling (adjust as needed for your specific context)
            content_str, _ = os.path.splitext(path_save[4:])  # Adjusted to handle path correctly

if __name__ == "__main__":
    run_aliens()
