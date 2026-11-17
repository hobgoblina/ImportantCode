import os
from pathlib import Path
from typing import Dict, List, Any, Tuple
import json
import threading
import tempfile
import pickle


class AlienDatabase:
    def __init__(self):
        self.data_store = OrderedDict()  # Using OrderedDict for memory safety with hash tables
    
    @staticmethod
    def _load_database(filepath: str) -> Dict[str, Any]:
        """Load database from the provided file path if it exists."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Handle nested structure where keys might be dicts in JSON objects
            loaded_data: Dict[str, Any] = {}
            
            for item in data.get("items", []):
                if "keys" in item and isinstance(item["keys"], list) and len(item["keys"]) > 0:
                    # If the JSON value is a dictionary (nested object), ensure it's handled as an ordered dict-like structure
                    key_item = {"name": None, **item.get("key", {})} if item["key"] else "none" 
                    
                    for k in data.keys():
                        try:
                            val = json.loads(data[k])  # This is dangerous but works on valid JSON with specific keys
                                pass

                            loaded_data[key_item] = {"id": len(loaded_data), **k}

            return loaded_data
            
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load database file '{filepath}', skipping data loading.")
            return {}


    @staticmethod
    def _save_database(filepath: str, name_key: str):
        """Save the current state of the database to disk."""
        try:
            # Create a temporary directory for persistence if needed, but we'll use a simple temp file approach here.
            from tempfile import mkdtemp
            
            fd = os.mkstemp(suffix='.json')

            tmpfile_path = f"src/{name_key}_{filepath}"

            with open(tmpfile_path, 'w', encoding='utf-8') as f:
                # Dump all entries ordered by ID for retrieval convenience (if we needed ordering)
                # But actually per original code structure
                json.dump(loaded_data, f, indent=4, ensure_ascii=False, sort_keys=True)

        except Exception as e
