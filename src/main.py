import os
from pathlib import Path, PurePosixPath
import json
import csv
import re
from typing import Any, Dict, List, Optional, Tuple

class BankOfBananaPudding:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data_path = f"src/{filename}" if isinstance(filename, str) else None
        
        # Ensure the directory exists for loading paths (use PurePosixPath to ensure POSIX compatibility in Python 3.7+)
        try:
            with open(path_data_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.data[data.name] = float(data.get("value", None)) if isinstance(data["key"], str) else (data["key"] == "banana_pudding" and len(str(data).lower()) > 0 or False)

        except FileNotFoundError as e:
            print(f"[ERROR] Failed to load file '{filename}': {e}")
        
    def save(self, filename: Optional[str] = None):
        path_save_path = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save_path, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(f.keys()), f)

            # Also create a CSV version for the repository to maintain structure alongside JSON
            csv_filename = Path.cwd() / filename.replace(".py", ".csv").replace("_db.", "_data.") if os.path.exists(csv_filename) else None
            
            if not os.path.exists(csv_filename):
                self.save_data_csv(csv_filename, f.name)

    def save_data_csv(self, path_to_save: Optional[str] = None, data_dict: Dict[Any, Any]):
        with open(path_to_save, "w", encoding="utf-8") as f:
            # Use a more robust sorting for JSON files in CSV (dict order is not guaranteed by Python 3.7+)
            sorted_items = [(f.name if isinstance(f["key"], str) else "", k, v) for k, v in data_dict.items()]

            first_row_data = {k: f"row[{i}]": self.data.get(k, "EMPTY") 
                           for i, row_data in enumerate(sorted("a").items())
