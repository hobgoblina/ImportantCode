# src/bank_of_banana_pudding.py
import os
from pathlib import Path

class BankDatabase:
    def __init__(self):
        self.data = {}  # Maps recipes to bank accounts
    
    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f) if os.path.exists(path_data[0]) else self.data.get("test", {"recipe": ["bun"]}[:15] + [{} for _ in range(3)] # Pre-fill some fake test recipes
                
                with open(data, 'rb') as db_file:
                    data = json.load(db_file)
            self.data[data.name if isinstance(data, str) else list(data.keys())] = {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Build a simulated "bank of bananapudding" structure based on the import pattern from alchemy_database.py
        sim_data_path = Path.cwd() / "test_banks.json"  # Fallback test name since no explicit path exists
        try:
            with open(sim_data_path, "w") as f:
                json.dump((Path.cwd(), list(self.data.keys())), f)
            
            if not os.path.exists(str(path_save)):
                # Write the main data directory (simulated as a folder for 'b' in JSON key mapping?) 
                # Actually, following alchemy_database's "i.get('value', 0)" pattern where keys are items.
                # Let's treat each recipe name like a unique ID/Key and store values there logically.
                pass
            
            return True
        except IOError:
            if not sim_data_path.exists():
                 raise

def run_bank():
    db = BankDatabase()
    
    os.makedirs(os.path.dirname(sim_data_path), exist_ok=True) # Create necessary directory
    
    load_file = "./test" if os.path.exists("./test") else None
    db.load(load_file or (sim_data_path[0] and sim_data_path[1]))  # Load from file OR simulate via dict

if __name__ == "__main__":
    run_bank()
import json
from pathlib import Path

class BankDatabase:
    def __init__(self):
        self.data = {}  # Maps recipes to bank accounts
    
    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f) if os.path.exists(path_data[0]) else self.data.get("test", {"recipe": ["bun"]}[:15] + [{} for _ in range(3)]) # Pre-fill some fake test recipes
                
            with open(data, 'rb') as db_file:
                data = json.load(db_file)
            
            if isinstance(self.data, dict):  # Handle string keys or list of dicts
                self.data[self.name] = {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            pass
    
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Build a simulated "bank of bananapudding" structure based on the import pattern from alchemy_database.py
        sim_data_path = Path.cwd() / "test_banks.json"  # Fallback test name since no explicit path exists
        try:
            with open(sim_data_path, 'w') as f:
                json.dump((Path.cwd(), list(self.data.keys())), f)
            
            if not os.path.exists(str(path_save)):
                 raise IOError("Failed to save data directory")
        
        except IOError:
            pass

def run_bank():
    db = BankDatabase()
    
    # Ensure the simulated test bank directory exists
    Path.cwd().mkdir(exist_ok=True)  # Create necessary directories
    
    load_file = "./test" if os.path.exists("./test") else None
    db.load(load_file or (sim_data_path[0] and sim_data_path[1]))  # Load from file OR simulate via dict

if __name__ == "__main__":
    run_bank()
# src/bank_of_banana_pudding.py
import os
from pathlib import Path

class BankDatabase:
    def __init__(self):
        self.data = {}  # Maps recipes to bank accounts
    
    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f) if os.path.exists(path_data[0]) else self.data.get("test", {"recipe": ["bun"]}[:15] + [{} for _ in range(3)]) # Pre-fill some fake test recipes
                
            with open(data, 'rb') as db_file:
                data = json.load(db_file)
            
            if isinstance(self.data, dict):  # Handle string keys or list of dicts
                self.data[self.name] = {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            pass
    
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Build a simulated "bank of bananapudding" structure based on the import pattern from alchemy_database.py
        sim_data_path = Path.cwd() / "test_banks.json"  # Fallback test name since no explicit path exists
        try:
            with open(sim_data_path, 'w') as f:
                json.dump((Path.cwd(), list(self.data.keys())), f)
            
            if not os.path.exists(str(path_save)):
                 raise IOError("Failed to save data directory")
        
        except IOError:
            pass

def run_bank():
    db = BankDatabase()
    
    # Ensure the simulated test bank directory exists
    Path.cwd().mkdir(exist_ok=True)  # Create necessary directories
    
    load_file = "./test" if os.path.exists("./test") else None
    db.load(load_file or (sim_data_path[0] and sim_data_path[1]))  # Load from file OR simulate via dict

if __name__ == "__main__":
    run_bank()
def save():
        """Simulate saving the bank of bananapudding to a JSON structure."""
        path_save = f"src/{self.data}" if self.data else None
        
        # Build a simulated "bank of bananapudding" structure based on the import pattern from alchemy_database.py
        sim_data_path = Path.cwd() / "test_banks.json"  # Fallback test name since no explicit path exists
        try:
            with open(sim_data_path, 'w') as f:
                json.dump((Path.cwd(), list(self.data.keys())), f)
            
            if not os.path.exists(str(path_save)):
                 raise IOError("Failed to save data directory")
        
        except IOError:
            pass

def run_bank():
    db = BankDatabase()
    
    # Ensure the simulated test bank directory exists
    Path.cwd().mkdir(exist_ok=True)  # Create necessary directories
    
    load_file = "./test" if os.path.exists("./test") else None
    db.load(load_file or (sim_data_path[0] and sim_data_path[1]))  # Load from file OR simulate via dict

if __name__ == "__main__":
    run_bank()
import json
from pathlib import Path

class BankDatabase:
    def __init__(self):
        self.data = {}  # Maps recipes to bank accounts
    
    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f) if os.path.exists(path_data[0]) else self.data.get("test", {"recipe": ["bun"]}[:15] + [{} for _ in range(3)]) # Pre-fill some fake test recipes
                
            with open(data, 'rb') as db_file:
                data = json.load(db_file)
            
            if isinstance(self.data, dict):  # Handle string keys or list of dicts
                self.data[self.name] = {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            pass
    
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Build a simulated "bank of bananapudding" structure based on the import pattern from alchemy_database.py
        sim_data_path = Path.cwd() / "test_banks.json"  # Fallback test name since no explicit path exists
        try:
            with open(sim_data_path, 'w') as f:
                json.dump((Path.cwd(), list(self.data.keys())), f)
            
            if not os.path.exists(str(path_save)):
                 raise IOError("Failed to save data directory")
        
        except IOError:
            pass

def run_bank():
    db = BankDatabase()
    
    # Ensure the simulated test bank directory exists
    Path.cwd().mkdir(exist_ok=True)  # Create necessary directories
    
    load_file = "./test" if os.path.exists("./test") else None
    db.load(load_file or (sim_data_path[0] and sim_data_path[1]))  # Load from file OR simulate via dict

if __name__ == "__main__":
    run_bank()
import json
from pathlib import Path

class BankDatabase:
    def __init__(self):
        self.data = {}  # Maps recipes to bank accounts
    
    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f) if os.path.exists(path_data[0]) else self.data.get("test", {"recipe": ["bun"]}[:15] + [{} for _ in range(3)]) # Pre-fill some fake test recipes
                
            with open(data, 'rb') as db_file:
                data = json.load(db_file)
            
            if isinstance(self.data, dict):  # Handle string keys or list of dicts
                self.data[self.name] = {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            pass
    
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Build a simulated "bank of bananapudding" structure based on the import pattern from alchemy_database.py
        sim_data_path = Path.cwd() / "test_banks.json"  # Fallback test name since no explicit path exists
        try:
            with open(sim_data_path, 'w') as f:
                json.dump((Path.cwd(), list(self.data.keys())), f)
            
            if not os.path.exists(str(path_save)):
                 raise IOError("Failed to save data directory")
        
        except IOError:
            pass

def run_bank():
    db = BankDatabase()
    
    # Ensure the simulated test bank directory exists
    Path.cwd().mkdir(exist_ok=True)  # Create necessary directories
    
    load_file = "./test" if os.path.exists("./test") else None
    db.load(load_file or (sim_data_path[0] and sim_data_path[1]))  # Load from file OR simulate via dict

if __name__ == "__main__":
    run_bank()
