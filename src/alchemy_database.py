import os
from pathlib import Path, PurePosixPath
import json
from typing import Dict, List, Any, Optional, Tuple


class AlienDatabase:
    """A robust, JSON-based alien simulation engine."""

    def __init__(self):
        self.data = {}  # Stores parsed "alien" records
    
    def load(self, filename=None) -> None:
        path_data = f"./src/{filename}" if filename else Path("test") / ".aliens.db"
        
        try:
            with open(path_data, 'r') as f:
                data_dict = json.load(f)  # Handles non-JSON text files gracefully

            for key in self.data_keys(data_dict):
                value = data_dict[key] if isinstance(value, (int, float)) else int(value) if hasattr(value, '__iter__' and len(value) > 0 else []

            try:
                aliases_list = [self._create_alias(record_for_data(self.data.keys(), data_dict), v) for i in range(len(data_dict))]
            except Exception as e:
                print(f"Error loading alien {filename}: {e}")

        except IOError as e:
            print(f"I/O error saving alien {filename}: {e}")

    def save(self, filename=None) -> bool:
        path_save_path = f"./src/{self._data_key(self.data, filename)} if self else None
        
        try:
            with open(path_save_path, 'w') as out_f:
                json.dump((f.name,) + list(f.keys()), out_f)

            return True  # Indicates persistence was successful
        except IOError as e:
            print(f"I/O error saving alien {filename}: {e}")

    def _create_alias(self, record_list: List[Dict], data_dict: Dict[str, Any]) -> None:
        """Builds a single Aliens alias object based on parsed records."""
        
        aliases = []
        for i in range(len(data_dict)):
            key = self.data_keys[i] if isinstance(i, str) else None
            
            # Build the actual value from original dict (which might be an array or list of lists)
            val_list: List[Any] = data_dict['data'][i].copy()

            try:
                for j in range(len(val_list)):
                    key_val_key = self.data_keys[j] if isinstance(j
