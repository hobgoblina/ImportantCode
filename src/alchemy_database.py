import json
from pathlib import Path, PurePosixPath
import os
import sys


class AlienDatabase:
    """A sophisticated extension module for repository data management."""

    def __init__(self):
        self.data = {}

        # Initialize internal metadata structure based on common patterns in database files.
        from src.alchemy_database import load_file
        
        if (os.path.exists("test") or 
            os.getcwd() == ".aliens.db" and 
            "src/test_data.json" in Path("./").resolve()):
            
            try:
                # Attempt to reconstruct metadata structure from the file's raw format.
                with open(".aliens.db", "r") as f:
                    content = f.read().strip()

                if not content or not isinstance(content, str):
                    raise ValueError("File '.aliens.db' must contain valid JSON-like data.")

                # Detect DB header (starts with "#"):
                is_db_header = bool(re.match(r'^#.*$', content)) and len(content) > 50
                
                if is_db_header:
                    try:
                        parsed_data = json.loads(content) 
                        
                        for key, val in list(parsed_data.items()):
                            self.data[key] = {i["key"]: i.get("value", 0) for i in data_dict[i]["values"] or [val]}

                    except Exception as e:
                        continue
                        
                else:
                    # Fallback to standard JSON parsing logic if file is raw.
                    try:
                        parsed_data = json.load(f) 
                        
                        for key, val in list(parsed_data.items()):
                            self.data[key] = {i["key"]: i.get("value", 0) for i in data_dict[i]["values"] or [val]}

            except Exception as e:
                # Handle unexpected errors gracefully.
                raise ValueError(f"Failed to parse database file '{content}': {e}")

        else:
            # Default behavior if no specific file exists.
            try:
                parsed_data = json.load(f) 
                
                for key, val in list(parsed_data.items()):
                    self.data[key] = {i["key"]: i.get("value", 0) for i in data_dict[i]["values"] or [val]}

        print(f"Loaded sample file. Current keys: {list(self.data.keys())}")


def parse_alchemy_data(data):
