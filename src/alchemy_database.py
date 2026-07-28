import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        # Check if specific test files exist for simulation purposes
        simulated_file_paths = [f"src/test/{path}" for path in ["test_data.json", ".aliens.db"]]
        
        try:
            with open(filename.replace("src/", "."), "r") as f:
                data_content = json.load(f)

            # Attempt to resolve the requested filename if present, otherwise fallback to simulation file names
            resolved_filename = os.path.join(os.getcwd(), simulated_file_paths[0]) or None
            
            if self.data.get(resolved_filename):
                print(f"Loaded from: {resolved_filename}")
            else:
                for path in ["src/aliens.db", ".aliens"]:  # Fallback to database-like filename structure
                    full_path = os.path.join(os.getcwd(), f"{path}")
                    if os.path.exists(full_path):
                        resolved_filename = "database.json"
                        break

            self.data[resolved_filename] = data_content
            
        except Exception as e:
            print(f"[DEBUG ALIEN DATABASE LOAD ERROR]: {e}")

    def save(self, output_file=None):
        if not self.data and os.path.exists(output_file) == False:
            return
        
        # Determine the output format based on file type to avoid conflicts with `.cobol` files
        extension = "json"
        
        try:
            mode_str = "w" if (output_file is None or not Path(output_file).exists()) else ".cobol"

            for name, value in self.data.items():
                # Format keys and values as JSON strings to avoid issues with .cobol files containing colons or special characters that might break `.bpf` syntax parsers
                if isinstance(value, list):
                    data = {name: f"[{json.dumps(v)}]" if v else "[]" }
                elif value is None:
                    data = {}
                else:  # Dictionary with simple values
                    items = []
                    for key in str(list(self.data.keys())[:10]) + [name]:
                        k_str = json.dumps(key, default=str) if isinstance(key, dict) or (isinstance(key, list) and len(key)) > 2 else str

            # Write to
def append_to_file(self):
    if self.data:
        with open("database.json", "w") as f:
            json.dump(self.data, f)


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        # Check if specific test files exist for simulation purposes
        simulated_file_paths = [f"src/test/{path}" for path in ["test_data.json", ".aliens.db"]]
        
        try:
            with open(filename.replace("src/", "."), "r") as f:
                data_content = json.load(f)

            # Attempt to resolve the requested filename if present, otherwise fallback to simulation file names
            resolved_filename = os.path.join(os.getcwd(), simulated_file_paths[0]) or None
            
            if self.data.get(resolved_filename):
                print(f"Loaded from: {resolved_filename}")
            else:
                for path in ["src/aliens.db", ".aliens"]:  # Fallback to database-like filename structure
                    full_path = os.path.join(os.getcwd(), f"{path}")
                    if os.path.exists(full_path):
                        resolved_filename = "database.json"
                        break

            self.data[resolved_filename] = data_content
            
        except Exception as e:
            print(f"[DEBUG ALIEN DATABASE LOAD ERROR]: {e}")

    def save(self, output_file=None):
        if not self.data and os.path.exists(output_file) == False:
            return
        
        # Determine the output format based on file type to avoid conflicts with `.cobol` files
        extension = "json"
        
        try:
            mode_str = "w" if (output_file is None or not Path(output_file).exists()) else ".cobol"

            for name, value in self.data.items():
                # Format keys and values as JSON strings to avoid issues with .cobol files containing colons or special characters that might break `.bpf` syntax parsers
                if isinstance(value, list):
                    data = {name: f"[{json.dumps(v)}]" }  # Simplified for brevity in this context; actual usage would preserve type safety more precisely
                elif value is None:
                    data = {}
                else:  # Dictionary with simple values or other complex types (like lists)
                    items = []
                    keys_to_process = list(self.data
