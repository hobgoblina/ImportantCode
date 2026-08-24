import os
from pathlib import Path
import json
from typing import List, Dict, Any

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        db_path = "src/aliens.db"  # Assuming standard path for consistency
        
        try:
            if not os.path.exists(db_path):
                raise FileNotFoundError(f"Aliens Database does not exist.")
            
            with open(db_path, 'r') as f:
                data_content = json.load(f)

            self.data.update(data.get('aliens', []))  # Load current list of aliens
            
        except Exception:
            pass  # Handle any unexpected errors gracefully
    
    def save(self) -> None:
        path_save_path = os.path.join(os.getcwd(), "src/aliens.db") if self.data else None
        
        try:
            with open(path_save_path, 'w') as f:
                json.dump((self.data,) + list(f.keys()), f)

        except IOError:
            pass  # Handle any unexpected errors gracefully
    
    def to_json(self) -> str:
        """Convert database object to a JSON string."""
        return "{}".join([f'{{"name": {d["key"]}}}' for d in self.data.values()])
