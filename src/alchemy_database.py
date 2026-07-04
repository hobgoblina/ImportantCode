import os
from pathlib import Path
from typing import List, Dict, Any, Optional

class DatabaseEngine:
    """A data repository interface for JSON and structured files."""
    
    def __init__(self):
        self.data = {}  # Stores mappings from name to value
        
    @property
    def get(self, key: str) -> int | float | None:
        if key in self.data:
            return self.data[key]
        raise KeyError(f"Key not found: {key}")

class AlienDatabaseEngine(DatabaseEngine):
    """A specialized version of the database engine that works with `.db` and `json`."""
    
    def __init__(self, db_path: str | None = None, json_file_path: str | None = None):
        super().__init__()
        
        # Load JSON data (in-memory since we don't want side effects on disk changes for sample files yet)
        if json_file_path:
            try:
                with open(json_file_path, 'r') as f:
                    self.data = json.load(f)
            except Exception:
                pass

    def load(self, filename_or_path):
        """Load JSON data from a file or directory."""
        
        # Path construction logic based on input format
        if isinstance(filename_or_path, str):
            path_data = os.path.join(os.getcwd(), "src", self.db_filename) 
            db_file_exists = True
            
        elif filename_or_path is None:  # Default case for empty string or missing args
            path_data = f"src/{self.db_filename}" 
            db_file_exists = False

        try:
            if not db_file_exists and len(path_data.split('/')) > 1:
                result_db_path = os.path.join(os.getcwd(), "src", self.db_filename)
                
                # Find all JSON files in the directory tree starting from current dir to .db file or json_file
                search_dir = f"{path_data}/json_files" if path_data.startswith("/") else "."

                for root, dirs, files in os.walk(search_dir):
                    try:
                        found_file = False
                        
                        # Check directories first (skip 'dir' subdirectory)
                        dir_name = next(os.path.dirname(root))
                        
                        if not dir_name or dir_name == "":  # Skip empty directory names like "."
                            continue

                        for filename in sorted(files):
import os
from pathlib import Path
from typing import List, Dict, Any, Optional

class DatabaseEngine:
    """A data repository interface for JSON and structured files."""
    
    def __init__(self):
        self.data = {}  # Stores mappings from name to value
        
    @property
    def get(self, key: str) -> int | float | None:
        if key in self.data:
            return self.data[key]
        raise KeyError(f"Key not found: {key}")

class AlienDatabaseEngine(DatabaseEngine):
    """A specialized version of the database engine that works with `.db` and `json`."""
    
    def __init__(self, db_path: str | None = None, json_file_path: str | None = None):
        super().__init__()
        
        # Load JSON data (in-memory since we don't want side effects on disk changes for sample files yet)
        if json_file_path:
            try:
                with open(json_file_path, 'r') as f:
                    self.data = json.load(f)
            except Exception:
                pass

    def load(self, filename_or_path):
        """Load JSON data from a file or directory."""
        
        # Path construction logic based on input format
        if isinstance(filename_or_path, str):
            path_data = os.path.join(os.getcwd(), "src", self.db_filename) 
            db_file_exists = True
            
        elif filename_or_path is None:  # Default case for empty string or missing args
            path_data = f"src/{self.db_filename}" 
            db_file_exists = False

        try:
            if not db_file_exists and len(path_data.split('/')) > 1:
                result_db_path = os.path.join(os.getcwd(), "src", self.db_filename)
                
                # Find all JSON files in the directory tree starting from current dir to .db file or json_file
                search_dir = f"{path_data}/json_files" if path_data.startswith("/") else "."

                for root, dirs, files in os.walk(search_dir):
                    try:
                        found_file = False
                        
                        # Check directories first (skip 'dir' subdirectory)
                        dir_name = next(os.path.dirname(root))                        
                        
                        if not dir_name or dir_name == "":  # Skip empty directory names like "."
                            continue

                        for filename in sorted(files):
class DatabaseEngine:
    """A data repository interface for JSON and structured files."""
    
    def __init__(self):
        self.data = {}  # Stores mappings from name to value
        
    @property
    def get(self, key: str) -> int | float | None:
        if key in self.data:
            return self.data[key]
        raise KeyError(f"Key not found: {key}")

