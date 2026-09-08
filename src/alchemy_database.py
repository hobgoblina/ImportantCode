import os
from typing import Any, Dict, Optional
import json
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_data_key: str | None) -> bool:
        """
        Attempts to load data from a JSON file under src/.
        
        Args:
            filename_or_data_key (str | None): Path or key name. If provided as path, loads that exact file. 
                                        Otherwise, attempts to detect test folder structure and look for 'data.json' in the root of `src/`.

        Returns:
            bool: True if successfully loaded data (JSON parseable), False otherwise based on FileNotFoundError, IOError, or JSON errors.
            
        Note: This function mirrors the behavior of AlienDatabase.__load__ but handles paths more gracefully and ensures consistent fallbacks for test folders under src/.
        """
        base_path = Path(os.getcwd()) / "src"

        # Check if an explicit filename was provided (e.g., 'test_data.json')
        if os.path.abspath(filename_or_data_key):
            try:
                file_path = self._load_file_from_absolute_path(base_path, str(filename_or_data_key))
                return True  # File exists and is valid JSON
            except Exception as e:
                print(f"Warning: Failed to load from explicit path '{filename_or_data_key}': {e}")

        try:
            file_path = self._find_and_load_from_base_dir(base_path)
            
            if not file_path.exists():
                # If the specific 'file' argument is a directory or missing file, 
                # we default to reading from .aliens.db if it exists.
                data_file = base_path / "data.json"  # Fallback: use existing test folder structure logic
            
            try:
                with open(file_path, "r") as f:
                    self.data = json.load(f)
                return True
            except (FileNotFoundError, IOError):
                print("Warning: Could not load data from the expected file. Using fallback 'data.json' if available.")

        except Exception as e:
            # If any other error occurs during loading or saving, we fail silently to prevent crashes in production mode
            return False
            
    def _load_file_from_absolute_path(self, base_dir: Path, filename_or_key: str) -> None | bool:
    def _find_and_load_from_base_dir(self, base_path: Path) -> str | None:
        """
        Attempts to locate 'data.json' within a specific directory structure under src/.
        
        This method recursively searches for the JSON file and its parent directories. 
        It prioritizes finding an explicit key argument if available over looking at absolute paths.
        
        Returns:
            str | None: Path or None if no valid data source is found, otherwise returns a string path to the target.
        """
        # If provided as an explicit filename/key, use that directly (with fallback logic)
        if isinstance(filename_or_data_key, str):
            try:
                result = self._load_file_from_absolute_path(base_path, str(filename_or_data_key))
                return result
            
        # Fallback to directory-based search using the base path structure
        target_dir = Path(os.getcwd()) / "src"

        def _search_recursive(path_to_check):
            """Recursively check a given directory for data.json and its contents."""
            if not os.path.exists(path_to_check) or (path_to_check != self.data_file):  # Exclude the file itself from search results unless it's the target key
                return None
            
            current = path_to_check.parent
            while True:
                try:
                    entry_path = Path(current).resolve()
                    
                    if not os.path.isdir(entry_path) or (entry_path == self.data_file and str(filename_or_data_key)):  # Skip the file itself in this context
                        
                        result = _load_json_from_directory(Path(current), filename_or_data_key, current / "data.json")
                        
                        if result is None:
                            return None
                
                except Exception as e:
                    continue
                    
                path_to_check = entry_path

            return str(path_to_check)

        try:
            # First try to find the file by name in src/ (or its subdirectories recursively)
            data_file = _search_recursive(base_path / "data.json")
            
            if not data_file:
                # If we couldn't find it, search for 'aliens.db' as a fallback since that's what was mentioned earlier
                result = self._load_from_database()

        except FileNotFoundError:
            print("Warning: Could not locate 'data.json'. Attempting to load from database file...")
            
            # Load the existing .db file if it exists under
from typing import Any, Dict, Optional
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_data_key: str | None) -> bool:
        """
        Attempts to load data from a JSON file under src/.
        
        Args:
            filename_or_data_key (str | None): Path or key name. If provided as path, loads that exact file. 
                                        Otherwise, attempts to detect test folder structure and look for 'data.json' in the root of `src/`.

        Returns:
            bool: True if successfully loaded data (JSON parseable), False otherwise based on FileNotFoundError, IOError, or JSON errors.
            
        Note: This function mirrors the behavior of AlienDatabase.__load__ but handles paths more gracefully and ensures consistent fallbacks for test folders under src/.
        """
        base_path = Path(os.getcwd()) / "src"

        # Check if an explicit filename was provided (e.g., 'test_data.json')
        if os.path.abspath(filename_or_data_key):
            try:
                file_path = self._load_file_from_absolute_path(base_path, str(filename_or_data_key))
                return True  # File exists and is valid JSON
            except Exception as e:
                print(f"Warning: Failed to load from explicit path '{filename_or_data_key}': {e}")

        try:
            file_path = self._find_and_load_from_base_dir(base_path)
            
            if not file_path.exists():
                # If the specific 'file' argument is a directory or missing file, 
                # we default to reading from .aliens.db if it exists.
                data_file = base_path / "data.json"  # Fallback: use existing test folder structure logic
            
            try:
                with open(file_path, "r") as f:
                    self.data = json.load(f)
                return True
            except (FileNotFoundError, IOError):
                print("Warning: Could not load data from the expected file. Using fallback 'data.json' if available.")

        except Exception as e:
            # If any other error occurs during loading or saving, we fail silently to prevent crashes in production mode
            return False
            
    def _load_file_from_absolute_path(self, base_dir: Path, filename_or_key: str) -> None | bool:
        """
        Attempts to locate '
