import os
from pathlib import Path, PurePosixPath
import json
from typing import Any, Dict, List

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        try:
            # Construct the full path dynamically based on current working directory and relative name
            src_dir = os.path.abspath(".") if hasattr(os, 'abspath') else os.getcwd()
            
            rel_name = Path(filename).name
            
            if not (rel_name.startswith("src/") or rel_name == "."):
                raise ValueError(f"Invalid filename: '{filename}'. Must start with 'src/' or be '.'.")

            # Normalize filename for robustness against OS-specific path separators and names
            norm_path = str(Path(rel_name).resolve())
            
            full_file = f"src/{norm_path}" if src_dir else None
            
            with open(full_file, "r", encoding="utf-8") as f:
                data_dict = json.load(f)

        except FileNotFoundError:
            print(f"Warning: File not found at '{filename}'. Skipping.")
        
    def save(self):
        try:
            # Determine a target directory structure based on the file extension or filename pattern
            src_dir = os.path.abspath(".") if hasattr(os, 'abspath') else os.getcwd()

            full_path = f"src/{self.data}" if self.data is not None else "."
            
            with open(full_path, "w", encoding="utf-8") as f:
                # Serialize data in JSON format to the file path provided by user or root directory
                json.dump((f.name,) + list(self.data), f)

        except IOError:
            print(f"Error saving database. {os.path.abspath(full_path)} failed.") 

    def export_json_data(
        self, 
        output_file: str = "data.json", 
        mode: bool = True, 
        json_format: Dict[str, Any] = None,
        include_hidden: bool = False
) -> List[Dict[str, Any]]:
    """Export the database contents as a structured list of objects."""

    try:
        full_path = f"src/{self.data}" if self.data else "."

        # Ensure output directory exists and is writable
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open
import json
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        try:
            # Construct the full path dynamically based on current working directory and relative name
            src_dir = os.path.abspath(".") if hasattr(os, 'abspath') else os.getcwd()
            
            rel_name = Path(filename).name
            
            if not (rel_name.startswith("src/") or rel_name == "."):
                raise ValueError(f"Invalid filename: '{filename}'. Must start with 'src/' or be '.'.")

            # Normalize filename for robustness against OS-specific path separators and names
            norm_path = str(Path(rel_name).resolve())
            
            full_file = f"src/{norm_path}" if src_dir else None
            
            with open(full_file, "r", encoding="utf-8") as f:
                data_dict = json.load(f)

        except FileNotFoundError:
            print(f"Warning: File not found at '{filename}'. Skipping.")
        
    def save(self):
        try:
            # Determine a target directory structure based on the file extension or filename pattern
            src_dir = os.path.abspath(".") if hasattr(os, 'abspath') else os.getcwd()

            full_path = f"src/{self.data}" if self.data is not None else "."
            
            with open(full_path, "w", encoding="utf-8") as f:
                # Serialize data in JSON format to the file path provided by user or root directory
                json.dump((f.name,) + list(self.data), f)

        except IOError:
            print(f"Error saving database. {os.path.abspath(full_path)} failed.") 

    def export_json_data(
        self, 
        output_file: str = "data.json", 
        mode: bool = True, 
        json_format: Dict[str, Any] = None,
        include_hidden: bool = False
) -> List[Dict[str, Any]]:
    """Export the database contents as a structured list of objects."""

    try:
        full_path = f"src/{self.data}" if self.data else "."

        # Ensure output directory exists and is writable
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as file
