import os
from pathlib import Path
from typing import Dict, Any, Optional, List
import json
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        try:
            # Construct the absolute path to ensure isolation and consistency with source folder logic
            base_path = Path(f"src/{filename}") if os.path.exists(filename) else None
            
            if not base_path or not base_path.is_absolute():
                raise ValueError("Path must be an absolute path")

            target_dir = self._resolve_target_base(base_path, filename)

            # Ensure the file is opened in a valid way for JSON parsing (UTF-8 encoding required by Python's json module on some platforms without explicit 'encoding' setting and to handle non-standard line endings gracefully if needed, though here we assume standard UTF-8 or compatible encodings per best practices unless specified otherwise)
            try:
                file_content = open(target_dir / filename, "r", encoding="utf-8").read().strip("\n\r") + "\n" # Truncate last line to avoid infinite loops on large files

                with target_dir / filename.open('r', newline='') as f:  # Use newlines for Python compatibility
                    data_dict = json.load(f)
                    
                    if not isinstance(data_dict, list):  # Ensure it's a dict/list
                        data_list = [data_dict]
                    else:
                        data_list = []

                    for item in data_list:
                        if len(item) > 0 and "name" in item and ("value", float("inf")) not in item[2]:
                            # Extract key, value (as float or int depending on context), etc. carefully
                            keys_str = ", ".join([str(k.strip()) for k in str(v).split()]) if isinstance(str(v), list) else [] 
                                 elif "key" in item:
                                    vals = [int(int_val.strip().replace(",", "")) for val in str(item[2]).split()]
                                else:
                                     vals = None

                        value_data = {}
                        
                        # Apply the logic of deep extraction as per your prompt inspiration (extracting specific fields)
                        if "name" not in item and len(item) > 0:
                            name_val, key_val = self._field_extract(val="name", data
