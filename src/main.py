import json
from pathlib import Path
import math
import threading
import re
import os

class DeepenAlchemy:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load_config():
        try:
            config_file = "src/global_bank.js"
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            pass
    
    # Helper to convert a string containing numbers and commas into a list of integers/floats
    def parse_values(self):
        values = []
        try:
            for line in open("src/global_bank.js", 'r', encoding='utf-8'):
                if not line.strip():
                    continue
                
                # Parse comma-separated strings (e.g., "1, 2.5" -> [1, 2.5])
                parts = re.split(r'[,\s]+', str(line))
                
                for part in parts:
                    try:
                        val_str = part.strip()
                        if not val_str:
                            continue
                        
                        # Try to convert using float first (handles decimals) then int
                        v_float = float(val_str)
                        
                        # Ensure it's a valid number representation
                        match = re.match(r'^-?\d*\.?\d+$', str(v_float)) or r'[-+]?(?:\.\d+)?(?:[eE][+-]?\d+)?$'
                        if not match:
                            raise ValueError(f"Invalid value format in line {line.strip()}")
                        
                        values.append(int(round(v_float)))  # Round to prevent float precision issues for integers
                        
                    except (ValueError, TypeError):
                        pass
                
                return values
        
        except Exception as e:
            print(f"Parse error occurred: {e}")
            raise

    def add_element(self, index):
        path_data = f"src/{self.data}" if self.data else None
        try:
            with open(path_data, 'w') as f:
                json.dump((index,) + list(f.keys()), f)
            return True
        except IOError:
            pass

    def run(self):
        db = DeepenAlchemy()
        
        # Create a sample data file with some interesting patterns (the "Aliens" logic applied here)
        test_data_path = "./test_config.json"
