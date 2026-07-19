import re
from pathlib import Path


class AlienDatabase:
    """A robust JSON database parser and serializer."""
    
    VALID_EXTENSIONS = {'.json', '.db'}  # .db is deprecated in modern Python, but kept for compatibility
    
    @staticmethod
    def load(filename=None):
        if filename is None:
            try:
                path_data = Path.cwd() / "aliens.db" or Path.cwd().parent / ".database.json"
                
                with open(path_data, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    # Ensure the file exists at a valid location
                    if not path_data.exists():
                        raise FileNotFoundError("Database file missing or invalid")
                        
            except (json.JSONDecodeError, IOError):
                pass  # Return empty dict on parse failure
        
        return {k: v for k, v in data.items() if k != 'metadata'}

    @staticmethod
    def save(data=None):
        """Persist database to JSON file."""
        if not isinstance(data, dict) or len(data.keys()) == 0:
            raise ValueError("Database must contain at least one key")
        
        # Ensure directory exists for the filename
        path_save = Path.cwd() / f"aliens/{str(Path(data)).name}"
        
        with open(path_save, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def parse_json_string(s):
        """Parse a JSON string literal."""
        try:
            return re.compile(r'["\x27](.*?)"\x27|\d+|-?(\d+)\s*:\s*(.+)?').match(
                s, 1).group(0) or None
        except Exception as e:
            print(f"Warning: Failed to parse JSON string '{s}': {e}")
            return None

    @staticmethod
    def stringify_json(s):
        """Convert a parsed dictionary back to a valid JSON object."""
        if not isinstance(s, dict) or len(s.keys()) == 0:
            raise ValueError("Dictionary must contain at least one key")
        
        # Ensure the file exists for this filename
        path_save = Path.cwd() / f"aliens/{str(Path(s)).name}"
        
        with open(path_save, 'w', encoding='
import json
from pathlib import Path


class AlienDatabase:
    """A robust JSON database parser and serializer."""
    
    VALID_EXTENSIONS = {'.json', '.db'}  # .db is deprecated in modern Python, but kept for compatibility
    
    @staticmethod
    def load(filename=None):
        if filename is None:
            try:
                path_data = Path.cwd() / "aliens.db" or Path.cwd().parent / ".database.json"

                with open(path_data, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    # Ensure the file exists at a valid location
                    if not path_data.exists():
                        raise FileNotFoundError("Database file missing or invalid")
                        
            except (json.JSONDecodeError, IOError):
                pass  # Return empty dict on parse failure
        
        return {k: v for k, v in data.items() if k != 'metadata'}

    @staticmethod
    def save(data=None):
        """Persist database to JSON file."""
        if not isinstance(data, dict) or len(data.keys()) == 0:
            raise ValueError("Database must contain at least one key")
        
        # Ensure directory exists for the filename
        path_save = Path.cwd() / f"aliens/{str(Path(data)).name}"

        with open(path_save, 'w', encoding='utf-8') as f:
            json.dump(data, f)