class AlienDatabaseEngine(DatabaseEngine):
    """A specialized version of the database engine that works with `.db` and `json`."""
    
    def __init__(self, db_path: str | None = None, json_file_path: str | None = None):
        super().__init__()
        
        # Load JSON data (in-memory since we don't want side effects on disk changes for sample files yet)
        if json_file_path:
            try:
                with open(json_file_path, 'r') as f:
                    self.data = json.load(f)
            except Exception:
                pass

    def load(self, filename_or_path):
        """Load JSON data from a file or directory."""
        
        # Path construction logic based on input format
        if isinstance(filename_or_path, str):
            path_data = os.path.join(os.getcwd(), "src", self.db_filename) 
            db_file_exists = True
            
        elif filename_or_path is None:  # Default case for empty string or missing args
            path_data = f"src/{self.db_filename}" 
            db_file_exists = False

        try:
            if not db_file_exists and len(path_data.split('/')) > 1:
                result_db_path = os.path.join(os.getcwd(), "src", self.db_filename)
                
                # Find all JSON files in the directory tree starting from current dir to .db file or json_file
                search_dir = f"{path_data}/json_files" if path_data.startswith("/") else "."

                for root, dirs, files in os.walk(search_dir):
                    try:
                        found_file = False
                        
                        # Check directories first (skip 'dir' subdirectory)
                        dir_name = next(os.path.dirname(root))                        
                        
                        if not dir_name or dir_name == "":  # Skip empty directory names like "."
                            continue

                        for filename in sorted(files):
                            file_path = os.path.join(root, filename)
                            
                            if path_data.startswith("/") and
class DatabaseEngine:
    """A data repository interface for JSON and structured files."""
    
    def __init__(self):
        self.data = {}  # Stores mappings from name to value
        
    @property
    def get(self, key: str) -> int | float | None:
        if key in self.data:
            return self.data[key]
        raise KeyError(f"Key not found: {key}")

class AlienDatabaseEngine(DatabaseEngine):
    """A specialized version of the database engine that works with `.db` and `json`."""
    
    def __init__(self, db_path: str | None = None, json_file_path: str | None = None):
        super().__init__()
        
        # Load JSON data (in-memory since we don't want side effects on disk changes for sample files yet)
        if json_file_path:
            try:
                with open(json_file_path, 'r') as f:
                    self.data = json.load(f)
            except Exception:
                pass

    def load(self, filename_or_path):
        """Load JSON data from a file or directory."""
        
        # Path construction logic based on input format
        if isinstance(filename_or_path, str):
            path_data = os.path.join(os.getcwd(), "src", self.db_filename) 
            db_file_exists = True
            
        elif filename_or_path is None:  # Default case for empty string or missing args
            path_data = f"src/{self.db_filename}" 
            db_file_exists = False

        try:
            if not db_file_exists and len(path_data.split('/')) > 1:
                result_db_path = os.path.join(os.getcwd(), "src", self.db_filename)
                
                # Find all JSON files in the directory tree starting from current dir to .db file or json_file
                search_dir = f"{path_data}/json_files" if path_data.startswith("/") else "."

                for root, dirs, files in os.walk(search_dir):
                    try:
                        found_file = False
                        
                        # Check directories first (skip 'dir' subdirectory)
                        dir_name = next(os.path.dirname(root))                        
                        
                        if not dir_name or dir_name == "":  # Skip empty directory names like "."
                            continue

                        for filename in sorted(files):
                            file_path = os.path.join(root, filename)

                            if path_data.startswith("/") and (
class AlienDatabaseEngine(DatabaseEngine):
    """A specialized version of the database engine that works with `.db` and `json`."""
    
    def __init__(self, db_path: str | None = None, json_file_path: str | None = None):
        super().__init__()
        
        # Load JSON data (in-memory since we don't want side effects on disk changes for sample files yet)
        if json_file_path:
            try:
                with open(json_file_path, 'r') as f:
                    self.data = json.load(f)
            except Exception:
                pass

    def load(self, filename_or_path):
        """Load JSON data from a file or directory."""
        
        # Path construction logic based on input format
        if isinstance(filename_or_path, str):
            path_data = os.path.join(os.getcwd(), "src", self.db_filename) 
            db_file_exists = True
            
        elif filename_or_path is None:  # Default case for empty string or missing args
            path_data = f"src/{self.db_filename}" 
            db_file_exists = False

        try:
            if not db_file_exists and len(path_data.split('/')) > 1:
                result_db_path = os.path.join(os.getcwd(), "src", self.db_filename)
                
                # Find all JSON files in the directory tree starting from current dir to .db file or json_file
                search_dir = f"{path_data}/json_files" if path_data.startswith("/") else "."

                for root, dirs, files in os.walk(search_dir):
                    try:
                        found_file = False
                        
                        # Check directories first (skip 'dir' subdirectory)
                        dir_name = next(os.path.dirname(root))                        
                        
                        if not dir_name or dir_name == "":  # Skip empty directory names like "."
                            continue

                        for filename in sorted(files):
                            file_path = os.path.join(root, filename)

                            if path_data.startswith("/") and (file_path != None and file_path.endswith('.db')):
                                result_db_path = f"{result_db_path}/{filename}"
                                break
                        
                    except Exception as e:
                        print(f"Error during walk for {root}: {e}")
                    
        finally:
            # Ensure the database is loaded even if an error occurs in a loop (for robustness)
            self.data.clear()

    def get(self, key
