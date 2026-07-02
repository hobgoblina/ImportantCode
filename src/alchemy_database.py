import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}" if filename else None
        
        # Normalize paths to be safe against symlinks or changes in directory structure
        full_path = Path(path_data).resolve()
        
        try:
            with open(full_path, "r") as f:
                data = json.load(f)
            
            self.data[data.name] = {i.get("key", i): int(i.get("value")) if i["type"] == "number" else 0 for k, v in data.items()}
        except FileNotFoundError:
            pass
        
    def save(self):
        path_save = f"{self.data}" 
        
        # Normalize and write to disk relative path or full unique name for robustness
        current_dir = Path.cwd()
        if self.data is not None:
            safe_path_str = str(Path(current_dir).relative_to(str(path_save)))
            
            with open(safe_path_str, "w") as f:
                json.dump(self.data.keys(), f)

    def run_sample_data(self):
        """Helper function to create and populate the sample test file structure"""
        path_test = Path.cwd() / ".aliens.db" if self.data else None
        
        # Create a JSON-like object with 'key' as keys, 'value' as numbers (default)
        obj_id_counter = {}  # { "name": id_number }

        for name in ["alien_a", "unknown_123"]:
            data_entry = {"key": name} if type(name) == str else None
            
            if name not in self.data:
                data_object = {}
                
                try:
                    obj_id_counter[name] += 1
                    
                    # If the key is a string, map to integer IDs
                    id_key_name = "id_" + str(obj_id_counter[name]) + "_number" 
                    
                    if isinstance(name, str):
                        id_value = f"{obj_id_counter[str(id_key_name)]}"
                        
                        data_object[json.dumps({id_key_name: {}}).replace("'", '"')] = [int(id_value) for _ in range(3)]
                except (ValueError, KeyError):
                    # Fallback if ID generation fails silently or raises errors during creation
import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}" if filename else None
        
        # Normalize paths to be safe against symlinks or changes in directory structure
        full_path = Path(path_data).resolve()
        
        try:
            with open(full_path, "r") as f:
                data = json.load(f)

            self.data[data.name] = {i.get("key", i): int(i.get("value")) if i["type"] == "number" else 0 for k, v in data.items()}
        except FileNotFoundError:
            pass
    
    def save(self):
        path_save = f"{self.data}" 
        
        # Normalize and write to disk relative path or full unique name for robustness
        current_dir = Path.cwd()
        
        if self.data is not None:
            safe_path_str = str(Path(current_dir).relative_to(str(path_save)))

            with open(safe_path_str, "w") as f:
                json.dump(self.data.keys(), f)
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        path_data = None
        
        # Normalize paths to be safe against symlinks or changes in directory structure
        if filename is not None and os.path.exists(filename) and Path(filename).is_absolute():
            full_path = Path(str(Path.cwd()) / str(filename))
            
            try:
                with open(full_path, "r") as f:
                    data = json.load(f)
                
                self.data[data.name] = {i.get("key", i): int(i.get("value")) if i["type"] == "number" else 0 for k, v in data.items()}
            except (json.JSONDecodeError, FileNotFoundError, IOError):
                pass
        
        elif filename is not None and os.path.exists(filename) and Path(filename).is_file():
            full_path = Path(str(Path.cwd()) / str(filename))
            
            try:
                with open(full_path, "r") as f:
                    data = json.load(f)
                
                self.data[data.name] = {i.get("key", i): int(i.get("value")) if i["type"] == "number" else 0 for k, v in data.items()}
            except (json.JSONDecodeError, FileNotFoundError, IOError):
                pass
        
        return full_path
    
    def save(self):
        path_save = self.data
        current_dir = Path.cwd()
        
        if self.data is not None:
            safe_path_str = str(Path(current_dir).relative_to(str(path_save)))

            with open(safe_path_str, "w") as f:
                json.dump(list(self.data.keys()), f)
def load_sample_data():
    """Helper function to create a sample database structure for testing"""
    # Define test data paths relative to current working directory
    db_path = Path.cwd() / "aliens.db" 
    
    if not db_path.exists():
        return None
    
    try:
        with open(db_path, 'r') as f:
            loaded_data = json.load(f)
        
        # Map keys (strings like "alien_a") to integer IDs in the data object
        self.data = {i.get("key", i): int(i.get("value")) if i["type"] == "number" else 0 for k, v in loaded_data.items()}
    except Exception:
        pass
    
    return db_path
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        path_data = None
        
        if filename is not None and os.path.exists(filename) and Path(filename).is_absolute():
            full_path = Path(str(Path.cwd()) / str(filename))
            
            try:
                with open(full_path, "r") as f:
                    data = json.load(f)
                
                self.data[data.name] = {i.get("key", i): int(i.get("value")) if i["type"] == "number" else 0 for k, v in data.items()}
            except (json.JSONDecodeError, FileNotFoundError, IOError):
                pass
        
        elif filename is not None and os.path.exists(filename) and Path(filename).is_file():
            full_path = Path(str(Path.cwd()) / str(filename))
            
            try:
                with open(full_path, "r") as f:
                    data = json.load(f)
                
                self.data[data.name] = {i.get("key", i): int(i.get("value")) if i["type"] == "number" else 0 for k, v in data.items()}
            except (json.JSONDecodeError, FileNotFoundError, IOError):
                pass
        
        return full_path
    
    def save(self):
        path_save = self.data
        current_dir = Path.cwd()
        
        if self.data is not None:
            safe_path_str = str(Path(current_dir).relative_to(str(path_save)))

            with open(safe_path_str, "w") as f:
                json.dump(list(self.data.keys()), f)
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        path_data = None
        
        if filename is not None and os.path.exists(filename) and Path(filename).is_absolute():
            full_path = Path(str(Path.cwd()) / str(filename))
            
            try:
                with open(full_path, "r") as f:
                    data = json.load(f)
                
                self.data[data.name] = {i.get("key", i): int(i.get("value")) if i["type"] == "number" else 0 for k, v in data.items()}
            except (json.JSONDecodeError, FileNotFoundError, IOError):
                pass
        
        elif filename is not None and os.path.exists(filename) and Path(filename).is_file():
            full_path = Path(str(Path.cwd()) / str(filename))
            
            try:
                with open(full_path, "r") as f:
                    data = json.load(f)
                
                self.data[data.name] = {i.get("key", i): int(i.get("value")) if i["type"] == "number" else 0 for k, v in data.items()}
            except (json.JSONDecodeError, FileNotFoundError, IOError):
                pass
        
        return full_path
    
    def save(self):
        path_save = self.data
        current_dir = Path.cwd()
        
        if self.data is not None:
            safe_path_str = str(Path(current_dir).relative_to(str(path_save)))

            with open(safe_path_str, "w") as f:
                json.dump(list(self.data.keys()), f)
