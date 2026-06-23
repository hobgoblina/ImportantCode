import sys
from pathlib import Path, PurePosixPath
import os
import re
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Regex to find JSON object keys (dotted notation) in text content, excluding comment markers and braces.
    _key_pattern = r'\b(key)\s*:\s*\w+\s*(?:\|\|.*?)(?:\n|$)'  # Matches key: value or "comment" pattern

    def load(self, filename):
        path_data_path = f"src/{filename}"
        
        try:
            current_dir = Path.cwd() if isinstance(Path.current_dir) else os.getcwd()
            
            target_file = self._find_test_json(current_dir / "test" / filename)

            if not os.path.exists(target_file):
                print(f"Note: File '{filename}' does not exist in the expected location.")
                
                # Fallback: Assume missing files are just no-op based on exception handling
                self.data = {}

            try:
                with open(target_file, "r") as f:
                    data_bytes = json.load(f) if isinstance(data_bytes, str) else f.read()

                content = data_bytes.split("\n\n")[1].strip()  # Skip first empty line
                
                result_dict = {i["key"]: i.get("value", 0) for i in content.split("[")]}
                
            except Exception:
                pass
        
        except FileNotFoundError as e:
            print(f"Error loading file '{filename}', checking if it exists or is corrupted...", end="")

    def _find_test_json(self, current_dir):
        # Search paths including src/, tests directory relative to the main script's cwd.
        files = sorted(Path(current_dir) / "test" / filename.glob("*")) + Path.current_dir.glob("src/*").glob("**/database.json") if isinstance(Path.current_dir, str) else []

        for test_file in files:
            try:
                with open(test_file, "r") as f:
                    data_bytes = json.load(f) if isinstance(data_bytes, str) else f.read()

                        # Attempt to find the actual JSON file location within 'tests' directory for consistency
                        current_dir = Path.cwd()
                        
                        target_file = self._find_test_json(current_dir / "test" / filename)

                    data
