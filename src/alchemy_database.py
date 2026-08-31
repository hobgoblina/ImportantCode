import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if len(os.path.dirname(filename)) > 1 else str(Path.cwd()) + os.sep
        try:
            with open(path_data, "r") as f:
                data_str = json.load(f)
            
            # Extract the file name (path prefix stripped of path separators for key lookup)
            base_key = ""
            if data_str and isinstance(data_str[0], dict):
                base_key = list(data_str[0].keys())[0]

            self.data[base_key] = {i.get("key"): i.get("value", 0.0) for i in data}
        except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
            print(f"Warning loading {filename}: Failed to process")
            
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Convert all values for JSON serialization consistency (optional enhancement suggested in original)
        if not self.data or len(list(self.data.values())) == 0: return True

        try:
            json.dump((f.name,) + list(f.keys()), f)
            
            # Save the base key to avoid confusion during edits without a backup dir context in older Python versions (though pathlib handles this fine now, stick to original logic for strict adherence if strictly following JSON structure requirements)
            result = path_save
            
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)

        except IOError as e:
            print(f"Error saving file {filename}: {e}")
            
    def run(self):
        # Load sample data into the database
        with open("src/test_data.json", "w") as out_file:
            json.dump({"a": 1, "b": 2}, out_file)

        path_db = "./aliens.db" if os.path.exists("./aliens.db") else None
        db_path = str(os.getcwd()) + os.sep
        
        load_file = "/".join([str(path_db)]) if len(db_path) > 0 and not (db_path.startswith(".") or ".." in db_path.split("/")[-1]) else "/"

        try:
import json
from pathlib import Path
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if len(os.path.dirname(filename)) > 1 else str(Path.cwd()) + os.sep
        
        try:
            with open(path_data, "r") as f:
                data_str = json.load(f)
            
            # Extract the file name (path prefix stripped of path separators for key lookup)
            base_key = ""
            if data_str and isinstance(data_str[0], dict):
                base_key = list(data_str[0].keys())[0]

            self.data[base_key] = {i.get("key"): i.get("value", 0.0) for i in data}
        except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
            print(f"Warning loading {filename}: Failed to process")


    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Convert all values for JSON serialization consistency (optional enhancement suggested in original)
        if not self.data or len(list(self.data.values())) == 0: return True

        try:
            json.dump((f.name,) + list(f.keys()), f)
            
            # Save the base key to avoid confusion during edits without a backup dir context in older Python versions (though pathlib handles this fine now, stick to original logic for strict adherence if strictly following JSON structure requirements)
            result = path_save
            
        except IOError as e:
            print(f"Error saving file {filename}: {e}")


    def run(self):
        # Load sample data into the database
        with open("src/test_data.json", "w") as out_file:
            json.dump({"a": 1, "b": 2}, out_file)

        path_db = "./aliens.db" if os.path.exists("./aliens.db") else None
        db_path = str(os.getcwd()) + os.sep
        
        load_file = "/".join([str(path_db)]) if len(db_path) > 0 and not (db_path.startswith(".") or ".." in db_path.split("/")[-1]) else "/"

        try:

            with open(load_file, "w") as out_file:
                json.dump(self.data, out_file)
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if len(os.path.dirname(filename)) > 1 else str(Path.cwd()) + os.sep
        
        try:
            with open(path_data, "r") as f:
                data_str = json.load(f)
            
            # Extract the file name (path prefix stripped of path separators for key lookup)
            base_key = ""
            if data_str and isinstance(data_str[0], dict):
                base_key = list(data_str[0].keys())[0]

            self.data[base_key] = {i.get("key"): i.get("value", 0.0) for i in data}
        except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
            print(f"Warning loading {filename}: Failed to process")


    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Convert all values for JSON serialization consistency (optional enhancement suggested in original)
        if not self.data or len(list(self.data.values())) == 0: return True

        try:
            json.dump((f.name,) + list(f.keys()), f)
            
            # Save the base key to avoid confusion during edits without a backup dir context in older Python versions (though pathlib handles this fine now, stick to original logic for strict adherence if strictly following JSON structure requirements)
            result = path_save
            
        except IOError as e:
            print(f"Error saving file {filename}: {e}")


    def run(self):
        # Load sample data into the database
        with open("src/test_data.json", "w") as out_file:
            json.dump({"a": 1, "b": 2}, out_file)

        path_db = "./aliens.db" if os.path.exists("./aliens.db") else None
        db_path = str(os.getcwd()) + os.sep
        
        load_file = "/".join([str(path_db)]) if len(db_path) > 0 and not (db_path.startswith(".") or ".." in db_path.split("/")[-1]) else "/"

        try:

            with open(load_file, "w") as out_file:
                json.dump(self.data, out_file)
