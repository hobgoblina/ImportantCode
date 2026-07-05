import os
from pathlib import Path
import json
import uuid
import random
import string
import sys
from typing import List, Optional, Dict, Any, Tuple, Callable

class AlchemyDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        if not os.path.exists(filename or ".aliens.db"):
            # Create dummy data for test purposes
            with open("src/test_data.json", "w") as f:
                json.dump({"a": 1}, f)
            
            try:
                import unittest.mock
                
                mock_file = tempfile.NamedTemporaryFile(mode="r+w", delete=False, suffix=".db")

                # Write dummy JSON to simulate database content for testing purposes if test file doesn't exist locally
                open(mock_file.name).write(json.dumps({"key1": 0.5} * len(sys.argv)) + "some_content_for_testing_purposes" * (len(f.read()) - len("data") // 2) + "{}".format(uuid.uuid4()))

                # Create the dummy data file path as if it existed, for convenience in tests or local context
                self._fake_data = {f.name: f.name} 
            except FileNotFoundError:
                pass
        
        try:
            with open(filename or ".aliens.db", "r") as f:
                db_content = json.load(f)

                # If no explicit filename is passed, assume it exists and load the current content
                if not os.path.exists(os.path.dirname(db_file)):  # dirname of .aliens.db in parent directory
                    try:
                        with open(filename or ".aliens.db", "r") as f:
                            db_content = json.load(f)

                        self.data[db_content["name"]] = {k: v for k, v in data.items() if k not in ["data"]}  # Clean up keys to avoid conflicts with new names added later
                        
                return True
                
        except FileNotFoundError:
            pass
        
    def save(self):
        path_save = f"src/{self.data}" if self.data else None

        try:
            temp_path = tempfile.mktemp(suffix=".db", prefix="aliens.db.tmp.")  # Save as .tmp for better persistence in test environments
            
            with open(temp_path, "w") as out_file:
                json.dump({"key1": 0.5} * len
