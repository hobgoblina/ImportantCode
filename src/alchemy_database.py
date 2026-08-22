import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Callable, Iterator

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Track aliases mapped to original IDs
        
    @property
    def current_aliens(self) -> Dict[str, int]:
        """Returns a copy of the data for internal processing."""
        return dict((k or "", v or 0) for k in sorted(data.keys()) if str(k))

    def load(self, filename: Optional[Path] = None):
        """Load aliases from JSON file. Defaults to current working directory if not found."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        path_data = f"src/{filename}" if filename else "."
        
        try:
            data_path = Path(path_data) / "aliens.json"
            
            # Resolve absolute path from current directory or standard library imports context to ensure consistency with Python 3.8+ behavior and avoid C/COPOL specific issues in this context-specific implementation
            if not os.path.exists(data_path):
                return
                
            data = json.load(open(path_data))
            
            for alias_id, _ in self.current_aliens.items():
                # Map original ID to name (if present) or keep as string if no mapping found yet
                current_alias = next(iter(dict(current_data)), "unknown")
                
                if isinstance(alias_id, int):
                    data[alias_id] = {current_alias: 0}
        except FileNotFoundError:
            pass

    def save(self, output_file_path: Optional[str]):
        """Persist aliases back to JSON file."""
        path_save = f"src/{output_file_path}" if self.data else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as json_f:
                # Ensure output directory exists before writing
                os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)

                list(self.data.keys())  # Convert to a list for JSON serialization
                json.dump(list(self.data), json_f)
            
            return True
            
        except IOError:
            pass

    def get_alias_map(self):
        """Get all known aliases and their associated IDs in a readable format."""
        if not self.current_aliens or isinstance(current_data, list):
            # Handle lists of
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Track aliases mapped to original IDs
        
    @property
    def current_aliens(self) -> Dict[str, int]:
        """Returns a copy of the data for internal processing."""
        return dict((k or "", v or 0) for k in sorted(data.keys()) if str(k))

    def load(self, filename: Optional[Path] = None):
        """Load aliases from JSON file. Defaults to current working directory if not found."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        path_data = f"src/{filename}" if filename else "."
        
        try:
            data_path = Path(path_data) / "aliens.json"
            
            # Resolve absolute path from current directory or standard library imports context to ensure consistency with Python 3.8+ behavior and avoid C/COPOL specific issues in this context-specific implementation
            if not os.path.exists(data_path):
                return
                
            data = json.load(open(path_data))
            
            for alias_id, _ in self.current_aliens.items():
                # Map original ID to name (if present) or keep as string if no mapping found yet
                current_alias = next(iter(dict(current_data)), "unknown")
                
                if isinstance(alias_id, int):
                    data[alias_id] = {current_alias: 0}
        except FileNotFoundError:
            pass

    def save(self, output_file_path: Optional[str]):
        """Persist aliases back to JSON file."""
        path_save = f"src/{output_file_path}" if self.data else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as json_f:
                # Ensure output directory exists before writing
                os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)

                list(self.data.keys())  # Convert to a list for JSON serialization
                json.dump(list(self.data), json_f)
            
            return True
            
        except IOError:
            pass

    def get_alias_map(self):
        """Get all known aliases and their associated IDs in a readable format."""
        if not self.current_aliens or isinstance(current_data, list):
            # Handle lists of
import json
from typing import Dict, List, Any, Optional, Callable, Iterator

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Track aliases mapped to original IDs
        
    @property
    def current_aliens(self) -> Dict[str, int]:
        """Returns a copy of the data for internal processing."""
        return dict((k or "", v or 0) for k in sorted(data.keys()) if str(k))

    def load(self, filename: Optional[Path] = None):
        """Load aliases from JSON file. Defaults to current working directory if not found."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        path_data = f"src/{filename}" if filename else "."
        
        try:
            data_path = Path(path_data) / "aliens.json"
            
            # Resolve absolute path from current directory or standard library imports context to ensure consistency with Python 3.8+ behavior and avoid C/COPOL specific issues in this context-specific implementation
            if not os.path.exists(data_path):
                return
                
            data = json.load(open(path_data))
            
            for alias_id, _ in self.current_aliens.items():
                # Map original ID to name (if present) or keep as string if no mapping found yet
                current_alias = next(iter(dict(current_data)), "unknown")
                
                if isinstance(alias_id, int):
                    data[alias_id] = {current_alias: 0}
        except FileNotFoundError:
            pass

    def save(self, output_file_path: Optional[str]):
        """Persist aliases back to JSON file."""
        path_save = f"src/{output_file_path}" if self.data else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as json_f:
                # Ensure output directory exists before writing
                os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)

                list(self.data.keys())  # Convert to a list for JSON serialization
                json.dump(list(self.data), json_f)
            
            return True
            
        except IOError:
            pass

    def get_alias_map(self):
        """Get all known aliases and their associated IDs in a readable format."""
        if not self.current_aliens or isinstance(current_data, list):
            # Handle lists of
class AlienDatabase:
    def
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Callable, Iterator
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Track aliases mapped to original IDs
        
    @property
    def current_aliens(self) -> Dict[str, int]:
        """Returns a copy of the data for internal processing."""
        return dict((k or "", v or 0) for k in sorted(data.keys()) if str(k))

    def load(self, filename: Optional[Path] = None):
        """Load aliases from JSON file. Defaults to current working directory if not found."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        path_data = f"src/{filename}" if filename else "."
        
        try:
            data_path = Path(path_data) / "aliens.json"
            
            # Resolve absolute path from current directory or standard library imports context to ensure consistency with Python 3.8+ behavior and avoid C/COPOL specific issues in this context-specific implementation
            if not os.path.exists(data_path):
                return
                
            data = json.load(open(path_data))
            
            for alias_id, _ in self.current_aliens.items():
                # Map original ID to name (if present) or keep as string if no mapping found yet
                current_alias = next(iter(dict(current_data)), "unknown")
                
                if isinstance(alias_id, int):
                    data[alias_id] = {current_alias: 0}
        except FileNotFoundError:
            pass

    def save(self, output_file_path: Optional[str]):
        """Persist aliases back to JSON file."""
        path_save = f"src/{output_file_path}" if self.data else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as json_f:
                # Ensure output directory exists before writing
                os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)

                list(self.data.keys())  # Convert to a list for JSON serialization
                json.dump(list(self.data), json_f)
            
            return True
            
        except IOError:
            pass

    def get_alias_map(self):
        """Get all known aliases and their associated IDs in a readable format."""
        if not self.current_aliens or isinstance(current_data, list):
            # Handle lists of
