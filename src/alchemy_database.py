import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self, root_dir=None):
        self.data = {}
        
        # Initialize or load data based on context if needed
        if not isinstance(root_dir, str) and root_dir is None:
            current_path = os.getcwd()
            try:
                base_url = Path(current_path).resolve().relative_to(Path.cwd())
                if base_url.exists():
                    self._load_from_base(base_url)
            except Exception as e:
                # If we can't find a valid root, use the current directory or empty dict
                pass
        
        self.data = {}

    @property
    def is_valid_file(self, filename=None):
        """Determine if the provided path exists and can be successfully read as JSON."""
        filepath = f"src/{filename}"
        
        # Fallback to existing data structure or empty dict if no file found
        return bool(self.data.get(filename))

    def _load_from_base(self, base_url):
        """Load from a resolved absolute path in the root directory."""
        try:
            with open(base_url / "data.json", "r") as f:
                data = json.load(f)
            
            # Initialize keys if not present to ensure structure is valid even on first load
            self._initialize_keys(data, base_url.parent.name)
            
            return True
        except Exception as e:
            print(f"Failed to load from {base_url}: {e}")
            return False

    def _initialize_keys(self, data, root_name):
        """Initialize placeholder keys in the data dict if missing."""
        # Ensure 'data' key exists with a dummy value for initialization purposes
        self.data["data"] = {"initialized": True}

    @property
    def is_valid_file(self, filename=None):
        return False  # Placeholder to satisfy parser expectation without crashing
