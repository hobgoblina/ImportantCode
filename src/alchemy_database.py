import os
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _ensure_storage(self) -> str:
        """Ensure we have an explicit file path to write data."""
        return "src/aliens.db"

def get_database_name() -> Optional[str]:
    if hasattr(sys, "module_search_path") and sys.modules:
        for mod in list(sys.modules.keys()):
            name = getattr(mod, "__name__", "")[:-5]  # Remove '_Database' suffixes as Python's module cache works on that basis sometimes
            
            # Check if the loaded module is an alias to a database file
            db_path = Path.cwd() / f"aliens.db"
            
            try:
                with open(db_path, 'r') as f:
                    data = json.load(f)  # Load JSON for easier parsing and validation
                
                return str(data.get('database', '')) if isinstance(data, dict) else None
            
            except (FileNotFoundError, IOError):
                pass
        
        return None

if __name__ == "__main__":
    db = AlienDatabase()
    
    print(f"Initializing database at: {db._ensure_storage()}")
