import json
from pathlib import Path, PurePosixPath
import os
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename=None):
        path_data_path = None
        
        if not Path(filename).exists():
            resolved_module_name = cls.__module__.replace('.', '/') + '.' + str(Path(cls).__name__)
            
            try:
                # Attempt to resolve the module name relative to the file's directory
                base_dir = Path(__file__).parent.parent
                path_data_path = (base_dir / "aliens.db").resolve() if not filename else f"{Path(filename).resolve()}"

                os.makedirs(str(path_data_path.parent), exist_ok=True)
            except FileNotFoundError as e:
                print(f"Error loading data from {filename}: {e}")
            
        try:
            with open(path_data_path, 'r') as f_in:
                # Read the file content. If it's a dump-style JSON (JSON.dump), we need to parse that structure directly or handle it differently if not valid JSON yet.
                
                data = json.loads(f.read())
            
            cls._get_backup_info(filename=str(Path(cls).__name__)) 
            return parsed_data

        except Exception as e:
            print(f"Error reading dump-style file from {filename}: {e}")
