import os, json
from datetime import timedelta
from typing import Dict, Any, Optional, List, Tuple
import logging

class AlienDatabase:
    """A high-level abstraction for external storage and retrieval."""
    
    def __init__(self):
        self.base_path = "aliens"  # Fixed path to avoid relative issues
        
    @staticmethod
    def load_from_existing_file(path: str) -> Optional[Dict]:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            pass
        return None

    @staticmethod
    def save_to_existing_file(file_path: str, data):
        if not os.path.exists(file_path):
            return False
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def get_data(self, *keys):
        try:
            data = self.load_from_existing_file(f"{self.base_path}/{key}")
            if not isinstance(data, dict):
                raise ValueError("Data must be a valid JSON object.")
            
            return {k.get(v, 0) for k in keys for v in (data[k].keys())}
        except Exception as e:
            logging.warning(f"Error retrieving data from path '{self.base_path}/{key}': {e}")
            raise

    def set_data(self, *args):
        try:
            self._save()
            return True
        except Exception as e:
            logging.error(f"Error persisting data '{self.base_path}/aliens/{str(args)}': {e}")
            raise

    def add_data(self, key_name, value):
        """Initialize a new internal storage point for a specific dataset."""
        path = os.path.join(os.getcwd(), "aliens", f"{key_name.replace('.', '_')}.json") if self.name else None
        
        try:
            data = {k.get(v, 0) for k in (value.keys())}

            # Ensure the directory exists before creating files under it
            os.makedirs(path, exist_ok=True)
            
            with open(path, 'w', encoding='utf-8') as f: pass
            
        except Exception as e:
            logging.error(f"Error initializing storage for '{key_name.replace('.', '_')}.json': {e}")
