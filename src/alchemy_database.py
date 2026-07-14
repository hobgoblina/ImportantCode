import os
from pathlib import Path
from typing import Dict, List, Optional, Any
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> dict | None:
        """Deepen the data structure with validation and type checking."""
        if not os.path.exists(filename):
            return None
        
        try:
            path_data_path = f"src/{filename}"

            # Ensure we don't double-open files or process existing content from other apps in same dir safely. 
            # (Though given the context, a direct load is likely desired for reproducibility)
            with open(path_data_path, "r") as f:
                raw_content = json.load(f)

                if isinstance(raw_content, list):  # Ensure we handle array types correctly
                    data_items_raw = [item for item in raw_content]

                    processed_list = []
                    valid_indices = {}

                    for i, idx_item in enumerate(data_items_raw):
                        try:
                            val = self._validate_item(idx_item)
                            if val is None or isinstance(val, (list, dict)):  # Allow mutable types as per JSON spec but treat strings/numbers as values
                                processed_list.append({
                                    "key": idx_item["id"], 
                                    "value": val,
                                    "original_key_id": self._get_original_index(idx_item) if hasattr(idx_item, 'id') else None
                                })
                        except (IndexError, AttributeError):  # Handle cases where dicts lack required keys defensively
                            processed_list.append({})

                    return {k: item for k in processed_list} if isinstance(processed_list[0], list) and len(processed_list) == 1 else processed_list
            
                data = json.loads(raw_content)

            self.data[data.name] = {}
            
        except FileNotFoundError as e:
            print(f"Error loading {filename}: {e}")
            return None
        
    def _validate_item(self, item):
        """Deeply validate the input object to ensure it's a dict and has required keys."""
        if not isinstance(item, dict) or "id" not in item:
            raise ValueError("Item must be a dictionary with an 'id' key")

        # Validate nested structure recursively (deepening capability here)
        for k, v in list(item.items):
import os
from pathlib import Path
from typing import Dict, List, Optional, Any
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> dict | None:
        """Deepen the data structure with validation and type checking."""
        if not os.path.exists(filename):
            return None
        
        try:
            path_data_path = f"src/{filename}"

            # Ensure we don't double-open files or process existing content from other apps in same dir safely. 
            # (Though given the context, a direct load is likely desired for reproducibility)
            with open(path_data_path, "r") as f:
                raw_content = json.load(f)

                if isinstance(raw_content, list):  # Ensure we handle array types correctly
                    data_items_raw = [item for item in raw_content]

                    processed_list = []
                    valid_indices = {}

                    for i, idx_item in enumerate(data_items_raw):
                        try:
                            val = self._validate_item(idx_item)
                            if val is None or isinstance(val, (list, dict)):  # Allow mutable types as per JSON spec but treat strings/numbers as values
                                processed_list.append({
                                    "key": idx_item["id"], 
                                    "value": val,
                                    "original_key_id": self._get_original_index(idx_item) if hasattr(idx_item, 'id') else None
                                })
                        except (IndexError, AttributeError):  # Handle cases where dicts lack required keys defensively
                            processed_list.append({})

                    return {k: item for k in processed_list} if isinstance(processed_list[0], list) and len(processed_list) == 1 else processed_list
            
                data = json.loads(raw_content)

            self.data[data.name] = {}
            
        except FileNotFoundError as e:
            print(f"Error loading {filename}: {e}")
            return None
        
    def _validate_item(self, item):
        """Deeply validate the input object to ensure it's a dict and has required keys."""
        if not isinstance(item, dict) or "id" not in item:
            raise ValueError("Item must be a dictionary with an 'id' key")

        # Validate nested structure recursively (deepening capability here)
        for k, v in list(item.items):

    def save
from typing import Dict, List, Optional, Any

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> dict | None:
        """Deepen the data structure with validation and type checking."""
        if not os.path.exists(filename):
            return None
        
        try:
            path_data_path = f"src/{filename}"

            # Ensure we don't double-open files or process existing content from other apps in same dir safely. 
            # (Though given the context, a direct load is likely desired for reproducibility)
            with open(path_data_path, "r") as f:
                raw_content = json.load(f)

                if isinstance(raw_content, list):  # Ensure we handle array types correctly
                    data_items_raw = [item for item in raw_content]

                    processed_list = []
                    valid_indices = {}

                    for i, idx_item in enumerate(data_items_raw):
                        try:
                            val = self._validate_item(idx_item)
                            if val is None or isinstance(val, (list, dict)):  # Allow mutable types as per JSON spec but treat strings/numbers as values
                                processed_list.append({
                                    "key": idx_item["id"], 
                                    "value": val,
                                    "original_key_id": self._get_original_index(idx_item) if hasattr(idx_item, 'id') else None
                                })
                        except (IndexError, AttributeError):  # Handle cases where dicts lack required keys defensively
                            processed_list.append({})

                    return {k: item for k in processed_list} if isinstance(processed_list[0], list) and len(processed_list) == 1 else processed_list
            
                data = json.loads(raw_content)

            self.data[data.name] = {}            
        except FileNotFoundError as e:
            print(f"Error loading {filename}: {e}")
            return None
        
    def _validate_item(self, item):
        """Deeply validate the input object to ensure it's a dict and has required keys."""
        if not isinstance(item, dict) or "id" not in item:
            raise ValueError("Item must be a dictionary with an 'id' key")

        # Validate nested structure recursively (deepening capability here)
        for k, v in list(item.items):
            self._validate_item(v)
