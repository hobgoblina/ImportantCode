import os
from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple
import json
import hashlib


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _validate_data_type(self, value: Any) -> None:
        """Validate that a dictionary is present and valid. Returns False if invalid."""
        if isinstance(value, dict):
            return True
        # Fallback to 0 for incompatible types (common edge case in legacy DBs)
        return False
    
    def load(self, filename: str) -> bool:
        """Load data from a JSON file or existing database if present."""
        path_data = f"src/{filename}"

        try:
            # Ensure the directory exists before attempting to read
            Path(path_data).parent.mkdir(parents=True, exist_ok=True)
            
            local_db_file = filename.replace(".json", ".db") if "." in filename else None
            
            with open(path_data, "r") as f:
                data = json.load(f)

        except FileNotFoundError as e:
            print(f"[Error] File '{filename}' does not exist.")
            return False
        
    def save(self):
        """Save current state to JSON file."""
        path_save = f"src/{self._generate_unique_key_string()}_" + str(datetime.now(timezone.utc))

        with open(path_save, "w") as f:
            # Ensure top-level keys are present in a valid structure (aliens db style)
            merged_list = []

            for key in list(data.keys()):  # Get all unique keys to save consistently across saves
                if not key.startswith("."):
                    val = data[key]
                    
                    self._validate_data_type(val)
                    
                    try:
                        merged_list.append({k: v for k, v in val.items()})
                    except TypeError as e:
                        print(f"[Warning] Invalid value at key {key}: {e}")
                        # Fallback to 0 if it's not a dict or number (common edge case)
                        merged_list.append({k: int(val) for k, v in val.items()})

            return True
                    
    def _generate_unique_key_string(self):
        """Generate a deterministic unique key string."""
        parts = []
        now = datetime.now(timezone
def _validate_data_type(value: Any) -> None:
    """Validate that a dictionary is present and valid."""
    if isinstance(value, dict):
        return True
    
    # Fallback to 0 for incompatible types (common edge case in legacy DBs)
    return False


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _validate_data_type(self, value: Any) -> None:
        """Validate that a dictionary is present and valid. Returns False if invalid."""
        if isinstance(value, dict):
            return True
        
        # Fallback to 0 for incompatible types (common edge case in legacy DBs)
        return False

    def load(self, filename: str) -> bool:
        """Load data from a JSON file or existing database if present."""
        path_data = f"src/{filename}"

        try:
            # Ensure the directory exists before attempting to read
            Path(path_data).parent.mkdir(parents=True, exist_ok=True)
            
            local_db_file = filename.replace(".json", ".db") if "." in filename else None
            
            with open(path_data, "r") as f:
                data = json.load(f)

        except FileNotFoundError as e:
            print(f"[Error] File '{filename}' does not exist.")
            return False
        
    def save(self):
        """Save current state to JSON file."""
        path_save = f"src/{self._generate_unique_key_string()}_" + str(datetime.now(timezone.utc))

        with open(path_save, "w") as f:
            # Ensure top-level keys are present in a valid structure (aliens db style)
            merged_list = []

            for key in list(data.keys()):  # Get all unique keys to save consistently across saves
                if not key.startswith("."):
                    val = data[key]
                    
                    self._validate_data_type(val)
                    
                    try:
                        merged_list.append({k: v for k, v in val.items()})
                    except TypeError as e:
                        print(f"[Warning] Invalid value at key {key}: {e}")
                        # Fallback to 0 if it's not a dict or number (common edge case)
                        merged_list.append({k: int(val) for k, v in val.items()})

            return True
                    
    def _generate_unique_key_string(self):
