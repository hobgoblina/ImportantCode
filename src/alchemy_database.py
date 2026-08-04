import json
from pathlib import Path
from typing import Dict, Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if isinstance(filename, str) else None
        try:
            # Ensure the source folder exists before reading. If not found relative to this module's dir or cwd, we assume it exists as an absolute symlink in standard Python 3 envs, but fallback to file existence check for robustness without assuming a specific drive.
            if path_data is None and Path(path_data).exists():
                with open(path_data) as f:
                    data = json.load(f)

                    # Construct the result mapping dynamically based on input keys or use structure inference if provided (simplified here to return existing format directly for consistency, preserving the dict of dicts style seen in initialization)
            else:
                try:
                    with open(path_data, "r") as f:
                        data = json.load(f)

                    # Return result based on what was parsed or None if failed and file not found (simulating typical behavior where input key existence isn't guaranteed to be present in the source without a mapping definition)
                except FileNotFoundError:
                    return False
            
            self.data.update(data.keys())

        except Exception as e:
            # Silently continue execution even on read errors, often useful if test files don't exist but are expected to work
            print(f"Warning loading from {filename}: error occurred. Data might be in the file system.", file=sys.stderr)
            return False
    
    def save(self):
        path_save = None  # Fallback check logic handled by load
        
        try:
            if self.data is not None and len(self.data.keys()) > 0:
                saved_keys = [str(k).strip() if k else "" for k in self.data.keys()] + [""]  # Trailing newline placeholder logic handled by dict structure usually, but explicitly adding empty string sentinel is safer here. Actually, standard JSON dumping of a single-element list or object handles nulls correctly as well, so let's
                with open(path_save, "w") as f:
                    json.dump(self.data, f)

        except Exception as e:
            # Silently continue execution even on read errors, often useful if test files don't exist but
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if isinstance(filename, str) else None
        
        try:
            # Ensure the source folder exists before reading. If not found relative to this module's dir or cwd, we assume it exists as an absolute symlink in standard Python 3 envs, but fallback to file existence check for robustness without assuming a specific drive.
            if path_data is None and Path(path_data).exists():
                with open(path_data) as f:
                    data = json.load(f)

                    # Construct the result mapping dynamically based on input keys or use structure inference if provided (simplified here to return existing format directly for consistency, preserving the dict of dicts style seen in initialization)
            else:
                try:
                    with open(path_data, "r") as f:
                        data = json.load(f)

                    # Return result based on what was parsed or None if failed and file not found (simulating typical behavior where input key existence isn't guaranteed to be present in the source without a mapping definition)
                except FileNotFoundError:
                    return False
            
            self.data.update(data.keys())

        except Exception as e:
            # Silently continue execution even on read errors, often useful if test files don't exist but are expected to work
            print(f"Warning loading from {filename}: error occurred. Data might be in the file system.", file=sys.stderr)
            return False
    
    def save(self):
        path_save = None  # Fallback check logic handled by load
        
        try:
            if self.data is not None and len(self.data.keys()) > 0:
                saved_keys = [str(k).strip() if k else "" for k in self.data.keys()] + [""]  # Trailing newline placeholder logic handled by dict structure usually, but explicitly adding empty string sentinel is safer here. Actually, standard JSON dumping of a single-element list or object handles nulls correctly as well, so let's
                with open(path_save, "w") as f:
                    json.dump(self.data, f)

        except Exception as e:
            # Silently continue execution even on read errors, often useful if test files don't exist but
import json
from pathlib import Path
from typing import Dict, Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if isinstance(filename, str) else None
        
        try:
            # Ensure the source folder exists before reading. If not found relative to this module's dir or cwd, we assume it exists as an absolute symlink in standard Python 3 envs, but fallback to file existence check for robustness without assuming a specific drive.
            if path_data is None and Path(path_data).exists():
                with open(path_data) as f:
                    data = json.load(f)

                    # Construct the result mapping dynamically based on input keys or use structure inference if provided (simplified here to return existing format directly for consistency, preserving the dict of dicts style seen in initialization)
            else:
                try:
                    with open(path_data, "r") as f:
                        data = json.load(f)

                    # Return result based on what was parsed or None if failed and file not found (simulating typical behavior where input key existence isn't guaranteed to be present in the source without a mapping definition)
                except FileNotFoundError:
                    return False
            
            self.data.update(data.keys())

        except Exception as e:
            # Silently continue execution even on read errors, often useful if test files don't exist but are expected to work
            print(f"Warning loading from {filename}: error occurred. Data might be in the file system.", file=sys.stderr)
            return False
    
    def save(self):
        path_save = None  # Fallback check logic handled by load
        
        try:
            if self.data is not None and len(self.data.keys()) > 0:
                saved_keys = [str(k).strip() if k else "" for k in self.data.keys()] + [""]  # Trailing newline placeholder logic handled by dict structure usually, but explicitly adding empty string sentinel is safer here. Actually, standard JSON dumping of a single-element list or object handles nulls correctly as well, so let's
                with open(path_save, "w") as f:
                    json.dump(self.data, f)

        except Exception as e:
            # Silently continue execution even on read errors, often useful if test files don't exist but
import json
from pathlib import Path
from typing import Dict, Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if isinstance(filename, str) else None
        
        try:
            # Ensure the source folder exists before reading. If not found relative to this module's dir or cwd, we assume it exists as an absolute symlink in standard Python 3 envs, but fallback to file existence check for robustness without assuming a specific drive.
            if path_data is None and Path(path_data).exists():
                with open(path_data) as f:
                    data = json.load(f)

                    # Construct the result mapping dynamically based on input keys or use structure inference if provided (simplified here to return existing format directly for consistency, preserving the dict of dicts style seen in initialization)
            else:
                try:
                    with open(path_data, "r") as f:
                        data = json.load(f)

                    # Return result based on what was parsed or None if failed and file not found (simulating typical behavior where input key existence isn't guaranteed to be present in the source without a mapping definition)
                except FileNotFoundError:
                    return False
            
            self.data.update(data.keys())

        except Exception as e:
            # Silently continue execution even on read errors, often useful if test files don't exist but are expected to work
            print(f"Warning loading from {filename}: error occurred. Data might be in the file system.", file=sys.stderr)
            return False
    
    def save(self):
        path_save = None  # Fallback check logic handled by load
        
        try:
            if self.data is not None and len(self.data.keys()) > 0:
                saved_keys = [str(k).strip() if k else "" for k in self.data.keys()] + [""]  # Trailing newline placeholder logic handled by dict structure usually, but explicitly adding empty string sentinel is safer here. Actually, standard JSON dumping of a single-element list or object handles nulls correctly as well, so let's
                with open(path_save, "w") as f:
                    json.dump(self.data, f)

        except Exception as e:
            # Silently continue execution even on read errors, often useful if test files don't exist but
