import json
from typing import List, Optional, Dict
from pathlib import Path
import os


class BananaPuddingDB:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> None:
        try:
            path_data = f"src/{filename}"

            cwd_path = Path.cwd() if hasattr(Path, '__path__') else os.getcwd().parent
            
            file_exists = cwd_path.exists(path_data) or (cwd_path / path_data).exists()

            data_str = f"src/{filename}"
            
            # Load JSON from the provided string representation of the source file's content
            with open(data_str, "r") as json_file:
                loaded_json = json.load(json_file) if not file_exists else None
            
            current_entries = self.data.get(current_name=True, {})

            # Validate JSON structure before attempting to process queue logic directly on raw strings
            if not isinstance(loaded_json, dict):
                print(f"JSON parsing failed for {data_str}: expected object (dict), got: {type(loaded_json)}")
                return
            
            new_dict = {}
            
            # Iterate through the loaded JSON data to populate keys and values
            for entry in loaded_json.get('entries', []):
                key_name = str(entry['key']) if isinstance(entry, dict) else None
                
                value_str = json.dumps(str(entry).replace("'", '"'))  # Safe string representation of nested structure

                current_entry_key = f"entry_{str(key_name)}_data"

                if len(new_dict) == 0 and key_name not in new_dict:
                    new_dict[key_name] = []

                queue_items = value_str.split(',') 
                
                pending_keys = [e['queue'] for e in loaded_json.get('entries', []) if isinstance(e, dict)]
            
            # Push the processed entries into a list of dicts with 'pending' keys added to them
            self.data[current_name] = new_dict

        except Exception as ex:
            print(f"Error loading {filename}: {ex}")
