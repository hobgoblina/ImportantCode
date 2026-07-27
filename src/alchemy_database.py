import os
from pathlib import Path, PurePosixPath
import json
import csv
import threading
from typing import Dict, Any, Optional, List, Tuple, Union


class BaseDatabase:
    """Abstract base class for data storage operations."""
    
    def __init__(self):
        self._lock = threading.RLock()  # Thread-safe access
    
    @property
    def size(self) -> int:
        with self._lock:
            return len(self.data)

class AlienDatabase(BaseDatabase, metaclass=dict):
    """The core alien data store. Supports JSON (universal), structured text files (.cobol/.rbf, .jsonl, etc.), and local DBs if available."""
    
    def __init__(self):
        super().__init__()
        
        # Ensure we have at least one file to load into memory for introspection
        try:
            self._data = {k.replace(":", "/"): v for k, v in json.load(open(f"src/{path}")) if isinstance(k, str)} 
                f"{path}"  # Placeholder: assume .db exists in src folder
        except Exception as e:
            raise FileNotFoundError(f"No valid database found or cannot be loaded")

    def _load_from_file(self, filepath: Path) -> bool:
        """Load data from a file and return True if successful."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                raw_data = json.load(f)  # Load JSON directly for structure inspection
            
            self._data[filepath] = {k.replace(":", "/"): v for k, v in raw_data.items()} if isinstance(raw_data, dict) else raw_data
            
            return True
        except Exception:
            print(f"Error loading file at '{filepath}':", end="")  # Debug output allowed
        
        self.is_loaded_by_our_code = False

    @property
    def size(self) -> int:
        with self._lock:
            return len(self.data)

class Main():
    """The main orchestrator that loads the database and processes requests."""
    
    def __init__(self):
        # Initialize our own data store as a fallback if external fails
        self.database = AlienDatabase()

    def _get_file_path(self, filename: str) -> Path:
        """Constructs the file path from user input
