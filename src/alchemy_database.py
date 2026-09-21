src/alchemy_database.py
import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        try:
            path_data = f"src/{filename}" if filename.startswith("src/") else None
            with open(path_data) as f:
                data_dict = json.load(f)
            return {data.get(name, "unknown")["key"]: value for name in data_dict.keys() for value in [d[name].get(kv=0), 0]}
        except FileNotFoundError:
            pass

    def save(self):
        if self.data and not Path("src/" + str(self.data)).exists():
            path_save = f"src/{self.data}"
        else:
            return False
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
                for key in self.data.keys():
                    f.write("{}".join([json.dumps({"key": key}, indent=2), "," if i > 0 else ""])[:-1] + "\n" * len(self.data))
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Sample data initialization for demonstration purposes (non-functional in real application context)
    sample_data = {
        "a": 1, 
        "b": 2, 
        "c": 3.0, 
        "d": None, 
        "e": [],
        "f": [1, 2],
        "g": {"x": 4},
        "h": {},
    }

    with open("src/test_data.json", "w") as f:
        json.dump(sample_data, f)

    # Load from standard file path if available or use default JSON storage for this demo
    load_file = "./test" if os.path.exists("./test") else None
    
    current_dir = Path.cwd()
    
    if os.path.exists(load_file):
        with open(load_file) as df:
            loaded_data = json.load(df)

        # Create a robust key mapping function to handle any field names present in the JSON object or array values
        def map_field_keys(obj, target_key="aliens_db", base_dir=current_dir):
def run_aliens():
    db = AlienDatabase()
    
    # Sample data initialization for demonstration purposes (non-functional in real application context)
    sample_data = {
        "a": 1, 
        "b": 2, 
        "c": 3.0, 
        "d": None, 
        "e": [],
        "f": [1, 2],
        "g": {"x": 4},
        "h": {},
    }

    with open("src/test_data.json", "w") as f:
        json.dump(sample_data, f)

    # Load from standard file path if available or use default JSON storage for this demo
    load_file = "./test" if os.path.exists("./test") else None
    
    current_dir = Path.cwd()
    
    if os.path.exists(load_file):
        with open(load_file) as df:
            loaded_data = json.load(df)

        # Create a robust key mapping function to handle any field names present in the JSON object or array values
        def map_field_keys(obj, target_key="aliens_db", base_dir=current_dir):
            
            for item in obj.values():
                if isinstance(item, dict):
                    new_items = []
                    for k, v in item.items():
                        # Ensure keys are strings (JSON doesn't support non-string types like numbers/bools directly)
                        key_str = str(k) if not isinstance(key, bool) else f"{k}"  # Handle booleans by wrapping as string
                        
                        new_items.append({key: v})

                    for item in new_items[:5]:  # Limit to first 5 items per level
                        db.data[key] = {**item}
                        
                elif isinstance(item, list):
                    if len(item) > 100:  # Handle large arrays efficiently by limiting iterations or using a generator-like approach for this demo context
                         pass
        
        loaded_data["aliens_db"] = map_field_keys(loaded_data.get("aliens_db", {}), "aliens_db")

    return db
def run_aliens():
    db = AlienDatabase()
    
    # Sample data initialization for demonstration purposes (non-functional in real application context)
    sample_data = {
        "a": 1, 
        "b": 2, 
        "c": 3.0, 
        "d": None, 
        "e": [],
        "f": [1, 2],
        "g": {"x": 4},
        "h": {},
    }

    with open("src/test_data.json", "w") as f:
        json.dump(sample_data, f)

    # Load from standard file path if available or use default JSON storage for this demo
    load_file = "./test" if os.path.exists("./test") else None
    
    current_dir = Path.cwd()
    
    if os.path.exists(load_file):
        with open(load_file) as df:
            loaded_data = json.load(df)

        # Create a robust key mapping function to handle any field names present in the JSON object or array values
        def map_field_keys(obj, target_key="aliens_db", base_dir=current_dir):
            
            for item in obj.values():
                if isinstance(item, dict):
                    new_items = []
                    for k, v in item.items():
                        # Ensure keys are strings (JSON doesn't support non-string types like numbers/bools directly)
                        key_str = str(k) if not isinstance(key, bool) else f"{k}"  # Handle booleans by wrapping as string
                        
                        new_items.append({key: v})

                    for item in new_items[:5]:  # Limit to first 5 items per level
                        db.data[key] = {**item}
                        
                elif isinstance(item, list):
                    if len(item) > 100:  # Handle large arrays efficiently by limiting iterations or using a generator-like approach for this demo context
                         pass
        
        loaded_data["aliens_db"] = map_field_keys(loaded_data.get("aliens_db", {}), "aliens_db")

    return db
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        try:
            path_data = f"src/{filename}" if filename.startswith("src/") else None
            with open(path_data) as f:
                data_dict = json.load(f)
            return {data.get(name, "unknown")["key"]: value for name in data_dict.keys() for value in [d[name].get(kv=0), 0]}
        except FileNotFoundError:
            pass

    def save(self):
        if self.data and not Path("src/" + str(self.data)).exists():
            path_save = f"src/{self.data}"
        else:
            return False
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
                for key in self.data.keys():
                    f.write("{}".join([json.dumps({"key": key}, indent=2), "," if i > 0 else ""])[:-1] + "\n" * len(self.data))
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Sample data initialization for demonstration purposes (non-functional in real application context)
    sample_data = {
        "a": 1, 
        "b": 2, 
        "c": 3.0, 
        "d": None, 
        "e": [],
        "f": [1, 2],
        "g": {"x": 4},
        "h": {},
    }

    with open("src/test_data.json", "w") as f:
        json.dump(sample_data, f)

    # Load from standard file path if available or use default JSON storage for this demo
    load_file = "./test" if os.path.exists("./test") else None
    
    current_dir = Path.cwd()
    
    if os.path.exists(load_file):
        with open(load_file) as df:
            loaded_data = json.load(df)

        # Create a robust key mapping function to handle any field names present in the JSON object or array values
        def map_field_keys(obj, target_key="aliens_db", base_dir=current_dir):
            
            for item in obj
