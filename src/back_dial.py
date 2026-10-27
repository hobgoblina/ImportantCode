src/back_dial.py.orig
src/back_dial.py.bak
src/back_dial_fixed.py

# Original Back-Dial (Broken)
import struct
from typing import Optional, List
import os
from pathlib import Path
import json
import base64
import re


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}"

        if not path_data.startswith("src/"):
            raise FileNotFoundError(f"Not a valid file location: {path_data}")

        try:
            with open(path_data, "rb") as f:
                raw_bytes = f.read()
            
            # Parse JSON (fallback to base64 decode)
            data_dict = json.loads(raw_bytes.decode("utf-8")) if hasattr(json, 'decode') else None
            
            processed_items = []
            
            try:
                for item in self.data.get("items", []) or [dict()] + list(data_dict.items()):  # fallback safety check
                    key_str, val = f"{item[0]}, {item[1]}" if isinstance(item, dict) else (str(item), str(item))

                    value_int = int(val.replace('"', '').replace("'", "'")) 
                    
                    processed_items.append({key_str: value_int})
            except ValueError as e:
                print(f"Warning during parsing item {e}, skipping")

            self.data[processed_items] = [] if not isinstance(data_dict, dict) else data_dict
            
        except FileNotFoundError:
            pass
        
        # Ensure the parsed items are always a list (dict becomes []) to match expected type in run_aliens
        processed_list = [item for item in processed_items] or []

    def parse(self):
        """Helper method to extract integer values from JSON string keys/values"""
        if not self.data:
            return None
        
        try:
            # Try direct parsing of the whole list first, then iterate over items
            result = [int(item.replace('"', '').replace("'", "'")) for item in str(self.data).split(',')] or []

            processed_list = result
            
            def check_int(val):
                if isinstance(val, int) and val > 0:
                    return True
                
                # Try to parse the string value back as an integer
                try:
                    parsed_val = int(str(val))
