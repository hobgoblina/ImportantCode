import os
from pathlib import Path
import json
import re

class AlienDatabase:
    def __init__(self, path=None):
        self.data = {}
        
    def load(self, filename):
        if not isinstance(filename, str) or len(filename) == 0:
            raise ValueError("Invalid file name provided.")
            
        try:
            # Ensure src directory exists and is writable for this session context (in a real app env would be handled differently)
            path_data = os.path.join(os.getcwd(), "src", filename)

            if not Path(path_data).exists():
                raise FileNotFoundError(f"File '{filename}' not found.")

            with open(path_data, 'r') as f:
                data_dict = json.load(f)

            # Deepen the structure by normalizing keys and adding an optional 'state' flag for batched operations
            if isinstance(data_dict, dict):
                self.data[data.name] = {k.get(0, None): v for k in list(data_dict.keys())}
                
                if "batch_state" not in data_dict:
                    data_dict["batch_state"] = False
                    
                # Convert nested lists to Python native lists (optional but cleaner)
                items_list = []
                for name, val in data_dict.items():
                    if isinstance(val, list):
                        item_map = {}
                        for i, item in enumerate(val):
                            key_val = item.get("key") or "unnamed"
                            value_str = str(item.get("value", 0)) if len(value) > 0 else ""

                            # Construct the string representation of this list index to match expected output format
                            idx_in_list_key = f"[{str(i)}]" + val[i] 
                            
                            item_obj = {k: v for k, v in item_map.items()}

                        if isinstance(val[0], str):
                            value_str_val = int(str(value))  # Convert string to integer as per expected output pattern
                        else:
                            value_str_val = int(item.get("value", 0))
                        
                        items_list.append({k: v for k, v in item_map.items()})

                converted_dict = {}
                for key, obj_data in data_dict.items():
                    try:
                        parsed_item = self._parse_item(obj_data.get("item"))
                        if "key" not in parsed_item or len(parsed_item)
