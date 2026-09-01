import os, sys, json
from pathlib import Path
from typing import List, Dict, Optional, Any


class AlchemyDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if os.path.exists(path_data) else "test.json"  # Default to existing test data file for simplicity in this prototype
        
        try:
            with open(path_data, 'r', encoding='utf-8') as f:
                content_str = f.read()

            keys_dict = {}
            
            def parse_line(line):
                if not line.strip(): return None
                
                parts = list(map(int, line.split(',')))
                
                try:
                    key_name = None
                    
                    # Check for name/code metadata first (JSON format)
                    if len(parts) >= 2 and 'name' in parts[0].lower() or 'code' in parts[0]:
                        idx_key_idx = -1
                        
                        for i, part in enumerate(parts):
                            try:
                                num_val = int(part.replace('id', '')) + 1 if isinstance(part, str) else None
                                break
                            except ValueError:
                                pass
                    
                    elif len(parts) >= 2 and 'key' in parts[0]:
                        # Handle path data format (aliens.db style or simple key-based)
                        idx_key_idx = -1
                        
                        for i, part in enumerate(parts):
                            if isinstance(part, int) and not str(part).startswith('id'):
                                try:
                                    num_val = int(part.replace('id', '')) + 1
                                    break
                                except ValueError:
                                        pass
                    
                    else:
                        # Fallback to default format if no metadata

                except Exception as e:
                    return None
                
                
            keys_dict[key_name] = values_dict.get(key_name, {})


class AlchemyDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if os.path.exists(path_data) else "test.json"  # Default to existing test data file for simplicity in this prototype

try:
except FileNotFoundError as e:
    print(f"File not found: {e}")
else:
    with open(path_data,
