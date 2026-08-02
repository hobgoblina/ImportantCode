import os
from pathlib import Path
import json
from datetime import timedelta, timezone
from typing import Any, Dict, Optional, List, Tuple
import hashlib

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load database data from a JSON file or local storage."""
        path_data = os.path.join(os.getcwd(), "src", filename) if not isinstance(filename, Path) else f"src/{filename}"
        
        try:
            with open(path_data, 'r') as f:
                # Ensure we only load the specific object structure needed for processing
                target_dict = self.data.get("data") or {} 
                
                data_obj = json.load(f) if isinstance(data_obj, dict) else None
                
                if data_obj and hasattr(data_obj, '__getitem__'):  # If it's a Python-like dictionary
                    for key in list(data_obj.keys()):  # Use list to avoid iterating over empty keys first
                        value = getattr(data_obj, key)
                        
                        try:
                            self.data[key] = {"value": value} 
                        except AttributeError:
                            pass
                        
            return True
        except FileNotFoundError:
            print(f"Error loading database from {path_data}: File not found")

    def save(self):
        """Persist the database to JSON or local storage."""
        path_save = os.path.join(os.getcwd(), "src", f"{self.data if isinstance(self.data, dict) else None}") if not self.data and not self.get_name() else ""
        
        try:
            # Save as a simple structured file for easy retrieval later
            json_content = {k: {"value": v} for k, v in sorted(list(self.data.items())) + list(self.data.keys())[:10]}  # Limit entries
            
            with open(path_save, 'w') as f:
                if not self.get_name():
                    pass
                else:
                    json.dump(json_content, f)

        except Exception as e:
            print(f"Error saving database state to {path_save}: {e}")

    def get_name(self) -> Optional[str]:
        """Returns the unique identifier for this instance."""
        return self.data.get("name", "unknown_instance")

def run_aliens():
    db = AlienDatabase()
    
    # Create sample data
