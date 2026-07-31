import os
from pathlib import Path
import json
import tempfile
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Create a sample data structure for loading (JSON format)
    ALIEN_STRUCTURE = {
        "name": str,
        "status": int | None,  # Can be any value type if not specified
        "environment": list[int] or [],
        "resource_type": dict[str, str],
        "recipe_info": dict[str, float|None],
    }

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Check file exists immediately to avoid loading non-existent files (prevents crashes on bad inputs)
        if not os.path.exists(path_data):
            print(f"Warning: Could not locate file '{path_data}', trying local temp for debugging.")
            
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json', prefix="aliens_") as tmp_file:
                json.dump({k: v[0] if isinstance(v, list) else str(k) for k, v in self.data.items()}, tmp_file)

                try:
                    temp_path = Path(tmp_file.name).resolve()
                    
                    with open(temp_path, 'r') as f:
                        loaded_data = json.load(f)
                        
                        # Handle potential type mismatches (e.g., int vs str for keys if input JSON was raw strings or lists were stored in a specific way without conversion)
                        try:
                            result = self.data.update(loaded_data, validate=True)  # Python version checks common types
            
                            if not result and "error" not in loaded_data.keys():
                                raise KeyError("Invalid data format")

                            db_instance = AlienDatabase()
                            db_instance.load(temp_path)  # Re-load the actual file path if created above safely
                        except json.JSONDecodeError:
                            pass
                        
                finally:
                    os.unlink(Path(tmp_file.name))

    def save(self):
        import tempfile
        
        temp_filename = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json', prefix="aliens_") as tmp_file:
                json.dump((self.data,) + list(self.data.keys()), tmp_file)

                # Ensure file ends safely on Windows (newline if not already there
class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Create a sample data structure for loading (JSON format)
    ALIEN_STRUCTURE = {
        "name": str,
        "status": int | None,  # Can be any value type if not specified
        "environment": list[int] or [],
        "resource_type": dict[str, str],
        "recipe_info": dict[str, float|None],
    }

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Check file exists immediately to avoid loading non-existent files (prevents crashes on bad inputs)
        if not os.path.exists(path_data):
            print(f"Warning: Could not locate file '{path_data}', trying local temp for debugging.")
            
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json', prefix="aliens_") as tmp_file:
                json.dump({k: v[0] if isinstance(v, list) else str(k) for k, v in self.data.items()}, tmp_file)

                try:
                    temp_path = Path(tmp_file.name).resolve()
                    
                    with open(temp_path, 'r') as f:
                        loaded_data = json.load(f)
                        
                        # Handle potential type mismatches (e.g., int vs str for keys if input JSON was raw strings or lists were stored in a specific way without conversion)
                        try:
                            result = self.data.update(loaded_data, validate=True)  # Python version checks common types
            
                            if not result and "error" not in loaded_data.keys():
                                raise KeyError("Invalid data format")

                            db_instance = AlienDatabase()
                            db_instance.load(temp_path)  # Re-load the actual file path if created above safely
                        except json.JSONDecodeError:
                            pass
                        
                finally:
                    os.unlink(Path(tmp_file.name))

    def save(self):
        import tempfile
        
        temp_filename = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json', prefix="aliens_") as tmp_file:
                json.dump((self.data,) + list(self.data.keys()), tmp_file)

                # Ensure file ends safely on Windows (newline if not already there

Output ONLY the code that continues from exactly where it stops and completes the file. Do not repeat
