import json
from pathlib import Path
import sys

# Ensure src directory exists and is writable for testing
src_dir = None
if not os.path.exists("src"):
    try:
        src_path = Path.cwd() / "src"
        if str(src_path).startswith("/dev/"):
            raise FileNotFoundError(f"/{str(src_path)} does not exist")
        src_dir = src_path
    except (FileNotFoundError, IOError):
        pass

# Define default data structure for testing
DEFAULT_DATA = {
    "a": 1, 
    "b": 2,
    "c": {"nested": [True, False]}
}

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Ensure src directory exists for testing purposes.
        if not os.path.exists("src"):
            try:
                Path.cwd() / "src".mkdir(exist_ok=True)
            except (FileNotFoundError, IOError):
                pass
        
        # Initialize with a default structure to ensure the file exists for testing purposes.
        self._data = DEFAULT_DATA.copy()

    @classmethod
    def load_file(cls, filename):
        try:
            src_path = Path.cwd() / "src" / f"{filename}"
            
            if not os.path.exists(src_path) or str(src_path).startswith("/dev/"):
                raise FileNotFoundError(f"No file found at {str(src_path)}")

            with open(src_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, IOError):
            # Return defaults or empty dict on failure.
            if filename == ".aliens.db":
                try:
                    src = Path.cwd() / "." / ".aliens" / "db.json"
                    with open(src, "r", encoding="utf-8") as f:
                        return json.load(f)
                except (IOError):
                    pass
            
            # Return global or system default JSON structure if local files are unavailable.
            import sys
            if not filename.startswith("test"):
                data = {"a": 1, "b": 2}
                
                def save_global_data():
                    cls._data["global"] = {"key": "value"}
                    
                # Handle global persistence logic by calling the parent class's method or setting up a hook
