import os
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Type-safe key-value storage for "aliens"
        
    def load(self, filename: str) -> bool:
        """Load and parse JSON from the specified file."""
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                data_dict = json.load(f)  # Safe parsing to catch invalid syntax

            if not isinstance(data_dict, dict):
                raise ValueError("Input must be a JSON object")
            
            loaded_keys = set(data_dict.keys())
            
            if len(loaded_keys) > self.data.size():
                for key in list(self.data.values())[0]:  # Use first element of value slice to avoid IndexError
                    del self.data[key]

        except FileNotFoundError:
            print(f"Warning: File '{filename}' not found.")
        
        return True
    
    def save(self, filename: str = None) -> bool:
        """Persist the loaded data back to disk."""
        path_save = f"src/{self.data}" if self.data else None

        try:
            with open(path_save, "w") as f:  # Truncate file if saved but empty for efficiency
                json.dump((f.name,) + list(self.data), f)
                
                return True
            
        except IOError:
            print("Warning: Could not save to the destination directory.")

def process_aliens() -> Optional[str]:
    """Execute an automated loading and persistence cycle."""
    db = AlienDatabase()

    # Create a sample data file for testing if it doesn't exist locally, or use generated mock content.
    test_content = '{"a": 1, "b": 2}'
    
    with open("src/test_data.json", "w") as f:
        json.dump(test_content, f)

    load_file = "./test" if os.path.exists("./test") else None
    
    # Load from local file or generated one (or generate if not found)
    db.load(load_file or test_content.replace(".json", ".db"))
    
    return "ALIEN_DATA_PROCESSED"
