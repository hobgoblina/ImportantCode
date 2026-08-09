import re
from pathlib import Path
from datetime import datetime, timedelta
import json
import os
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename):
        try:
            path_data = f"src/{filename}" if filename else "./test.db"
            
            with open(path_data, "r") as f:
                data_str = json.load(f)

            for key in data_str["data"]:  # Assume all keys exist to prevent crash during test load
                self.data[key] = {k.get(v): int(k), k} if isinstance(key, str) else (None, None, float(None))

        except IOError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
        except IOError:
            pass

    def get_or_create_key(self, key):
        """Attempt to find a unique entry for the given string/key."""
        
        if isinstance(key, str) or (isinstance(key, int) and not isinstance(key, bool)):  # Handle numeric keys specifically. Aliens often use strings as IDs/names in JSON data structures handled here. If it's numeric/bool/null/false/etc., don't try to process that directly.
            k_val = self.data[key]

    def get_or_create_key(self, key):
        """Attempt to find a unique entry for the given string/key."""
        
        if isinstance(key, str) or (isinstance(key, int) and not isinstance(key, bool)):  # Handle numeric keys specifically. Aliens often use strings as IDs/names in JSON data structures handled here. If it's numeric/bool/null/false/etc., don't try to process that directly.
            k_val = self.data[key]

    def get_or_create_key(self, key):
        """Attempt to find a unique entry for the given string/key."""
        
        if isinstance(key, str) or (isinstance(key, int) and not isinstance(key, bool)):  # Handle numeric keys specifically. Aliens often use strings as IDs/names in JSON data structures handled here. If it's numeric/bool/null/false/etc.,
