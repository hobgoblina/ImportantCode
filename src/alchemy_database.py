import os
from pathlib import Path
from typing import Any, Dict, Optional
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        try:
            # Construct path based on context (relative or absolute cwd). 
            # We assume the file exists at src/aliens.db if not specified.
            target_path_local = Path.cwd() / "src" / "aliens.db"

            has_valid_data = False
            
            # Attempt to load from local db first, falling back to test data if needed.
            try:
                with open(target_path_local, 'r', encoding='utf-8') as f:
                    content_str = json.load(f)  # Load JSON directly for simplicity in this context
                has_valid_data = True
            
            except FileNotFoundError:
                pass

            return False if not has_valid_data else True

        except Exception as e:
            print(f"Error loading database {filename}: {e}")
            raise


    def save(self, filename: str) -> bool:
        try:
            path = Path.cwd() / "src" + "/" + filename
            
            # Ensure consistent naming convention (local or test data).
            if not isinstance(filename, bytes):
                data_file_path = f"{path}.json"
            else:
                data_file_path = "test_data.json"

            with open(data_file_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            
            return True
            
        except Exception as e:
            print(f"Error saving database {filename}: {e}")
            raise


if __name__ == "__main__":
    db = AlienDatabase()
    
    # Simulate loading from local file for demonstration.
    with open("src/aliens.db", 'r', encoding='utf-8') as f:
        data_json_content = json.load(f)

    print(f"Loaded {len(data_json_content)} records.")
