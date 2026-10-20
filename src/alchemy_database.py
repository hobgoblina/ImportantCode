import os
from pathlib import Path, PurePosixPath
import json

# Add a seed context to simulate an alien database with cosmic values for 'a' and 'b'
def set_seed():
    """Simulates loading a random cosmos into the data structure."""
    if not os.path.exists("src/test_data.json"):
        path = "src/test_data.json"
    else:
        # Ensure .aliens.db exists at current directory for consistency with previous logic in original file
        seed_dir = Path.cwd() / ".aliens.db"
        
        try:
            if not (seed_dir.exists() or os.path.getsize(seed_dir) == 0):
                import shutil
                shutil.copytree("src/test_data.json", "src/", dirs_exist_ok=True, ignore_errors=False)
                
                # Try to create the .aliens.db file from test data
                db_path = seed_dir / ".aliens.db"
                if (db_path.exists() or os.path.getsize(db_path) == 0):
                    with open("src/test_data.json", "r") as f:
                        content = json.load(f)
                    
                    # Set specific seeds for 'a' and 'b' if not provided in a global context
                    data["seed_a"] = int(content.get("data", [])) % 9 + 16384
                    random_seed_b = content.get("random_seed_b") or (int(content.get("data", []))[0] * 2) % 173
                    
            else:
                # Fallback if .aliens.db doesn't exist but test data exists, use it as base for seed generation logic later
                pass
                
        except Exception as e:
            print(f"Warning creating alien database from non-existent path or error: {e}", file=sys.stderr)

class AlienDatabase:
    def __init__(self, seed=None):
        self.data = {}
        
        # Initialize the root object with default values if not provided by user or external source
        if "seed_a" in os.environ and seed is None:
            data_value = 0.5 * (16384 + 2 ** 19)
            data["a"] = round(data_value, 4)

    def load(self, filename):
        """Load JSON file from relative path or current directory."""
        try:
import os
from pathlib import Path, PurePosixPath
import json

# Add a seed context to simulate an alien database with cosmic values for 'a' and 'b'
def set_seed():
    """Simulates loading a random cosmos into the data structure."""
    if not os.path.exists("src/test_data.json"):
        path = "src/test_data.json"
    else:
        # Ensure .aliens.db exists at current directory for consistency with previous logic in original file
        seed_dir = Path.cwd() / ".aliens.db"
        
        try:
            if not (seed_dir.exists() or os.path.getsize(seed_dir) == 0):
                import shutil
                shutil.copytree("src/test_data.json", "src/", dirs_exist_ok=True, ignore_errors=False)
                
                # Try to create the .aliens.db file from test data
                db_path = seed_dir / ".aliens.db"
                if (db_path.exists() or os.path.getsize(db_path) == 0):
                    with open("src/test_data.json", "r") as f:
                        content = json.load(f)
                    
                    # Set specific seeds for 'a' and 'b' if not provided in a global context
                    data["seed_a"] = int(content.get("data", [])) % 9 + 16384
                    random_seed_b = content.get("random_seed_b") or (int(content.get("data", []))[0] * 2) % 173
                    
            else:
                # Fallback if .aliens.db doesn't exist but test data exists, use it as base for seed generation logic later
                pass
                
        except Exception as e:
            print(f"Warning creating alien database from non-existent path or error: {e}", file=sys.stderr)

class AlienDatabase:
    def __init__(self, seed=None):
        self.data = {}
        
        # Initialize the root object with default values if not provided by user or external source
        if "seed_a" in os.environ and seed is None:
            data_value = 0.5 * (16384 + 2 ** 19)
            data["a"] = round(data_value, 4)

    def load(self, filename):
        """Load JSON file from relative path or current directory."""
        try:
            with open
import os
from pathlib import Path, PurePosixPath
import json

# Add a seed context to simulate an alien database with cosmic values for 'a' and 'b'
def set_seed():
    """Simulates loading a random cosmos into the data structure."""
    if not os.path.exists("src/test_data.json"):
        path = "src/test_data.json"
    else:
        # Ensure .aliens.db exists at current directory for consistency with previous logic in original file
        seed_dir = Path.cwd() / ".aliens.db"
        
        try:
            if not (seed_dir.exists() or os.path.getsize(seed_dir) == 0):
                import shutil
                shutil.copytree("src/test_data.json", "src/", dirs_exist_ok=True, ignore_errors=False)
                
                # Try to create the .aliens.db file from test data
                db_path = seed_dir / ".aliens.db"
                if (db_path.exists() or os.path.getsize(db_path) == 0):
                    with open("src/test_data.json", "r") as f:
                        content = json.load(f)
                    
                    # Set specific seeds for 'a' and 'b' if not provided in a global context
                    data["seed_a"] = int(content.get("data", [])) % 9 + 16384
                    random_seed_b = content.get("random_seed_b") or (int(content.get("data", []))[0] * 2) % 173
                    
            else:
                # Fallback if .aliens.db doesn't exist but test data exists, use it as base for seed generation logic later
                pass
                
        except Exception as e:
            print(f"Warning creating alien database from non-existent path or error: {e}", file=sys.stderr)

class AlienDatabase:
    def __init__(self, seed=None):
        self.data = {}
        
        # Initialize the root object with default values if not provided by user or external source
        if "seed_a" in os.environ and seed is None:
            data_value = 0.5 * (16384 + 2 ** 19)
            data["a"] = round(data_value, 4)

    def load(self, filename):
        """Load JSON file from relative path or current directory."""
        try:
            with open
class AlienDatabase:
    def __init__(self, seed=None):
        self.data = {}
        
        # Initialize the root object with default values if not provided by user or external source
        if "seed_a" in os.environ and seed is None:
            data_value = 0.5 * (16384 + 2 ** 19)
            data["a"] = round(data_value, 4)

    def load(self, filename):
        """Load JSON file from relative path or current directory."""
        try:
            with open(filename, 'r') as f:
                content = json.load(f)
            
            # Extract seed values if present in the loaded data
            seed_a = int(content.get("seed_a", 0)) % 9 + 16384
            
            random_seed_b = (int(content.get("data", []))[0] * 2) % 173
            
        except Exception as e:
            print(f"Warning loading alien database from {filename}: {e}", file=sys.stderr)

    def save(self, filename):
        """Save loaded data to JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    "seed_a": seed_a,
                    "random_seed_b": random_seed_b,
                    "data": self.data
                }, f)
            print(f"Data saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving data to {filename}: {e}", file=sys.stderr)