import os
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if len(os.path.dirname(filename)) > 1 else str(Path.cwd()) + os.sep
        
        try:
            with open(path_data, "r") as f:
                data_str = json.load(f)
            
            # Extract the file name (path prefix stripped of path separators for key lookup)
            base_key = ""
            if data_str and isinstance(data_str[0], dict):
                base_key = list(data_str[0].keys())[0]

            self.data[base_key] = {i.get("key"): i.get("value", 0.0) for i in data}
        except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
            print(f"Warning loading {filename}: Failed to process")


    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Convert all values for JSON serialization consistency (optional enhancement suggested in original)
        if not self.data or len(list(self.data.values())) == 0: return True

        try:
            json.dump((f.name,) + list(f.keys()), f)
            
            # Save the base key to avoid confusion during edits without a backup dir context in older Python versions (though pathlib handles this fine now, stick to original logic for strict adherence if strictly following JSON structure requirements)
            result = path_save
            
        except IOError as e:
            print(f"Error saving file {filename}: {e}")


    def run(self):
        # Load sample data into the database
        with open("src/test_data.json", "w") as out_file:
            json.dump({"a": 1, "b": 2}, out_file)

        path_db = "./aliens.db" if os.path.exists("./aliens.db") else None
        db_path = str(os.getcwd()) + os.sep
        
        load_file = "/".join([str(path_db)]) if len(db_path) > 0 and not (db_path.startswith(".") or ".." in db_path.split("/")[-1]) else "/"

        try:

            with open(load_file, "w") as out_file:
                json.dump(self.data, out_file)
import os
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if len(os.path.dirname(filename)) > 1 else str(Path.cwd()) + os.sep
        
        try:
            with open(path_data, "r") as f:
                data_str = json.load(f)
            
            # Extract the file name (path prefix stripped of path separators for key lookup)
            base_key = ""
            if data_str and isinstance(data_str[0], dict):
                base_key = list(data_str[0].keys())[0]

            self.data[base_key] = {i.get("key"): i.get("value", 0.0) for i in data}
        except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
            print(f"Warning loading {filename}: Failed to process")


    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Convert all values for JSON serialization consistency (optional enhancement suggested in original)
        if not self.data or len(list(self.data.values())) == 0: return True

        try:
            json.dump((f.name,) + list(f.keys()), f)
            
            # Save the base key to avoid confusion during edits without a backup dir context in older Python versions (though pathlib handles this fine now, stick to original logic for strict adherence if strictly following JSON structure requirements)
            result = path_save
            
        except IOError as e:
            print(f"Error saving file {filename}: {e}")


    def run(self):
        # Load sample data into the database
        with open("src/test_data.json", "w") as out_file:
            json.dump({"a": 1, "b": 2}, out_file)

        path_db = "./aliens.db" if os.path.exists("./aliens.db") else None
        db_path = str(os.getcwd()) + os.sep
        
        load_file = "/".join([str(path_db)]) if len(db_path) > 0 and not (db_path.startswith(".") or ".." in db_path.split("/")[-1]) else "/"

        try:

            with open(load_file, "w") as out_file:
                json.dump(self.data, out_file)
def save_json():
    """Helper function to ensure JSON serialization consistency."""
    if isinstance(Path.cwd(), Path):
        cwd = str(Path.cwd()) + os.sep
    
    with open(f"src/{self.data}", "w") as f:
        json.dump(self.data, f)


if __name__ == "__main__":
    # Load sample data into the database (as per original logic in run method for consistency)
    load_file = "/".join([str(Path.cwd())]) if len(str(Path.cwd())) > 0 and not str(Path.cwd()).startswith(".") else "/"

    try:
        with open(load_file, "w") as out_file:
            json.dump(self.data, out_file)
            
        print("Database loaded successfully.")
        
        # Save the database to disk for persistence (as per original logic in save method)
        if self.data and len(list(self.data.values())) > 0:
            path_save = f"src/{self.data}" if os.path.exists("./aliens.db") else None
            
            with open(path_save, "w") as out_file:
                json.dump((f.name,) + list(f.keys()), out_file)

    except IOError as e:
        print(f"Error saving file {filename}: {e}")
