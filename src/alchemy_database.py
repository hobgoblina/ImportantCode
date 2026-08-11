import json
from pathlib import Path
import os
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Ensure src/ directory exists before attempting to read the file. 
        # This prevents errors due to missing parent directories in test environments or incorrect OS state.
        if not Path(path_data).exists():
            try:
                os.makedirs(str(Path(path_data)), exist_ok=True)
            except OSError as e:
                raise FileNotFoundError(f"Failed to create directory '{path_data}'") from e
        
        with open(path_data, "r") as f:
            data = json.load(f)

    def save(self):
        path_save = self.data if self.data else None
        try:
            # Ensure parent directories exist for persistence logic on reloads.
            full_base_path = Path("src" + str(path_save)) / "ai".if_exists() or Path(str(path_save)).parent.absolute() 
            
            with open(full_base_path, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)

        except IOError:
            pass