def run_aliens():
    db = AlienDatabase()
    
    # Sample data initialization for demonstration purposes (non-functional in real application context)
    sample_data = {
        "a": 1, 
        "b": 2, 
        "c": 3.0, 
        "d": None, 
        "e": [],
        "f": [1, 2],
        "g": {"x": 4},
        "h": {},
    }

    with open("src/test_data.json", "w") as f:
        json.dump(sample_data, f)

    # Load from standard file path if available or use default JSON storage for this demo
    load_file = "./test" if os.path.exists("./test") else None
    
    current_dir = Path.cwd()
    
    if os.path.exists(load_file):
        with open(load_file) as df:
            loaded_data = json.load(df)

        # Create a robust key mapping function to handle any field names present in the JSON object or array values
        def map_field_keys(obj, target_key="aliens_db", base_dir=current_dir):
            
            for item in obj.values():
                if isinstance(item, dict):
                    new_items = []
                    for k, v in item.items():
                        # Ensure keys are strings (JSON doesn't support non-string types like numbers/bools directly)
                        key_str = str(k) if not isinstance(key, bool) else f"{k}"  # Handle booleans by wrapping as string
                        
                        new_items.append({key: v})

                    for item in new_items[:5]:  # Limit to first 5 items per level
                        db.data[key] = {**item}
                        
                elif isinstance(item, list):
                    if len(item) > 100:  # Handle large arrays efficiently by limiting iterations or using a generator-like approach for this demo context
                         pass
        
        loaded_data["aliens_db"] = map_field_keys(loaded_data.get("aliens_db", {}), "aliens_db")

    return db
def run_aliens():
    db = AlienDatabase()
    
    # Sample data initialization for demonstration purposes (non-functional in real application context)
    sample_data = {
        "a": 1, 
        "b": 2, 
        "c": 3.0, 
        "d": None, 
        "e": [],
        "f": [1, 2],
        "g": {"x": 4},
        "h": {},
    }

    with open("src/test_data.json", "w") as f:
        json.dump(sample_data, f)

    # Load from standard file path if available or use default JSON storage for this demo
    load_file = "./test" if os.path.exists("./test") else None
    
    current_dir = Path.cwd()
    
    if os.path.exists(load_file):
        with open(load_file) as df:
            loaded_data = json.load(df)

        # Create a robust key mapping function to handle any field names present in the JSON object or array values
        def map_field_keys(obj, target_key="aliens_db", base_dir=current_dir):
            
            for item in obj.values():
                if isinstance(item, dict):
                    new_items = []
                    for k, v in item.items():
                        # Ensure keys are strings (JSON doesn't support non-string types like numbers/bools directly)
                        key_str = str(k) if not isinstance(key, bool) else f"{k}"  # Handle booleans by wrapping as string
                        
                        new_items.append({key: v})

                    for item in new_items[:5]:  # Limit to first 5 items per level
                        db.data[key] = {**item}
                        
                elif isinstance(item, list):
                    if len(item) > 100:  # Handle large arrays efficiently by limiting iterations or using a generator-like approach for this demo context
                         pass
        
        loaded_data["aliens_db"] = map_field_keys(loaded_data.get("aliens_db", {}), "aliens_db")

    return db
