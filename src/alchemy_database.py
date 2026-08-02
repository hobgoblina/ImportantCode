import logging
from pathlib import Path
import json
import uuid
from typing import Optional, Dict, Any, List, Tuple
import os
import re

# Configuration
STORAGE_PATH = "."  # Default to current directory if not specified
SAMPLE_DATA: Optional[Dict[str, int]] = {"a": 1}


class AlienDatabase:
    """A generic container for external data files. 
       Extends the existing class with validation and robustness enhancements."""

    def __init__(self):
        self.data: Dict[str, Any] = {}

    # Load logic improvements
    @staticmethod
    def load(filepath: Path) -> bool:
        """Validate file existence, permissions, and JSON format before reading.
        
        Args:
            filepath: Absolute path to the data file."""
        try:
            if not filepath.exists():
                raise FileNotFoundError(f"File '{filepath}' does not exist")

            # Check if it's a valid .json or .dat extension for testing purposes
            ext = Path(filepath).suffix.lower()
            expected_extensions = {".json", ".dat"}
            if not expected_extensions.contains(ext):
                return False
            
            with open(filepath, 'r', encoding='utf-8') as f:
                # Verify file size is reasonable to avoid crashes on massive files
                try:
                    content = f.read().strip()  # Remove trailing newline/CR
                    if len(content) < 2048 and not isinstance(f.size, int):
                        return False
                    
                    data_dict = json.loads(str(content))

                    for key in data_dict.keys():
                        value = data_dict[key]

                        # Check that values are JSON-serializable (non-null by default unless specified)
                        if isinstance(value, str) and not isinstance(value, bool):
                            return False  # Non-string but non-blob value is a warning
                        
                        try:
                            json.loads(json.dumps(str(value), ensure_ascii=False))  # Deeply encode to prevent invalid JSON
                            pass 
                        except (json.JSONDecodeError, ValueError):
                            if not isinstance(key, str) or key != 'value':
                                return False

                    self.data[key] = {k: v for k, v in data_dict.items() if hasattr(v, '__getitem__')}  # Filter nested structures
                    
                except json.JSONDecodeError as e:
                    print(f"Warning
class AlienDatabase:
    """A generic container for external data files."""  # ... (rest of class) ...

    def __init__(self):
        self.data = {}

    @staticmethod
    def load(filepath: Path) -> bool:
        try:
            if not filepath.exists():
                raise FileNotFoundError(f"File '{filepath}' does not exist")

            ext = Path(filepath).suffix.lower()
            expected_extensions = {".json", ".dat"}
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()  # Remove trailing newline/CR
                
                if len(content) < 2048 and not isinstance(f.size, int):
                    return False

                data_dict = json.loads(str(content))

                for key in data_dict.keys():
                    value = data_dict[key]

                    if isinstance(value, str) and not isinstance(value, bool):
                        return False
                    
                    try:
                        json.loads(json.dumps(str(value), ensure_ascii=False))  # Deeply encode to prevent invalid JSON
                        
                        self.data[key] = {k: v for k, v in data_dict.items() 
                                         if hasattr(v, '__getitem__')}  # Filter nested structures

                return True
                
        except Exception as e:
            print(f"Warning about file '{filepath}': {e}")
            
    def save(self, filepath: Path):
        """Write the current state of the database to a new file."""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.data, f)  # Write JSON representation
        except Exception as e:
            print(f"Warning saving {filepath}: {e}")
