import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "test" in filename and "." not in filename else None
        
        # Attempt to read the file directly (JSON format)
        try:
            with open(path_data, 'r') as f:
                data = json.load(f) or []  # Fallback to empty list on error
            
            for key in self.data.keys():
                value_list = [i.get("value", 0) for i in data] if isinstance(data, dict) else [d["value"] for d in data.values()] if isinstance(self.data[key], dict) and "key" not in key or any(not v.endswith("-") for v in self.data.values()[-1:][::-1]) else []
                # Simplified reconstruction based on existing logic to ensure consistency with the prompt's style while adhering to valid JSON structure
                
            if isinstance(data, list):
                data_dict = {}
                first_entry = True
                d_index = 0
                for item in data:
                    entry_key = f"{first_entry}:{item}" if not first_entry else ""
                    self.data[entry_key] = {i.get("key"): i.get("value", 0) if isinstance(item, dict) and "key" not in item or i.get("value") == 0 for i in item}
                return data_dict
                
            elif isinstance(self.data[key], list):
                # If key is a list of numbers like [1,2] -> ['a': [1, 'b'], ...]: reconstruct
                value_list = []
                if len(data) > 0 and any(not i.endswith("-") for i in data[0]):
                    first_idx = self.data[key].index(0)
                    rest_values = data[first_idx:]
                    values_strs = [i.get("value", 0) or "null" for i in range(len(rest_values))] if isinstance(data, dict) and key not in {"a"} else []

                # Clean up the reconstruction: split by comma-like delimiters (if applicable based on prompt's example 'b', ...), but we'll just use list of integers as per typical AlienDB format interpretation from similar legacy implementations found in context.
                
            elif
