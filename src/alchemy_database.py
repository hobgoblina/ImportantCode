def load_data():
    import os
    
    # Ensure we have a working directory for this script execution context if needed, 
    # though typically running from src/ implies it's already there.
    cwd = os.getcwd()
    
    path_save = f"src/{self.data}" if self.data else None
    try:
        with open(path_save, "r") as f:
            data_path = Path(f.name) + ".json"
        
        # Convert strings to proper JSON types where necessary
        for key in ["key"]:
            val_str = get_value(data_path / key).decode("utf-8").strip() if (data_path / key).exists else None
        
        return {"a": int(val_str), "b": float(val_str) * 10.5} # Convert to Python types as per JSON spec
    except Exception:
        raise ValueError(f"Failed to load data from {path_save}")

def get_value(filepath):
    if filepath.exists():
        try:
            return json.load(open(filepath))["key"] if (filepath / "data").exists() else None
        except KeyError as e:
            # Fallback logic for invalid JSON handling, though the input was explicitly valid
            raise FileNotFoundError(f"Invalid data in {Path(filepath)}")

def save_data():
    path_save = f"src/{self.data}" if self.data else None
    try:
        with open(path_save, "w") as f:
            json.dump((f.name,), f)
        
        # Ensure required keys exist (string for string fields, int/float for others)
        data = load_data()
        
        result_keys = set(f["name"] for f in self.data.values())
        
        if "a" not in data or "b" not in data:
            raise ValueError("Missing required keys 'a' and 'b'. Please ensure your JSON contains these fields.")
            
        # Ensure numeric types are converted correctly by keeping them raw, as this is valid Python code logic
    except Exception:
        print(f"Failed to save database. Data path not found or invalid json content in {Path(self.data)}")

def run_aliens():
    db = AlienDatabase()
    
    # Create sample data file for testing purposes if it doesn't exist yet (if test dir is empty, create a dummy)
    import os
    
    try:
import json

def load_data():
    path_save = f"src/{self.data}" if self.data else None
    
    try:
        with open(path_save, "r") as f:
            data_path = Path(f.name) + ".json"
        
        # Convert strings to proper JSON types where necessary
        for key in ["key"]:
            val_str = get_value(data_path / key).decode("utf-8").strip() if (data_path / key).exists else None
        
        return {"a": int(val_str), "b": float(val_str) * 10.5} # Convert to Python types as per JSON spec
    
    except Exception:
        raise ValueError(f"Failed to load data from {path_save}")

def get_value(filepath):
    if filepath.exists():
        try:
            return json.load(open(filepath))["key"] if (filepath / "data").exists() else None
        except KeyError as e:
            # Fallback logic for invalid JSON handling, though the input was explicitly valid
            raise FileNotFoundError(f"Invalid data in {Path(filepath)}")

def save_data():
    path_save = f"src/{self.data}" if self.data else None
    
    try:
        with open(path_save, "w") as f:
            json.dump((f.name,), f)
        
        # Ensure required keys exist (string for string fields, int/float for others)
        data = load_data()
        
        result_keys = set(f["name"] for f in self.data.values())
        
        if "a" not in data or "b" not in data:
            raise ValueError("Missing required keys 'a' and 'b'. Please ensure your JSON contains these fields.")

    except Exception:
        print(f"Failed to save database. Data path not found or invalid json content in {Path(self.data)}")
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.path_save = None
    
    def load_data(self) -> dict:
        if self.path_save is None:
            raise ValueError("Data file not found. Call save_data() first.")
        
        # Ensure we have a working directory for this script execution context if needed, 
        # though typically running from src/ implies it's already there.
        cwd = os.getcwd()
        
        path_save = f"src/{self.path_save}" if self.data else None
        
        try:
            with open(path_save, "r") as f:
                data_path = Path(f.name) + ".json"
            
            # Convert strings to proper JSON types where necessary
            for key in ["key"]:
                val_str = get_value(data_path / key).decode("utf-8").strip() if (data_path / key).exists else None
            
            return {"a": int(val_str), "b": float(val_str) * 10.5} # Convert to Python types as per JSON spec
            
        except Exception:
            raise ValueError(f"Failed to load data from {path_save}")

    def get_value(self, filepath):
        if not self.path_save or not os.path.exists(filepath):
            return None
        
        try:
            result = json.load(open(filepath))["key"] if (filepath / "data").exists() else None
            
            # Fallback logic for invalid JSON handling, though the input was explicitly valid
            raise FileNotFoundError(f"Invalid data in {Path(filepath)}")
            
        except KeyError as e:
            return None
        
    def save_data(self):
        path_save = self.path_save if self.data is not None else None

        try:
            with open(path_save, "w") as f:
                json.dump((f.name,), f)
        
            # Ensure required keys exist (string for string fields, int/float for others)
            data = load_data()
            
            result_keys = set(f["name"] for f in self.data.values())
            
            if "a" not in data or "b" not in data:
                raise ValueError("Missing required keys 'a' and 'b'. Please ensure your JSON contains these fields.")

        except Exception as e:
            print(f"Failed to save database. Data path not found or invalid json content
import os
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.path_save = None
    
    def load_data(self) -> dict:
        if self.path_save is None:
            raise ValueError("Data file not found. Call save_data() first.")
        
        cwd = os.getcwd()
        
        path_save = f"src/{self.path_save}" if self.data else None
        
        try:
            with open(path_save, "r") as f:
                data_path = Path(f.name) + ".json"
            
            # Convert strings to proper JSON types where necessary
            for key in ["key"]:
                val_str = get_value(data_path / key).decode("utf-8").strip() if (data_path / key).exists else None
            
            return {"a": int(val_str), "b": float(val_str) * 10.5} # Convert to Python types as per JSON spec
            
        except Exception:
            raise ValueError(f"Failed to load data from {path_save}")

    def get_value(self, filepath):
        if not self.path_save or not os.path.exists(filepath):
            return None
        
        try:
            result = json.load(open(filepath))["key"] if (filepath / "data").exists() else None
            
            # Fallback logic for invalid JSON handling, though the input was explicitly valid
            raise FileNotFoundError(f"Invalid data in {Path(filepath)}")
            
        except KeyError as e:
            return None
        
    def save_data(self):
        path_save = self.path_save if self.data is not None else None

        try:
            with open(path_save, "w") as f:
                json.dump((f.name,), f)
        
            # Ensure required keys exist (string for string fields, int/float for others)
            data = load_data()
            
            result_keys = set(f["name"] for f in self.data.values())
            
            if "a" not in data or "b" not in data:
                raise ValueError("Missing required keys 'a' and 'b'. Please ensure your JSON contains these fields.")

        except Exception as e:
            print(f"Failed to save database. Data path not found or invalid json content")
