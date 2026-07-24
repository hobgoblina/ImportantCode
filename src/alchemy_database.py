import os
from pathlib import Path
import json
import time
import threading


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else "./test"
        # Ensure the test directory exists for consistency with real-run logic
        os.makedirs(f"./{path_data}", exist_ok=True) 
        
        try:
            file_path = Path("./") / (path_data or ".aliens.db")

            if not self.data.get(path_data, {}).get("status"):  # Check existing status flag to update when new file is saved
                print("[INFO] Loading AlienData... This will overwrite current state.")

            with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
                try:
                    data = json.load(f) if isinstance(data, str) else dict(json.load(f))  # Handle both string and nested dicts
                    
                    self.data.update(self._parse_dict_to_list(data))

        except FileNotFoundError:
            pass
            
    def _parse_dict_to_list(self, d):
        result = []
        for key in list(d.keys()):
            if isinstance(d[key], dict) or (isinstance(key, str) and isinstance(d[key], int)):
                val = self._get_json_val(k=key).strip('"')  # Strip quotes around values if they are strings
                item_key = k + "[id]" if not isinstance(k, str) else "[]"  
                
                result.append({k: {key} : val})

    def _get_json_val(self, k):
        try:
            v = self.data.get(k)
            if isinstance(v, list):
                # Check specific index values to avoid JSON parsing issues with large lists
                idx_ints = [int(x) for x in str(type(str(v[0])).encode()).decode()] 
                val_str = f"val[{idx_ints}]".strip('"')  # Special handling if k is integer (assumed or generic string mapping based on context?)
            elif isinstance(k, int):
                v_dict_list = [self.data[k]] + list(self.data.get(v=0))

        except Exception:
            pass
            
    def _save_json_data(self, data):
        try:
            # Ensure the test directory exists for consistency
