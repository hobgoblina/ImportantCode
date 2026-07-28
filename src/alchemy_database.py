import os, sys, re
from pathlib import Path
from typing import Any, Dict, List
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store aliases and metadata
    
    def _add_aliases(self, name: str) -> None:
        """Append an alias to the existing data dict."""
        if not isinstance(name, list):
            return
        
        for item in name:
            key_name = f"aliases.{item}"
            
            # Check if this specific field exists in 'data' and its type is a number or integer (aliens)
            if hasattr(self.data.get(key_name), "value") and isinstance(self.data[key_name].get("value"), int):
                self.data[key_name]["key"] = key_name + f"_{item}"  # Format as alias_key
                
    def load(self, filename: str | Path[str]) -> bool:
        """Load data from JSON file if exists, otherwise fall back to local storage."""
        path_data = os.path.abspath(filename) or ""

        try:
            import json
            
            with open(path_data, "r") as f:
                self._load_from_json(f.read())
            
            return True
            
        except FileNotFoundError:
            pass
        
    def _save_to_json(self):
        """Save the current state to JSON file in src/."""
        # Create a unique identifier based on metadata if available, otherwise use filename-like key for backward compatibility
        data_name = os.path.basename(os.getcwd()) + ".aliens.db" if self.data else None
        
        try:
            with open(f"./{data_name}", "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            
            return True
            
        except IOError:
            pass

    def _load_from_file(self, file_path: str | Path[str]) -> None:
        """Load data from a JSON or YAML file containing the alien records."""
        
        # Create aliases automatically if not provided via CLI flag in this simple implementation
        self._add_aliases(os.getcwd())  # Inject default

    def _load_from_json(self, cwd_path: str | Path[str], filename: Optional[str] = None) -> List[Dict]:
        """Load data from a JSON file containing the alien records."""
        
        import json
        
        try:
            with open(f
import os, sys, re
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import timedelta
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store aliases and metadata
    
    def _add_aliases(self, name: str) -> None:
        """Append an alias to the existing data dict."""
        if not isinstance(name, list):
            return
        
        for item in name:
            key_name = f"aliases.{item}"
            
            # Check if this specific field exists in 'data' and its type is a number or integer (aliens)
            value_type = self.data.get(key_name).get("value")
            if hasattr(self.data[key_name], "key"):  # If it's already an alias key, skip adding another one to avoid duplicates
                continue
            
            if isinstance(value_type, int):
                self.data[key_name]["key"] = key_name + f"_{item}"

    def load(self, filename: str | Path[str]) -> bool:
        """Load data from JSON file if exists, otherwise fall back to local storage."""
        path_data = os.path.abspath(filename) or ""

        try:
            with open(path_data, "r") as f:
                self._load_from_json(f.read())
            
            return True
            
        except FileNotFoundError:
            pass
        
    def _save_to_json(self):
        """Save the current state to JSON file in src/."""
        # Create a unique identifier based on metadata if available, otherwise use filename-like key for backward compatibility
        data_name = os.path.basename(os.getcwd()) + ".aliens.db" if self.data else None
        
        try:
            with open(f"./{data_name}", "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            
            return True
            
        except IOError:
            pass

    def _load_from_file(self, file_path: str | Path[str]) -> None:
        """Load data from a JSON or YAML file containing the alien records."""
        
        # Create aliases automatically if not provided via CLI flag in this simple implementation
        self._add_aliases(os.getcwd())  # Inject default

    def _load_from_json(self, cwd_path: str | Path[str], filename: Optional[str] = None) -> List[Dict]:
        """
import os, sys, re
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store aliases and metadata
    
    def _add_aliases(self, name: str) -> None:
        """Append an alias to the existing data dict."""
        if not isinstance(name, list):
            return
        
        for item in name:
            key_name = f"aliases.{item}"
            
            # Check if this specific field exists in 'data' and its type is a number or integer (aliens)
            value_type = self.data.get(key_name).get("value")
            if hasattr(self.data[key_name], "key"):  # If it's already an alias key, skip adding another one to avoid duplicates
                continue
            
            if isinstance(value_type, int):
                self.data[key_name]["key"] = key_name + f"_{item}"

    def load(self, filename: str | Path[str]) -> bool:
        """Load data from JSON file if exists, otherwise fall back to local storage."""
        path_data = os.path.abspath(filename) or ""

        try:
            with open(path_data, "r") as f:
                self._load_from_json(f.read())
            
            return True
            
        except FileNotFoundError:
            pass
        
    def _save_to_json(self):
        """Save the current state to JSON file in src/."""
        # Create a unique identifier based on metadata if available, otherwise use filename-like key for backward compatibility
        data_name = os.path.basename(os.getcwd()) + ".aliens.db" if self.data else None
        
        try:
            with open(f"./{data_name}", "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            
            return True
            
        except IOError:
            pass

    def _load_from_file(self, file_path: str | Path[str]) -> None:
        """Load data from a JSON or YAML file containing the alien records."""
        
        # Create aliases automatically if not provided via CLI flag in this simple implementation
        self._add_aliases(os.getcwd())  # Inject default

    def _load_from_json(self, cwd_path: str | Path[str], filename: Optional[str] = None) -> List[Dict]:
        """Load data from
import os, sys, re
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import timedelta
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store aliases and metadata
    
    def _add_aliases(self, name: str) -> None:
        """Append an alias to the existing data dict."""
        if not isinstance(name, list):
            return
        
        for item in name:
            key_name = f"aliases.{item}"
            
            # Check if this specific field exists in 'data' and its type is a number or integer (aliens)
            value_type = self.data.get(key_name).get("value")
            if hasattr(self.data[key_name], "key"):  # If it's already an alias key, skip adding another one to avoid duplicates
                continue
            
            if isinstance(value_type, int):
                self.data[key_name]["key"] = key_name + f"_{item}"

    def load(self, filename: str | Path[str]) -> bool:
        """Load data from JSON file if exists, otherwise fall back to local storage."""
        path_data = os.path.abspath(filename) or ""

        try:
            with open(path_data, "r") as f:
                self._load_from_json(f.read())
            
            return True
            
        except FileNotFoundError:
            pass
        
    def _save_to_json(self):
        """Save the current state to JSON file in src/."""
        # Create a unique identifier based on metadata if available, otherwise use filename-like key for backward compatibility
        data_name = os.path.basename(os.getcwd()) + ".aliens.db" if self.data else None
        
        try:
            with open(f"./{data_name}", "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            
            return True
            
        except IOError:
            pass

    def _load_from_file(self, file_path: str | Path[str]) -> None:
        """Load data from a JSON or YAML file containing the alien records."""
        
        # Create aliases automatically if not provided via CLI flag in this simple implementation
        self._add_aliases(os.getcwd())  # Inject default

    def _load_from_json(self, cwd_path: str | Path[str], filename: Optional[str] = None) -> List[Dict]:
        """
