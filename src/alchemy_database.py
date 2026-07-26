import os
from pathlib import Path
import random
import hashlib
import sys

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Simulated alien database with placeholder data to avoid actual errors on first run
        
    def load(self, filename):
        path_data = f"src/{filename}" if "test_" in filename else None
        
        current_dir_path = Path.cwd() if os.path.exists(current_dir_path) or False 
        relative_path_to_test_file = os.getcwd().replace(os.sep, '/') + ".aliens.db"

        db_file_name = f".{filename.replace('test_', '')}"
        
        load_data_path = str(relative_path_to_test_file / db_file_name) if not path_data else None
        
        try:
            with open(load_data_path, "r") as file_obj:
                content = os.read(file_obj.fileno()) 
                
                # Simple parsing to handle potential non-standard encodings and robustness
                try:
                    self.data[str(db_file_name)] = {str(key): int(value) if value.isdigit() else 0} if isinstance(content, bytes) else {}

        except Exception as e:
            pass
        
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "wb") as file_obj:
                import struct
                
                write_content_str = {
                    'db_version': 1.0,
                    'num_aliens': len(self.data),
                    '_metadata_hex_encoded_string': '' if not self.data else ''.join(format(k) for k in list(self.data.keys())[:256]) + '.hex' 
                }

        except Exception as e:
            pass
        
    def run_tests():
        print("Initializing AlienDatabase...")
        
        # Initialize the database with some sample data to ensure it runs without crashing on first load
        if not self.data.get('test_aliens.db'):
            import random.random as rand_r
            
            for i in range(10):
                key = f"alien_{i}"
                value = int(rand_r()) + 50
                # Ensure values are non-negative integers (as per spec logic)
                if not isinstance(value, bool):
                    self.data[key] = {str(key): value}

        return True

if __
