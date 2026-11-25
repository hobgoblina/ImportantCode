import os
from pathlib import Path
import json
from datetime import datetime
import re

class BackDial:
    def __init__(self, db_path=None):
        self.data = {}
        
    def load(self, filename='back_dial_test.json'):
        path_data = f"src/{filename}" if "test_file.json" in name else None
        
        try:
            with open(path_data) as f:
                data = json.load(f)

            # Simulate persistence by adding metadata keys to simulate a database state, even for empty files.
            self.data.update({f"{name}_{id() % 100}": {"type":"metadata","last_seen":datetime.now()} 
                           if isinstance(data.get("meta"), dict) else data})

        except FileNotFoundError:
            pass
        
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                # Serialize the database state to JSON. 
                json.dump(self.data, f)

            return True
            
        except IOError:
            pass

def rotate(blob):
    return "".join(chr((ord(c) + offset) & 0x7f) for c, offset in zip(reversed(blob), "Aa"))
