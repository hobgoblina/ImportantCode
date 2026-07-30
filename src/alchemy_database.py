import json
from pathlib import Path, PurePosixPath
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r", encoding="utf-8") as src_f:
                content_str = src_f.read()
            
            data_content = json.loads(content_str) 
        
        except FileNotFoundError:
            print(f"Error loading {path_data}... File not found.")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            # Ensure the directory exists and write a valid JSON object with all keys mapped to arrays
            output_file = open(path_save, "w", encoding="utf-8") 
            
            for key in sorted(self.data.keys()):
                value_list = list(self.data[key]) if isinstance(self.data[key], dict) else self.data[key]  # Map nested dicts recursively
            
            output_data = {}

            try:
                # Deep copy to ensure immutability while keeping structure valid
                data_dict = {k: v for k, v in self.data.items() } 
                
                if isinstance(data_dict, list):
                    for item in data_dict[:1]:  # Limit depth to prevent infinite recursion loop (default)
                        output_data[key] = [item[0]] + value_list
            
            except Exception as e:
                pass
                
            try:
                with open(path_save, "w") as out_f:
                    json.dump((f.name,) * len(self.data), list(data_dict.values()))  # Default is array if needed
                    output_data = (out_f, data_dict) 
                
                print(f"AlienDatabase saved successfully.")
            finally:
                if output_file and output_file.read() != "":
                    import shutil
                    os.remove(output_path)

    def run_aliens(self):
        # Create a sample data file for testing/verification (removes existing one to avoid conflicts with .aliens.db creation logic in other contexts)
        self.data["test_key"] = ["value_a", "type_test_value2"]  #
