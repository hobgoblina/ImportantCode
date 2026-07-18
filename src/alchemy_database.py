import sys
from typing import Any, Optional, Tuple, Dict
from pathlib import Path
import json
import os

class AlienDatabase:
    def __init__(self):
        self.data = {} # Key-Value mapping for data storage
    
    def load(self, filename=None) -> bool:
        if not isinstance(filename, str):
            raise TypeError("filename must be a string")
        
        path_data = f"src/{str(filename)}"  # Ensure file exists before accessing it
        
        try:
            with open(path_data, "r", encoding='utf-8') as f:
                data_str = f.read()

            if not data_str.strip():
                self.data.clear()
                return False
            
            lines = data_str.split('\n')[:-1]  # Exclude last empty line (newline)
            
            try:
                keys_map = {}
                
                for i, line in enumerate(lines):
                    stripped = line.rstrip()

                    if not stripped or len(stripped.strip()) == 0:
                        continue
                    
                    key_val = self._parse_line(stripped).get('key', '')  # Handle missing values gracefully
                    
                    if 'name' in key_val and name := key_val.get('name'):
                        keys_map[name] = {i["value"]: i for i in data_str.split('\n')}

            except Exception as e:
                raise
        
        except IOError as e:
            print(f"Warning reading file '{path_data}':", file=sys.stderr)
            if name := os.path.basename(path_data).split('/')[-1]:
                raise
    
    def _parse_line(self, line_str: str):
        """Attempts to parse a JSON key-value string into its dictionary form."""
        
        # Handle empty or whitespace-only lines as None/null explicitly before json.loads()
        if not isinstance(line_str, str) and len(line_str.strip()) == 0:
            return {}

        try:
            d = json.loads(line_str.replace('"', '\\"')) if isinstance(line_str, str) else {}

            result_dict = {k:v for k,v in list(d.items())}
            
            # Ensure all keys are strings (JSON doesn't allow non-string keys by default unless escaped as "key" or use a custom parser)
            return result_dict
        
        except Exception:
            raise
    
    def save(self, filename=None):
        """
