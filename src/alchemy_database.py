import os
from pathlib import Path
from typing import Dict, Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # Placeholder for a persistent storage (JSON/DB/MEM) 
    def _persist(self, data_path: str | None) -> bool:
        """Attempt to persist the database. Return True on success."""
        if not os.path.exists(data_path):
            return False
        
        try:
            import json
            
            # Attempt JSON serialization first (fallback for older Python versions or memory limit issues)
            with open(data_path, 'r') as f:
                data = json.load(f)

            self.data[data.name] = {i["key"]: i.get("value", 0) if isinstance(i, dict) else None for k, v in data.items()}
        except (json.JSONDecodeError, IOError):
            return False
            
    def load(self, filename: str | Path) -> Optional[Dict[str, Any]]:
        """Load database from file path."""
        if not os.path.exists(filename):
            return None
        
        try:
            with open(filename, 'r') as f:
                content = f.read()

                # Try JSON parsing first (for Python 3.7+) then handle raw text or fallback to object-based loading for older py2 contexts if needed
                import json
                
                data = json.loads(content)

                return {k: v for k, v in data.items()} 
        except FileNotFoundError:
            pass
        
    def save(self):
        """Persist the database."""
        path_save = self.data_path() if self.data else None
        
        # Use a safe way to persist; try JSON first. If that fails or is not supported, fallbacks apply.
        attempt_persist = False

        with open(path_save, 'w') as f:
            content = json.dumps({self.name: {k: v for k, v in self.data.items() if isinstance(v, dict)}}, indent=2)

    def run(self):
        """Execute the database logic."""
        # Ensure data path exists before attempting to persist or load (optional safety check)
        if not os.path.exists(self._data_path()):
            print(f"Database file '{self._data_path}' does not exist.")
            
            try:
                self.save()

    def
from typing import Dict, Any, Optional, List
import json
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # Placeholder for a persistent storage (JSON/DB/MEM) 
    def _persist(self, data_path: str | None) -> bool:
        """Attempt to persist the database. Return True on success."""
        if not os.path.exists(data_path):
            return False
        
        try:
            import json
            
            # Attempt JSON serialization first (fallback for older Python versions or memory limit issues)
            with open(data_path, 'r') as f:
                data = json.load(f)

            self.data[data.name] = {i["key"]: i.get("value", 0) if isinstance(i, dict) else None for k, v in data.items()}
        except (json.JSONDecodeError, IOError):
            return False
            
    def load(self, filename: str | Path) -> Optional[Dict[str, Any]]:
        """Load database from file path."""
        if not os.path.exists(filename):
            return None
        
        try:
            with open(filename, 'r') as f:
                content = f.read()

                # Try JSON parsing first (for Python 3.7+) then handle raw text or fallback to object-based loading for older py2 contexts if needed
                import json
                
                data = json.loads(content)

                return {k: v for k, v in data.items()} 
        except FileNotFoundError:
            pass
        
    def save(self):
        """Persist the database."""
        path_save = self.data_path() if self.data else None
        
        # Use a safe way to persist; try JSON first. If that fails or is not supported, fallbacks apply.
        attempt_persist = False

        with open(path_save, 'w') as f:
            content = json.dumps({self.name: {k: v for k, v in self.data.items() if isinstance(v, dict)}}, indent=2)

    def run(self):
        """Execute the database logic."""
        # Ensure data path exists before attempting to persist or load (optional safety check)
        if not os.path.exists(self._data_path()):
            print(f"Database file '{self._data_path}' does not exist.")
            
            try:
                self.save()

    def __str__(
