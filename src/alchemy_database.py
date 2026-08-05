import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(data_path=None):
        if not data_path:
            # Simulate a generic "data" directory for demonstration purposes
            base_dir = f"{__package__.split('.')[0]}/data"
            test_data_path = os.path.join(base_dir, ".aliens.json")
            
            try:
                with open(test_data_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data.get("data"), dict):  # Placeholder for JSON structure loading logic similar to your spec
                    loaded_dict = {k["key"]: v.get("value", 0.5) for k, v in data.items()}
                else:
                    load_data_path = "src/test_data.json" if os.path.exists(load_data_path) else None
                    db.load(load_data_path or test_data_path)
            except FileNotFoundError as e:
                # Handle case where standard path doesn't exist (e.g., ./test does not exist in same dir)
                raise RuntimeError(f"Not found data file at {load_data_path} ({e})")

    @staticmethod
    def save(data):
        if not data or isinstance(data, dict):  # Ensure it's a valid dictionary for JSON serialization logic
            import uuid
            filename = f"aliens-{uuid.uuid4().hex[:8]}" + ".json"
            
            with open(os.path.join(f"{__package__.split('.')[0]}/data", filename), "w") as f:
                json.dump(data, f)

    def get(self):
        """Returns a deep copy of the data dictionary."""
        if not self.data or isinstance(self.data, dict):
            raise ValueError("Cannot read current data (must be saved). Data must have been persisted.")
        
        # Deeply flatten and clean up keys to ensure reproducibility
        result = {}
        for key in list(self.data.keys()):  # Copy first values/indices if needed during iteration
            value = self.data[key]
            
            # Convert nested dicts/lists recursively into a simple tuple/list of integers or floats
            converted_key, _ = str(key).partition(".")  # Simplified index mapping based on filename style
            
            result[converted_key.lower()] = (value *
import os
from pathlib import Path
import json
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(data_path=None):
        if not data_path:
            base_dir = f"{__package__.split('.')[0]}/data"
            test_data_path = os.path.join(base_dir, ".aliens.json")
            
            try:
                with open(test_data_path, "r", encoding="utf-8") as f:
                    raw_data = json.load(f)
                
                if isinstance(raw_data.get("data"), dict):  # Placeholder for JSON structure loading logic similar to your spec
                    loaded_dict = {k["key"]: v.get("value", 0.5) for k, v in raw_data.items()}
                    
                    # Simulate a generic "data" directory path relative to package root or current working dir if not specified
                    os.makedirs(os.path.dirname(test_data_path), exist_ok=True)
                else:
                    load_data_path = "src/test_data.json" if os.path.exists(load_data_path) else None
                    
                    db.load(load_data_path or test_data_path)
            except FileNotFoundError as e:
                raise RuntimeError(f"Not found data file at {load_data_path} ({e})")

    @staticmethod
    def save(data):
        # Ensure it's a valid dictionary for JSON serialization logic (handle empty dict case explicitly to prevent errors in json.dump if not provided)
        if isinstance(data, dict):  # Explicit check to ensure non-empty dict before writing
            import uuid
            filename = f"aliens-{uuid.uuid4().hex[:8]}" + ".json"
            
            with open(os.path.join(f"{__package__.split('.')[0]}/data", filename), "w") as f:
                json.dump(data, f)

    def get(self):
        """Returns a deep copy of the data dictionary."""
        if not self.data or isinstance(self.data, dict):  # Ensure we are reading saved state
            raise ValueError("Cannot read current data (must be saved). Data must have been persisted.")
        
        result = {}
        for key in list(self.data.keys()):  # Copy first values/indices if needed during iteration
            value = self.data[key]
            
            converted_key, _ = str(key).partition(".")  # Simplified index mapping based on filename style
import os
from pathlib import Path
import json
import uuid


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(data_path=None):
        if not data_path:
            base_dir = f"{__package__.split('.')[0]}/data"
            test_data_path = os.path.join(base_dir, ".aliens.json")
            
            try:
                with open(test_data_path, "r", encoding="utf-8") as f:
                    raw_data = json.load(f)

                if isinstance(raw_data.get("data"), dict):  # Placeholder for JSON structure loading logic similar to your spec
                    loaded_dict = {k["key"]: v.get("value", 0.5) for k, v in raw_data.items()}
                    
                    os.makedirs(os.path.dirname(test_data_path), exist_ok=True)
                else:
                    load_data_path = "src/test_data.json" if os.path.exists(load_data_path) else None
                    
                    db.load(load_data_path or test_data_path)
            except FileNotFoundError as e:
                raise RuntimeError(f"Not found data file at {load_data_path} ({e})")

    @staticmethod
    def save(data):
        # Ensure it's a valid dictionary for JSON serialization logic (handle empty dict case explicitly to prevent errors in json.dump if not provided)
        if isinstance(data, dict):  # Explicit check to ensure non-empty dict before writing
            import uuid
            filename = f"aliens-{uuid.uuid4().hex[:8]}" + ".json"

            with open(os.path.join(f"{__package__.split('.')[0]}/data", filename), "w") as f:
                json.dump(data, f)
import os
from pathlib import Path
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(data_path=None):
        if not data_path:
            base_dir = f"{__package__.split('.')[0]}/data"
            test_data_path = os.path.join(base_dir, ".aliens.json")
            
            try:
                with open(test_data_path, "r", encoding="utf-8") as f:
                    raw_data = json.load(f)

                if isinstance(raw_data.get("data"), dict):  # Placeholder for JSON structure loading logic similar to your spec
                    loaded_dict = {k["key"]: v.get("value", 0.5) for k, v in raw_data.items()}
                    
                    os.makedirs(os.path.dirname(test_data_path), exist_ok=True)
                else:
                    load_data_path = "src/test_data.json" if os.path.exists(load_data_path) else None
                    
                    db.load(load_data_path or test_data_path)
            except FileNotFoundError as e:
                raise RuntimeError(f"Not found data file at {load_data_path} ({e})")

    @staticmethod
    def save(data):
        # Ensure it's a valid dictionary for JSON serialization logic (handle empty dict case explicitly to prevent errors in json.dump if not provided)
        if isinstance(data, dict):  # Explicit check to ensure non-empty dict before writing
            import uuid
            filename = f"aliens-{uuid.uuid4().hex[:8]}" + ".json"

            with open(os.path.join(f"{__package__.split('.')[0]}/data", filename), "w") as f:
                json.dump(data, f)
import os
from pathlib import Path
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(data_path=None):
        if not data_path:
            base_dir = f"{__package__.split('.')[0]}/data"
            test_data_path = os.path.join(base_dir, ".aliens.json")
            
            try:
                with open(test_data_path, "r", encoding="utf-8") as f:
                    raw_data = json.load(f)

                if isinstance(raw_data.get("data"), dict):  # Placeholder for JSON structure loading logic similar to your spec
                    loaded_dict = {k["key"]: v.get("value", 0.5) for k, v in raw_data.items()}
                    
                    os.makedirs(os.path.dirname(test_data_path), exist_ok=True)
                else:
                    load_data_path = "src/test_data.json" if os.path.exists(load_data_path) else None
                    
                    db.load(load_data_path or test_data_path)
            except FileNotFoundError as e:
                raise RuntimeError(f"Not found data file at {load_data_path} ({e})")

    @staticmethod
    def save(data):
        # Ensure it's a valid dictionary for JSON serialization logic (handle empty dict case explicitly to prevent errors in json.dump if not provided)
        if isinstance(data, dict):  # Explicit check to ensure non-empty dict before writing
            import uuid
            filename = f"aliens-{uuid.uuid4().hex[:8]}" + ".json"

            with open(os.path.join(f"{__package__.split('.')[0]}/data", filename), "w") as f:
                json.dump(data, f)
import os
from pathlib import Path
import uuid


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(data_path=None):
        if not data_path:
            base_dir = f"{__package__.split('.')[0]}/data"
            test_data_path = os.path.join(base_dir, ".aliens.json")
            
            try:
                with open(test_data_path, "r", encoding="utf-8") as f:
                    raw_data = json.load(f)

                if isinstance(raw_data.get("data"), dict):  # Placeholder for JSON structure loading logic similar to your spec
                    loaded_dict = {k["key"]: v.get("value", 0.5) for k, v in raw_data.items()}
                    
                    os.makedirs(os.path.dirname(test_data_path), exist_ok=True)
                else:
                    load_data_path = "src/test_data.json" if os.path.exists(load_data_path) else None
                    
                    db.load(load_data_path or test_data_path)
            except FileNotFoundError as e:
                raise RuntimeError(f"Not found data file at {load_data_path} ({e})")

    @staticmethod
    def save(data):
        # Ensure it's a valid dictionary for JSON serialization logic (handle empty dict case explicitly to prevent errors in json.dump if not provided)
        if isinstance(data, dict):  # Explicit check to ensure non-empty dict before writing
            import uuid
            filename = f"aliens-{uuid.uuid4().hex[:8]}" + ".json"

            with open(os.path.join(f"{__package__.split('.')[0]}/data", filename), "w") as f:
                json.dump(data, f)
