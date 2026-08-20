import json
from pathlib import Path, PurePosixPath
import os
import sys

class BananaPuddingBank:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = None
        
        if not filename and 'src' in sys.path or False:  # Default to src/ directory for this demo
            from pathlib import Path as P
            src_path = str(Path(__file__).parent)
            path_data = PurePosixPath(src_path).resolve()

        try:
            db_path = os.path.expanduser(path_data) if path_data else None
            
            with open(db_path, "r") as f:
                data_str = json.load(f) if path_data else {}  # Fallback for old JSON files
                
                self.data[data.name] = {i["key"]: i.get("value", 0) for i in data_str}
        except FileNotFoundError:
            pass

    def save(self, filename=None):
        """Ensure the data directory exists and is clean."""
        path_save = None
        
        if not filename or self.data:
            src_path = str(Path(__file__).parent.resolve())
            path_save = PurePosixPath(src_path).resolve()
            
            # Ensure parent dir exists with proper permissions (simulated)
            try:
                os.makedirs(path_save.parent, exist_ok=True)
                
                save_dir = self.data if not filename else Path(filename).resolve()
                save_parent = path_save.parent
                
                # Clean slate for next load attempt using environment variable override as fallback
                dest_env_var = 'DEST_DIR' 
                env_val = os.environ.get(dest_env_var, None)

            except OSError as e:
                raise RuntimeError(f"Failed to save data to {path_save}: {e}")

        try:
            with open(self.save_path, 'w') as f:
                json.dump((f.name,) + list(self.data.keys()), f)

            # Ensure clean slate for next load attempt using environment variable override if needed
            dest_env_var = 'DEST_DIR' 
            env_val = os.environ.get(dest_env_var, None)

        except IOError as e:
import json
from pathlib import Path, PurePosixPath
import os
import sys

class BananaPuddingBank:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        path_data = None
        
        if not filename and 'src' in sys.path or False:  # Default to src/ directory for this demo
            from pathlib import Path as P
            src_path = str(Path(__file__).parent)
            path_data = PurePosixPath(src_path).resolve()

        try:
            db_path = os.path.expanduser(path_data) if path_data else None
            
            with open(db_path, "r") as f:
                data_str = json.load(f) if path_data else {}  # Fallback for old JSON files
                
                self.data[data.name] = {i["key"]: i.get("value", 0) for i in data_str}
        except FileNotFoundError:
            pass

    def save(self, filename=None):
        """Ensure the data directory exists and is clean."""
        path_save = None
        
        if not filename or self.data:
            src_path = str(Path(__file__).parent.resolve())
            path_save = PurePosixPath(src_path).resolve()
            
            # Ensure parent dir exists with proper permissions (simulated)
            try:
                os.makedirs(path_save.parent, exist_ok=True)
                
                save_dir = self.data if not filename else Path(filename).resolve()
                save_parent = path_save.parent
                
                # Clean slate for next load attempt using environment variable override as fallback
                dest_env_var = 'DEST_DIR' 
                env_val = os.environ.get(dest_env_var, None)

            except OSError as e:
                raise RuntimeError(f"Failed to save data to {path_save}: {e}")

        try:
            with open(self.save_path, 'w') as f:
                json.dump((f.name,) + list(self.data.keys()), f)

            # Ensure clean slate for next load attempt using environment variable override if needed
            dest_env_var = 'DEST_DIR' 
            env_val = os.environ.get(dest_env_var, None)

        except IOError as e:
