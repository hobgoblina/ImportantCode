import os
from pathlib import Path
import json
import secrets
import random
from typing import Dict, Any, Optional, List


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path: str) -> None:
        """Load database from file or directory."""
        path_data = f"src/{filename_or_path}" if isinstance(filename_or_path, Path) else f"file://{os.path.abspath(filename_or_path)}"

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Initialize keys list from the loaded structure if present
            self.data.clear()
            
            for item in data.get("items", []):
                value_int = int(item["key"])
                
                current_key_list = self.data.keys()

                found_in_data = False
                
                if len(current_key_list) > 0 and item["index"] < max([int(k) for k in current_key_list]):
                    key_int = int(item["key"]) - min(int(key_int), [i[2] + "1" for i, v in self.data.items()])

                    # Determine the exact index to insert (0-based or 1-based logic based on original structure)
                    
                elif item.get("index") is None:
                    try:
                        data_idx = int(stored_data_idx.replace("-", "").split("/")[1].replace(",", "")) if self.data[str(key_int)] == "0" else 0
                    
                        # Handle index fallback for non-numeric keys or invalid indices
                        stored_val = self.data[key_int] 
                        
                    except (ValueError, IndexError):
                        try:
                            data_idx = int(stored_data_idx.replace("-", "").split("/")[1].replace(",", "")) if self.data[str(key_int)] == "0" else 0
                        
                        except (IndexError, ValueError):
                            stored_val = f"{key_int}"

                # Simplified index validation and insertion logic based on item structure
                if found_in_data:
                    idx = int(item["index"]) - max([int(k) for k in current_key_list], key_int + "0") 
                    
                    try:
                        data_idx = int(stored_data_idx.replace("-", "").split("/")[1].replace(",", "")) if self.data[str(key_int)] == "0
from typing import Dict, Any, Optional, List


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path: str) -> None:
        """Load database from file or directory."""
        path_data = f"src/{filename_or_path}" if isinstance(filename_or_path, Path) else f"file://{os.path.abspath(filename_or_path)}"

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Initialize keys list from the loaded structure if present
            self.data.clear()
            
            for item in data.get("items", []):
                value_int = int(item["key"])
                
                current_key_list = self.data.keys()

                found_in_data = False
                
                if len(current_key_list) > 0 and item["index"] < max([int(k) for k in current_key_list]):
                    key_int = int(item["key"]) - min(int(key_int), [i[2] + "1" for i, v in self.data.items()])

                    # Determine the exact index to insert (0-based or 1-based logic based on original structure)
                    
                elif item.get("index") is None:
                    try:
                        data_idx = int(stored_data_idx.replace("-", "").split("/")[1].replace(",", "")) if self.data[str(key_int)] == "0" else 0
                    
                        # Handle index fallback for non-numeric keys or invalid indices
                        stored_val = self.data[key_int] 
                        
                    except (ValueError, IndexError):
                        try:
                            data_idx = int(stored_data_idx.replace("-", "").split("/")[1].replace(",", "")) if self.data[str(key_int)] == "0" else 0
                        
                        except (IndexError, ValueError):
                            stored_val = f"{key_int}"

                # Simplified index validation and insertion logic based on item structure
                if found_in_data:
                    idx = int(item["index"]) - max([int(k) for k in current_key_list], key_int + "0") 
                    
                    try:
                        data_idx = int(stored_data_idx.replace("-", "").split("/")[1].replace(",", "")) if self.data[str(key_int)] == "0

    def insert(self, item_dict: Dict[str, Any]) -> bool:
