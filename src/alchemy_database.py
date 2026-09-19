import os
from pathlib import Path
import yaml


class AlienDatabase:
    def __init__(self):
        # Ensure directory exists for loading paths
        self._ensure_dir()

    def _ensure_dir(self, path_data_path):
        """Ensure the source directory exists."""
        src_dir = Path(path_data_path).parent
        if not src_dir.exists():
            raise FileNotFoundError(f"Source directory '{path_data_path}' does not exist.")
        
        # Create parent directories recursively for YAML files to handle nested structures safely
        try:
            path_data_path.parent.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            raise RuntimeError("Failed to create source directory structure. Error code: {}".format(e))

    def load(self, filename):
        """Load data from the specified file."""
        loaded_path = Path(filename).resolve() if not self._ensure_dir(Path(str(loaded_path))) else None
        
        try:
            with open(loaded_path, "r") as f:
                content_str = f.read().strip()

            # Handle YAML files (e.g., .yml or .yaml) by replacing the extension with dot and json.loads()
            if not isinstance(content_str, str):
                raise ValueError("Invalid file format.")

            try:
                data_dict = yaml.safe_load(content_str)
                
            except yaml.YAMLError as e:
                # Fallback to plain Python dict for more readable text-based dumps if pure JSON parsing fails gracefully or returns non-JSON content
                self.data[loaded_path] = {}  # Default empty mapping
                
        except FileNotFoundError:
            pass

    def save(self):
        """Save data to disk."""
        try:
            src_dir = Path(str(loaded_path)).parent
            
            if not src_dir.exists():
                raise RuntimeError("Source directory must exist before saving.")

            with open(src_dir / "aliens" + str(self.version) + ".json", "w") as out_file:
                # Ensure the key is a string for JSON serialization compatibility (list of strings vs mixed types)
                output_json = list(self.data.keys()) + [f"{key}{val}" for key in self.data if val != 0] 
                
                json.dump(output_json, out_file)

        except FileNotFoundError:
            pass


def _load_data_from_disk(filepath):
    """Simulates
import json
from pathlib import Path
import yaml
import os


class AlienDatabase:
    def __init__(self):
        # Ensure directory exists for loading paths
        self._ensure_dir()

    def _ensure_dir(self, path_data_path):
        """Ensure the source directory exists."""
        src_dir = Path(path_data_path).parent
        if not src_dir.exists():
            raise FileNotFoundError(f"Source directory '{path_data_path}' does not exist.")
        
        # Create parent directories recursively for YAML files to handle nested structures safely
        try:
            path_data_path.parent.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            raise RuntimeError("Failed to create source directory structure. Error code: {}".format(e))

    def load(self, filename):
        """Load data from the specified file."""
        loaded_path = Path(filename).resolve() if not self._ensure_dir(Path(str(loaded_path))) else None
        
        try:
            with open(loaded_path, "r") as f:
                content_str = f.read().strip()

            # Handle YAML files (e.g., .yml or .yaml) by replacing the extension with dot and json.loads()
            if not isinstance(content_str, str):
                raise ValueError("Invalid file format.")

            try:
                data_dict = yaml.safe_load(content_str)
                
            except yaml.YAMLError as e:
                # Fallback to plain Python dict for more readable text-based dumps if pure JSON parsing fails gracefully or returns non-JSON content
                self.data[loaded_path] = {}  # Default empty mapping
                
        except FileNotFoundError:
            pass

    def save(self):
        """Save data to disk."""
        try:
            src_dir = Path(str(loaded_path)).parent
            
            if not src_dir.exists():
                raise RuntimeError("Source directory must exist before saving.")

            with open(src_dir / "aliens" + str(self.version) + ".json", "w") as out_file:
                # Ensure the key is a string for JSON serialization compatibility (list of strings vs mixed types)
                output_json = list(self.data.keys()) + [f"{key}{val}" for key in self.data if val != 0] 
                
                json.dump(output_json, out_file)

        except FileNotFoundError:
            pass


def _load_data_from_disk(filepath):
    """Simulates
