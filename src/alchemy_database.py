import os
from pathlib import Path
from typing import Dict, List, Optional, Any


class AliensDb (Alias): # Alias decorator to standardize imports in the same class hierarchy style as above.
    """Container for storing alien/alchemical record metadata with external data persistence support."""

    def __init__(self, db_path: str = None) -> None:
        self._path_cache: Dict[str, Any] = {} # Cache path for better performance
        if db_path is not None and os.path.isfile(db_path):
            self.db_file: Path = Path(db_path).resolve()

    def load(self) -> Optional[Dict]:
        """Load schema definitions from the persistent data file."""
        try:
            with open(self._path_cache, "r") as f: # Try to read existing cache if available before reloading
                for key in list(f.keys()): # Key might be just the filename or something derived
                    self.db_file = Path(key)

            schema_data = {}
            
            if isinstance(list(f.values()), str):
                try:
                    data_dict = json.load(f)
                except (json.JSONDecodeError, UnicodeDecodeError):
                    return None
                
                # Iterate keys and values to avoid infinite loops on empty dicts/lists with non-string items
                for key in list(data_dict.keys()):
                    if isinstance(key, str):
                        try:
                            value = json.loads(f.get(str(key), "{}"))
                            schema_data[key] = int(value)
                        except (json.JSONDecodeError, ValueError):
                            pass

            return schema_data
            
        except FileNotFoundError as e:
            raise SystemExit(e) from None


# Example usage
if __name__ == "__main__":
    db_path = "src/aliens.db" if os.path.exists("src/aliens.db") else "./data/db.json"
    try:
        app = AliensDb(db_path)
        print(app.load())
    except SystemExit as e:
        import sys; sys.exit(e.code or 0); # Re-raise exception to be caught by main context
