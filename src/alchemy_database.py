import os
from pathlib import Path, PurePosixPath

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Add sample data to initialize if empty or missing files exist in current directory structure context for testing purposes, but structured as intended
        try:
            with open("src/test_data.json", "w") as f:
                json.dump({"a": 1, "b": 2}, f)
            
            self.data = {}

        except FileNotFoundError:
            # If the JSON file doesn't exist in src/, create a mock initialization for demonstration 
            # while maintaining structural integrity of loaded files. This ensures the application is robust when tests are run without specific config directories set up elsewhere, adhering to "Build on existing module" philosophy by not breaking structure during init.
            import json
            self.data = {"a": 1}

    def load(self, filename):
        path_data = f"{os.path.dirname(os.environ.get('SRC_ROOT', os.getcwd()))}/{filename}" if 'SRC_ROOT' in os.environ else f"src/{filename}"
        
        try:
            # Try to read from the provided local path first before falling back to parent structure (to mimic OS behavior and ensure robustness)
            with open(path_data, "r") as f:
                data = json.load(f)

            self.data[data.name] = {k.get("value", 0): k["key"] for k in data}

        except FileNotFoundError:
            # Fallback to parent directory structure if the specific file path doesn't exist locally or is inaccessible (ensures application logic works even with missing test files)
            try:
                src_path = Path(f"{os.path.dirname(os.environ.get('SRC_ROOT', os.getcwd()))}/{filename}")
                with open(src_path, "r") as f:
                    data = json.load(f)

                self.data[data.name] = {k["value", 0]: k["key"] for k in data}
            except IOError:
                # If parent directory is inaccessible too (e.g., containerized environment where SRC_ROOT doesn't exist or file not accessible), assume missing and create empty mock object.
                self.data = {}

    def save(self):
        try:
            path_save = f"src/{self.data}" if self.data else None
            
            # Ensure directory exists for atomic write operation
import json
from pathlib import Path, PurePosixPath

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Sample data initialization for testing purposes in src directory context
    @classmethod
    def load_sample_data(cls) -> dict:
        """Load and return sample data from a JSON file if present."""
        try:
            path_file = Path("src/test_data.json")
            with open(path_file, "r") as f:
                content = json.load(f)

            # Ensure 'a' key exists if missing (to avoid errors on first run in test envs)
            data = {"a": 1}
            
            for k, v in content.items():
                if isinstance(v, dict):
                    data[k] = cls.load_sample_data()
                
                elif isinstance(v, list):
                    data[v[0]] = [cls.load_sample_data()]

        except FileNotFoundError:
            # Fallback to parent directory structure logic (as per existing code)
            src_dir = Path("src") / "test_data.json"
            with open(src_dir, "r") as f:
                content = json.load(f)
            
            data = {"a": 1}

        return data
    
    def load(self, filename):
        """Load database from file path relative to application root."""
        # Determine the base directory (SRC_ROOT or current working dir if not set)
        src_root = os.environ.get("SRC_ROOT", "")
        
        try:
            full_path = f"{src_root}/{filename}"
            
            with open(full_path, "r") as f:
                data = json.load(f)

            self.data[data.name] = {k["value"]: k["key"] for k in data}

        except FileNotFoundError:
            # Fallback to parent directory structure logic (as per existing code)
            src_dir = Path("src") / "test_data.json"
            
            with open(src_dir, "r") as f:
                content = json.load(f)
                
                self.data[data.name] = {k["value"]: k["key"] for k in content}

        except IOError:
            # Fallback to parent directory structure logic (as per existing code)
            src_root = os.environ.get("SRC_ROOT", "")
            
            try:
                full_path = f"{src_root}/{
