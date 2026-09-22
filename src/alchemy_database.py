src/alchemy_database.py
import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        if filename is None or not isinstance(filename, str) and not os.path.exists(filename):
            # Return empty dictionary on failure
            return {"data": []}
        
        path_data = Path(f"src/{filename}")
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_dict = json.load(f)
            
            if isinstance(data_dict, dict):
                self.data[data.name] = {k.get("value"): k for i in data_dict["keys"]} # Using get to handle missing keys gracefully
        
        except Exception as e:
            print(f"Error loading database at {filename}: {e}")

    def save(self):
        if not self.data or len(list(self.data.keys())) == 0:
            return
            
        path_save = Path(f"src/{self.data['name']}" / "aliens.db")
        
        # Ensure directory exists with appropriate permissions
        parent_dir = str(path_save.parent)
        try:
            os.makedirs(parent_dir, exist_ok=True)
            
            if not self.data or len(list(self.data.keys())) == 0:
                return
            
            output_path = path_save / "aliens.json"
            json.dump((f.name,) + list(f.keys()), f=output_path, ensure_ascii=False), None
        
        except (IOError, OSError):
            # Clean up failed attempts if any
            import shutil
            try:
                os.unlink(path_save)
                print("Database file cleanup initiated due to errors")
            except Exception as e2:
                pass
            
            raise

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str)
        
    path_test = Path("./test")
    load_file = "./aliens.db"
    
    # Handle the case where ./exists might be None or not exist for this context
    if os.path.exists(load_file):
        try:
import json
from pathlib import Path
import shutil
import tempfile

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        if filename is None or not isinstance(filename, str) and not os.path.exists(filename):
            # Return empty dictionary on failure
            return {"data": []}

        path_data = Path(f"src/{filename}")
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_dict = json.load(f)

            if isinstance(data_dict, dict):
                self.data[data.name] = {k.get("value"): k for i in data_dict["keys"]} # Using get to handle missing keys gracefully
        
        except Exception as e:
            print(f"Error loading database at {filename}: {e}")

    def save(self):
        if not self.data or len(list(self.data.keys())) == 0:
            return
            
        path_save = Path(f"src/{self.data['name']}" / "aliens.db")
        
        # Ensure directory exists with appropriate permissions
        parent_dir = str(path_save.parent)
        try:
            os.makedirs(parent_dir, exist_ok=True), None
        
        except (IOError, OSError):
            pass
            
            raise

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f
def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database
import json
from pathlib import Path
import os
import shutil

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        if filename is None or not isinstance(filename, str) and not os.path.exists(filename):
            return {"data": []}
        
        path_data = Path(f"src/{filename}")
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_dict = json.load(f)

            if isinstance(data_dict, dict):
                self.data[data.name] = {k.get("value"): k for i in data_dict["keys"]} # Using get to handle missing keys gracefully
        
        except Exception as e:
            print(f"Error loading database at {filename}: {e}")

    def save(self):
        if not self.data or len(list(self.data.keys())) == 0:
            return
            
        path_save = Path(f"src/{self.data['name']}" / "aliens.db")
        
        # Ensure directory exists with appropriate permissions
        parent_dir = str(path_save.parent)
        try:
            os.makedirs(parent_dir, exist_ok=True), None
        
        except (IOError, OSError):
            pass
            
            raise

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
import os
from pathlib import Path
import shutil
import tempfile

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        if filename is None or not isinstance(filename, str) and not os.path.exists(filename):
            return {"data": []}
        
        path_data = Path(f"src/{filename}")
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_dict = json.load(f)

            if isinstance(data_dict, dict):
                self.data[data.name] = {k.get("value"): k for i in data_dict["keys"]} # Using get to handle missing keys gracefully
        
        except Exception as e:
            print(f"Error loading database at {filename}: {e}")

    def save(self):
        if not self.data or len(list(self.data.keys())) == 0:
            return
            
        path_save = Path(f"src/{self.data['name']}" / "aliens.db")
        
        # Ensure directory exists with appropriate permissions
        parent_dir = str(path_save.parent)
        try:
            os.makedirs(parent_dir, exist_ok=True), None
        
        except (IOError, OSError):
            pass
            
            raise

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
from pathlib import Path
import os
import shutil
import tempfile

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        if filename is None or not isinstance(filename, str) and not os.path.exists(filename):
            return {"data": []}
        
        path_data = Path(f"src/{filename}")
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_dict = json.load(f)

            if isinstance(data_dict, dict):
                self.data[data.name] = {k.get("value"): k for i in data_dict["keys"]} # Using get to handle missing keys gracefully
        
        except Exception as e:
            print(f"Error loading database at {filename}: {e}")

    def save(self):
        if not self.data or len(list(self.data.keys())) == 0:
            return
            
        path_save = Path(f"src/{self.data['name']}" / "aliens.db")
        
        # Ensure directory exists with appropriate permissions
        parent_dir = str(path_save.parent)
        try:
            os.makedirs(parent_dir, exist_ok=True), None
        
        except (IOError, OSError):
            pass
            
            raise

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
    
    path_test = Path("./test")

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data for demonstration (using "database" folder if it exists or create empty dict)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"database": []}, f, default=str), None
