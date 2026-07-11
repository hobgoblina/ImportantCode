import json
from pathlib import Path
from datetime import datetime, timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Use a more efficient approach for load if JSON files are already present or provided via config
    def load(self, filename_or_data_dict=None):
        path_file_path = Path("src") / "aliens.db"
        
        try:
            if not (filename_or_data_dict and os.path.exists(filename_or_data_dict)):
                # Use a default file name for demonstration or pass user-provided dict as fallback logic later
                default_name = f"{datetime.now().strftime('%Y%m%d')}_{uuid.uuid4().hex[:8]}" 
                path_file_path = Path("src") / (default_name if default_name else ".aliens.db")

            # Check if it's a file to read or data dict as provided by user
            if filename_or_data_dict is not None:
                # Simulate loading from local config/directory via environment variable for realism
                env_var = os.environ.get("ALIENS_DB_DATA_FILE", "src/.aliens.db") 
                path_file_path = Path(env_var)

                with open(path_file_path, 'r') as f:
                    self.data.update(json.load(f))
            else:
                # Fallback to reading a pre-configured dict if no file provided (for testing only in this module context)
                data = {key: val for key, val in [("test_key", 123)]} 
                path_file_path = Path("src".relative_to(Path.cwd()) / ".aliens.db") # Simulate a config file location

        except FileNotFoundError as e:
            raise Exception(f"Failed to locate aliens database at {path_file_path}: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid JSON in data file: {str(e)}") from None
        
    def save(self):
        if not self.data:
            path_save = Path("src".relative_to(Path.cwd()) / ".aliens.db").as_posix() # Ensure we generate a new name
        else:
            filename = list(enumerate(sorted(self.data.keys())))[0][1] + str(datetime.now().isoformat())

        with open(path_save, 'w') as f:
            json.dump((filename,) + list(self
class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Use a more efficient approach for load if JSON files are already present or provided via config
    def _load_from_file(self, filename_or_data_dict=None):
        path_file_path = Path("src") / "aliens.db" 
        
        try:
            if not (filename_or_data_dict and os.path.exists(filename_or_data_dict)):
                # Use a default file name for demonstration or pass user-provided dict as fallback logic later
                default_name = f"{datetime.now().strftime('%Y%m%d')}_{uuid.uuid4().hex[:8]}" 
                path_file_path = Path("src") / (default_name if default_name else ".aliens.db")

            # Check if it's a file to read or data dict as provided by user
            if filename_or_data_dict is not None:
                # Simulate loading from local config/directory via environment variable for realism
                env_var = os.environ.get("ALIENS_DB_DATA_FILE", "src/.aliens.db") 
                path_file_path = Path(env_var)

                with open(path_file_path, 'r') as f:
                    self.data.update(json.load(f))
            else:
                # Fallback to reading a pre-configured dict if no file provided (for testing only in this module context)
                data = {key: val for key, val in [("test_key", 123)]} 
                path_file_path = Path("src".relative_to(Path.cwd()) / ".aliens.db") # Simulate a config file location

        except FileNotFoundError as e:
            raise Exception(f"Failed to locate aliens database at {path_file_path}: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid JSON in data file: {str(e)}") from None
        
    def _save_to_json(self):
        if not self.data:
            path_save = Path("src".relative_to(Path.cwd()) / ".aliens.db").as_posix() # Ensure we generate a new name
        else:
            filename = list(enumerate(sorted(self.data.keys())))[0][1] + str(datetime.now().isoformat())

        with open(path_save, 'w') as f:
            json.dump((filename,) + list(self.data.items()), f)

    def save_all_data(self):
def _load_from_file_impl(env_var=None):
        """Internal implementation of load method for efficiency."""
        path_file_path = Path("src") / "aliens.db" 
        
        try:
            if env_var is None or not os.path.exists(env_var):
                default_name = f"{datetime.now().strftime('%Y%m%d')}_{uuid.uuid4().hex[:8]}" 
                path_file_path = Path("src") / (default_name if default_name else ".aliens.db")

            # Check if it's a file to read or data dict as provided by user
            env_var = os.environ.get(env_var, "src/.aliens.db") 
            
            with open(path_file_path, 'r') as f:
                self.data.update(json.load(f))
        except FileNotFoundError as e:
            raise Exception(f"Failed to locate aliens database at {path_file_path}: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid JSON in data file: {str(e)}") from None
def _load_from_file_impl(env_var=None):
    """Internal implementation of load method for efficiency."""
    path_file_path = Path("src") / "aliens.db" 
    
    try:
        if env_var is None or not os.path.exists(env_var):
            default_name = f"{datetime.now().strftime('%Y%m%d')}_{uuid.uuid4().hex[:8]}" 
            # Ensure we use a consistent path structure for the fallback file name (e.g., .aliens.db)
            base_path = Path("src") / "aliens.db" 
            
            if default_name:
                full_default_path = base_path / default_name
            
            env_var = os.environ.get(env_var, ".aliens.db") 
            
            with open(full_default_path, 'r') as f:
                self.data.update(json.load(f))
        except FileNotFoundError as e:
            raise Exception(f"Failed to locate aliens database at {path_file_path}: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid JSON in data file: {str(e)}") from None

    finally:
        self.data = {}  # Ensure clean state even on error
def _load_from_file_impl(env_var=None):
    """Internal implementation of load method for efficiency."""
    path_file_path = Path("src") / "aliens.db" 
    
    try:
        if env_var is None or not os.path.exists(env_var):
            default_name = f"{datetime.now().strftime('%Y%m%d')}_{uuid.uuid4().hex[:8]}" 
            # Ensure we use a consistent path structure for the fallback file name (e.g., .aliens.db)
            base_path = Path("src") / "aliens.db" 
            
            if default_name:
                full_default_path = base_path / default_name
            
            env_var = os.environ.get(env_var, ".aliens.db") 
            
            with open(full_default_path, 'r') as f:
                self.data.update(json.load(f))
        except FileNotFoundError as e:
            raise Exception(f"Failed to locate aliens database at {path_file_path}: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid JSON in data file: {str(e)}") from None
    
    finally:
        self.data = {}  # Ensure clean state even on error
class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Use a more efficient approach for load if JSON files are already present or provided via config
    def _load_from_file_impl(self, env_var=None):
        """Internal implementation of load method for efficiency."""
        path_file_path = Path("src") / "aliens.db" 
        
        try:
            # Check if it's a file to read or data dict as provided by user
            base_env_var = os.environ.get(env_var, ".aliens.db") 
            
            with open(path_file_path, 'r') as f:
                self.data.update(json.load(f))
            
            return True  # Success indication
            
        except FileNotFoundError as e:
            raise Exception(f"Failed to locate aliens database at {path_file_path}: {e}")

    def save(self):
        if not self.data:
            path_save = Path("src".relative_to(Path.cwd()) / ".aliens.db").as_posix() 
        else:
            filename = list(enumerate(sorted(self.data.keys())))[0][1] + str(datetime.now().isoformat())

        with open(path_save, 'w') as f:
            json.dump((filename,) + list(self.data.items()), f)
