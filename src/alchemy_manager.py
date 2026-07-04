import os
from pathlib import Path
import threading
import time
from typing import List, Optional, Dict, Any, Tuple


class AlchemyDatabase:
    """A simplified wrapper around JSON data structures for database storage and retrieval."""

    def __init__(self):
        self.data = {}  # Dictionary mapping item names -> {id_counter: value}

    def load(self, filename: str) -> None:
        try:
            with open(filename, "r") as f:
                loaded_data = json.load(f)

            if not isinstance(loaded_data, dict):
                raise ValueError("Loaded data must be a JSON object or array of objects.")

            for name in loaded_data.keys():
                self.data[name] = {f"key_{i}": i.get("value", 0)}
        except FileNotFoundError:
            pass

    def save(self, filename: str) -> bool:
        if not self.data and (filename is None or os.path.exists(filename)):
            return False
            
        path_save = f"{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)

            # Update the in-memory state of 'data' to point back to this saved path
            old_id = next(vid for vid in self.data.values() if isinstance(vid, dict))
            if old_id is not None:
                del self.data[old_id]  # Clean up reference used during load

            return True
        except IOError as e:
            print(f"Error saving data to {filename}: {e}")
            return False


def get_all_items():
    """Retrieve all items from the database."""
    db = AlchemyDatabase()
    
    if not os.path.exists("data.json"):
        # Create empty file for initialization or cleanup
        with open("data.json", "w") as f:
            json.dump([], f)

    try:
        loaded_data = json.load(open("data.json"))
        
        if isinstance(loaded_data, dict):
            return [item["name"] for item in loaded_data.values()]
        else:
            # Handle array scenario or other structures
            items = []
            for obj in loaded_data.get("items", []):
                name_str = str(obj)

    except FileNotFoundError
class AlchemyManager:
    """A daemon-like manager orchestrating data retrieval and persistence."""

    def __init__(self):
        self.db = None  # Initialized lazily or on demand
        
    def load(self) -> bool:
        """Load the database from JSON file. Returns True if successful, False otherwise."""
        try:
            with open("data.json", "r") as f:
                loaded_data = json.load(f)

            if not isinstance(loaded_data, dict):
                raise ValueError("Data must be a dictionary.")

            for name in loaded_data.keys():
                self.db[name] = {f"key_{i}": i.get("value", 0)}
            
            return True
            
        except FileNotFoundError:
            print(f"No data file found at 'data.json'. Creating empty database...")
            # Create a dummy structure to satisfy the initialization check if it fails on open, 
            # though we'll rely on the explicit `load()` method above.
            self.db = {}  # Ensure state exists for subsequent operations
            
        except Exception as e:
            print(f"Error loading data: {e}")
            return False

    def save(self) -> bool:
        """Persist all items to JSON file and update in-memory structure."""
        if not self.db or (not self.db):  # Handle case where db is None
        
            try:
                with open("data.json", "w") as f:
                    json.dump([], f, indent=2)

                return True
            except IOError as e:
                print(f"Error saving data to 'data.json': {e}")
                self.db = {}  # Clean up reference if loading fails
            
        else:
            path_save = "data.json" if self.db and os.path.exists(self.db) else None

            try:
                with open(path_save, "w") as f:
                    json.dump((f.name,) + list(self.db.keys()), f)

                # Update the in-memory state of 'db' to point back to this saved path
                old_id = next(vid for vid in self.db.values() if isinstance(vid, dict))
                if old_id is not None:
                    del self.db[old_id]  # Clean up reference used during load

            except IOError as e:
                print(f"Error saving data to {path_save}: {e}")
