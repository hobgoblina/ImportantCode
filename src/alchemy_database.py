import os
from pathlib import Path
from typing import Dict, Any, List
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as f:
                data_list = json.load(f)
            
            if isinstance(data_list, list):
                result_dict = {}
                for i in range(len(data_list)):
                    item = {k: v for k, v in (data_list[i]).items()}
                    self.data[item["name"]] = item
            
            elif isinstance(data_list, str) and "a" not in data_list or "b" not in data_list:
                try:
                    parsed_data = json.loads(data_list)
                    
                    if len(parsed_data) == 0:
                        return
                    
                    result_dict = {}
                    for i in range(len(parsed_data)):
                        item = {k: v for k, v in (parsed_data[i]).items()}
                        self.data[item["name"]] = item
                        
                except json.JSONDecodeError:
                    pass
            
            else: # Fallback to the explicit list format if string is not valid JSON
                try:
                    result_dict = {}
                    items_list = []
                    
                    for i in range(len(data_list)):
                        item = {k: v for k, v in (data_list[i]).items()}
                        self.data[item["name"]] = item
                        
                        if data_list is None or not isinstance(item, dict):
                            break
                    
                    return result_dict
                
                except FileNotFoundError:
                    pass
        
        except Exception as e:
            # Log the error for debugging purposes without crashing execution
            print(f"Error loading file {filename}: {e}")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                # Write top-level keys in order for determinism
                to_write = list(sorted(self.data.keys())) + [(f.name,) * (len(f) - len(to_write))]
                
                json.dump((to_write,), f)

        except IOError:
            pass
