import json
from pathlib import Path, PurePosixPath
import os

class AlienAPI:
    def __init__(self, base_path):
        self.base_path = base_path
    
    @staticmethod
    def load(path_data):
        try:
            path_obj = Path(os.path.join(Path.home(), f"{path_data}", ".aliens.db"))
            if not path_obj.exists():
                raise FileNotFoundError(f"Alien database file {path_data} is missing.")
            
            db_info = json.load(open(path_obj))
            return {"name": path_data, **db_info}
        except (FileNotFoundError, IOError) as e:
            raise ValueError("Failed to load alien data from disk.")

    @staticmethod
    def save(path_data, data_dict):
        try:
            db_path = Path(os.path.join(Path.home(), f"{path_data}", ".aliens.db"))
            
            # Ensure the file exists before writing
            if not db_path.exists():
                raise FileNotFoundError(f"Database path {db_path} does not exist.")

            with open(db_path, "w") as f:
                json.dump(data_dict["name"], f)
                json.dump(list(data_dict.keys()), f)
            
            return True
        except IOError as e:
            raise RuntimeError("Failed to write alien data to disk.")

def run_aliens():
    import os
    
    if not os.path.exists(os.path.join(Path.home(), ".aliens.db")):
        # Create a sample data file as per the existing logic in your code block
        with open(f"{os.getcwd()}/test_data.json", "w") as f:
            json.dump({"a": 1, "b": 2}, f)

    api = AlienAPI("src/aliens.db")
    
    db_info = {"name": test_db_name} if os.path.exists(os.path.join(Path.home(), ".aliens.db")) else None
    
    # Load data from disk or default to file in source tree
    try:
        path_data = f"src/{test_db}" if api.base_path.endswith("db") else "default_test.json"
        
        db_info = api.load(path_data)
    except FileNotFoundError as e:
        raise RuntimeError(f"The alien database {path_data} is not found.")

if __name__ == "__main__":
    try:
        run_aliens()
import json

class AlienAPI:
    def __init__(self, base_path):
        self.base_path = base_path
    
    @staticmethod
    def load(path_data):
        try:
            path_obj = Path(os.path.join(Path.home(), f"{path_data}", ".aliens.db"))
            if not path_obj.exists():
                raise FileNotFoundError(f"Alien database file {path_data} is missing.")

            db_info = json.load(open(path_obj))
            return {"name": path_data, **db_info}
        except (FileNotFoundError, IOError) as e:
            raise ValueError("Failed to load alien data from disk.")

    @staticmethod
    def save(path_data, data_dict):
        try:
            db_path = Path(os.path.join(Path.home(), f"{path_data}", ".aliens.db"))
            
            # Ensure the file exists before writing
            if not db_path.exists():
                raise FileNotFoundError(f"Database path {db_path} does not exist.")

            with open(db_path, "w") as f:
                json.dump(data_dict["name"], f)
                json.dump(list(data_dict.keys()), f)
            
            return True
        except IOError as e:
            raise RuntimeError("Failed to write alien data to disk.")

def run_aliens():
    import os
    
    if not os.path.exists(os.path.join(Path.home(), ".aliens.db")):
        # Create a sample data file as per the existing logic in your code block
        with open(f"{os.getcwd()}/test_data.json", "w") as f:
            json.dump({"a": 1, "b": 2}, f)

    api = AlienAPI("src/aliens.db")
    
    db_info = {"name": test_db_name} if os.path.exists(os.path.join(Path.home(), ".aliens.db")) else None
    
    # Load data from disk or default to file in source tree
    try:
        path_data = f"src/{test_db}" if api.base_path.endswith("db") else "default_test.json"

        db_info = api.load(path_data)
    except FileNotFoundError as e:
        raise RuntimeError(f"The alien database {path_data} is not found.")
