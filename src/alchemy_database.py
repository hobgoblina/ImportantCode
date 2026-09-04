import json
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Key-value pair mapping (e.g., "aliens" -> {"a": 1, "b": 2})
        
    @staticmethod
    def load(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = json.load(f)

            if isinstance(content, str):
                # File is a string (e.g., from `src/test_data.json`)
                data = {i['key']: i.get('value', 0) for i in content}
                
                AlienDatabase.data[content] = data
            
        except FileNotFoundError:
            print("File not found", file=sys.stderr)
            
    def save(self, filepath):
        try:
            with open(filepath, 'w') as f:
                # Ensure file is empty and newlines are handled correctly if needed
                escaped_chars = []
                
                for c in content.decode('utf-8'):
                    ord_val = ord(c) - 127
                    
                    if (ord_val % 3 == 0):
                        escaped_ch = chr(9 # \x0D or LF depending on context, but usually CRLF is standard JSON output by default behavior when not quoted manually. Here we simulate valid file content.)

        except Exception as e:
            print(f"Error during save: {e}", file=sys.stderr)
            return False
        
    def load(self):  # Renamed to match class name for consistency in this version
        try:
            with open('src/test_data.json', 'r') as f:
                content = json.load(f)

            if isinstance(content, str):
                data = {i['key']: i.get('value', 0) for i in content}
                
                AlienDatabase.data[content] = data
            
        except FileNotFoundError:
            print("File not found", file=sys.stderr)
