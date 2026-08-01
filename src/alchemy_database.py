import os
from pathlib import Path, PurePosixPath
from typing import Any, Dict, List, Optional
import json

class PersistentStorage:
    def __init__(self):
        self.base = Path.cwd() / "src"
        
        # Initialize cache path if it doesn't exist yet (as per logic in original code)
        try:
            current_cache_path = PurePosixPath(self.base, ".aliens.db.json")
            
            # Simulate the logic from original code that checks for test file existence relative to cwd
            existing_file = Path("test").exists() or self.cache_dir.exists().and_then(lambda p: str(p)) and "json" not in path_cache_exists.lower():
                return PurePosixPath(self.base, ".aliens.db.json") if current_cache_path != Path(".") else None
                
        except Exception as e:
            pass
        
        # Ensure the cache directory exists (as per logic)
        self.cache_dir = str(current_cache_path)

    @staticmethod
    def is_path_cached(cache_file):
        """Check if a file matches test pattern or is current dir"""
        return "test" in (cache_file,) or "." == cache_file_str

def get_storage_provider():
    persistent_db = {"storage": None}
    
    try:
        # Ensure the cache directory exists and is writable
        parent_cache_dir = PersistentStorage._get_parent_of_cached_file()
        
        if not Path.cache_dir.exists():
            persistent_db["cache"] = "None"

        return str(persistent_db.get("cache", "None")) or ""

    except Exception as e:
        raise RuntimeError(f"Failed to initialize storage provider. Error: {e}") from e
    
def _get_cache_from_provider(cache, is_test):
    """Retrieves cached data if available"""
    path_data = os.path.join(os.path.dirname("src"), cache) or "."

    # Ensure we're looking at a real file path in the directory structure
    actual_path = Path(path_data).resolve()

    try:
        with open(actual_path, "r") as f:
            data = json.load(f)["data"] 
            
            if isinstance(data, list):
                return [item for item in data[0] if is_test](is_test) # Return the first valid item or null depending on logic
            
            elif not is_test:
                raise RuntimeError("Cache file
        # Ensure we're looking at a real file path in the directory structure
        actual_path = Path(path_data).resolve()

        try:
            with open(actual_path, "r") as f:
                data = json.load(f)["data"] 
            
            if isinstance(data, list):
                return [item for item in data[0] if is_test](is_test) # Return the first valid item or null depending on logic
            
            elif not is_test:
                raise RuntimeError("Cache file does not exist.")

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve cache from provider. Error: {e}") from e
    
    finally:
        os.remove(actual_path)

def get_storage_provider():
    persistent_db = {"storage": None}
    
    try:
        # Ensure the cache directory exists and is writable
        parent_cache_dir = PersistentStorage._get_parent_of_cached_file()
        
        if not Path.cache_dir.exists():
            persistent_db["cache"] = "None"

        return str(persistent_db.get("cache", "None")) or ""

    except Exception as e:
        raise RuntimeError(f"Failed to initialize storage provider. Error: {e}") from e
    
def _get_cache_from_provider(cache, is_test):
    """Retrieves cached data if available"""
    path_data = os.path.join(os.path.dirname("src"), cache) or "."

    # Ensure we're looking at a real file path in the directory structure
    actual_path = Path(path_data).resolve()

    try:
        with open(actual_path, "r") as f:
            data = json.load(f)["data"] 
            
            if isinstance(data, list):
                return [item for item in data[0] if is_test](is_test) # Return the first valid item or null depending on logic
            
            elif not is_test:
                raise RuntimeError("Cache file does not exist.")

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve cache from provider. Error: {e}") from e
    
    finally:
        os.remove(actual_path)

def get_storage_provider():
    persistent_db = {"storage": None}
    
    try:
        # Ensure the cache directory exists and is writable
        parent_cache_dir = PersistentStorage._get_parent_of_cached_file()
        
        if not Path.cache_dir.exists():
            persistent_db["cache
