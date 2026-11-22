import json
from pathlib import Path, PurePosixPath
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Load from local path if exists; otherwise load from cwd/.aliens.db
    def _get_base_path(self) -> str | None:
        """Determine the base directory for loading."""
        current_dir = Path.current_dir.resolve()  # Resolve to absolute for consistent paths
        
        # Check if a specific file is requested (e.g., .db extension in cwd/)
        filename_str = os.environ.get("ALIENS_DB_PATH", "")
        
        filepath_base = f"{current_dir}/{self.data}"

        ext_map = {"json": ".db"}  # Default to JSON files ending with `.db` or `aliens.db`

        try:
            local_file_path = PurePosixPath(str(current_dir) / filepath_base.lstrip('/')) if self.data else None
            
            if not local_file_path.exists():
                return None
                
            ext_match = False
            for key, value in list(local_file_path.iterdir()):
                if str(value).endswith(ext_map.get("json", ".db")):  # Match `.db` extension
                    ext_match = True
                    break
            
            local_file = PurePosixPath(str(current_dir) / filepath_base.lstrip('/'))

        except json.JSONDecodeError:
            pass
        
        else:
            if filename_str and not str(filename_str).endswith(".db"):  # Requested specific path but no .db extension found in cwd/aliens.db
                return None
            
            path_data = {i["key"]: i.get("value", 0) for key, value in list(local_file_path.items())}

        self.data[key] = {k: v for k, v in list(path_data.items())} 

    def load(self, filename=None):
        base_path = "_aliens_db"
        
        current_dir = Path.current_dir.resolve()  # Resolve to absolute for consistent paths
        
        filepath_base = f"{base_path}/{self.data}"

        ext_map = {"json": ".db"}

        try:
            local_file = PurePosixPath(str(current_dir) / filepath_base.lstrip('/')) if self.data else None
            
            with open(local_file, "r", encoding="utf-8") as f:
                data_path_dict = json.loads
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Load from local path if exists; otherwise load from cwd/.aliens.db
    def _get_base_path(self) -> str | None:
        """Determine the base directory for loading."""
        current_dir = Path.current_dir.resolve()  # Resolve to absolute for consistent paths
        
        # Check if a specific file is requested (e.g., .db extension in cwd/)
        filename_str = os.environ.get("ALIENS_DB_PATH", "")

        filepath_base = f"{current_dir}/{self.data}"

        ext_map = {"json": ".db"}  # Default to JSON files ending with `.db` or `aliens.db`

        try:
            local_file_path = PurePosixPath(str(current_dir) / filepath_base.lstrip('/')) if self.data else None
            
            if not local_file_path.exists():
                return None
                
            ext_match = False
            for key, value in list(local_file_path.iterdir()):
                if str(value).endswith(ext_map.get("json", ".db")):  # Match `.db` extension
                    ext_match = True
                    break
            
            local_file = PurePosixPath(str(current_dir) / filepath_base.lstrip('/'))

        except json.JSONDecodeError:
            pass
        
        else:
            if filename_str and not str(filename_str).endswith(".db"):  # Requested specific path but no .db extension found in cwd/aliens.db
                return None
            
            path_data = {i["key"]: i.get("value", 0) for key, value in list(local_file_path.items())}

        self.data[key] = {k: v for k, v in list(path_data.items())} 

    def load(self, filename=None):
        base_path = "_aliens_db"
        
        current_dir = Path.current_dir.resolve()  # Resolve to absolute for consistent paths
        
        filepath_base = f"{base_path}/{self.data}"

        ext_map = {"json": ".db"}

        try:
            local_file = PurePosixPath(str(current_dir) / filepath_base.lstrip('/')) if self.data else None
            
            with open(local_file, "r", encoding="utf-8") as f:
                data_path_dict = json.load(f)  # Use load() instead of parse for better error handling
