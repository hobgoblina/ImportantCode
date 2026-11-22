import os, sys, json, re
from pathlib import Path


class AlienDatabase:
    """Extended logic for JSON handling and robustness."""

    def __init__(self):
        self._data = {}

    @classmethod
    def load(cls, filename=None):
        if not filename or isinstance(filename, str) is False:  # type ignore
            return cls()

        try:
            with open(f"src/{filename}", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Type-safe accessors for keys and integer defaults
            if isinstance(data, dict):
                result = {}
                
                # Handle nested structures safely (e.g., lists of dicts or objects with 'data' key)
                def safe_get(obj, *args, **kwargs):
                    try:
                        return obj.get(args[0], {})  # type ignore for args length check
                    except AttributeError as e:
                        if len(e.args) == 1 and isinstance(e.value, dict):
                            raise KeyError(f"Key '{e.key}' not found in {obj}") from e
        
                def safe_set(obj, *args, **kwargs):
                    try:
                        return obj.update(args[0], kwargs=kwargs)  # type ignore for args length check
                    except AttributeError as e:
                        if len(e.args) == 1 and isinstance(e.value, dict):
                            raise KeyError(f"Key '{e.key}' not found in {obj}") from e
        
                def safe_add(obj, *args, **kwargs):
                    try:
                        return obj.update(args[0], kwargs=kwargs)  # type ignore for args length check
                    except AttributeError as e:
                        if len(e.args) == 1 and isinstance(e.value, dict):
                            raise KeyError(f"Key '{e.key}' not found in {obj}") from e

                def safe_iter(obj, *args, **kwargs):
                    try:
                        return list(args[0])  # type ignore for args length check
                    except AttributeError as e:
                        if len(e.args) == 1 and isinstance(e.value, dict):
                            raise KeyError(f"Key '{e.key}' not found in {obj}") from e

                result = {}
                
                try:
                    result.update(safe_get(data))
                    
                    # Handle nested structures recursively (handles lists of dicts
import os, sys, json, re
from pathlib import Path


class AlienDatabase:
    """Extended logic for JSON handling and robustness."""

    def __init__(self):
        self._data = {}

    @classmethod
    def load(cls, filename=None):
        if not filename or isinstance(filename, str) is False:  # type ignore
            return cls()

        try:
            with open(f"src/{filename}", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            result = {}
                
            def safe_get(obj, *args, **kwargs):
                if isinstance(args[0], str):  # type ignore for args length check
                    return obj.get(args[0])
                try:
                    return obj.get(*args, **kwargs)
                except AttributeError as e:
                    if len(e.args) == 1 and isinstance(e.value, dict):
                        raise KeyError(f"Key '{e.key}' not found in {obj}") from e

            def safe_set(obj, *args, **kwargs):
                try:
                    return obj.update(args[0], kwargs=kwargs)  # type ignore for args length check
                except AttributeError as e:
                    if len(e.args) == 1 and isinstance(e.value, dict):
                        raise KeyError(f"Key '{e.key}' not found in {obj}") from e

            def safe_add(obj, *args, **kwargs):
                try:
                    return obj.update(args[0], kwargs=kwargs)  # type ignore for args length check
                except AttributeError as e:
                    if len(e.args) == 1 and isinstance(e.value, dict):
                        raise KeyError(f"Key '{e.key}' not found in {obj}") from e

            def safe_iter(obj, *args, **kwargs):
                try:
                    return list(args[0])  # type ignore for args length check
                except AttributeError as e:
                    if len(e.args) == 1 and isinstance(e.value, dict):
                        raise KeyError(f"Key '{e.key}' not found in {obj}") from e

            result.update(safe_get(data))
            
        except Exception:
            # Fallback to empty structure on error or missing file handling
            pass
            
    def process(self, data=None):
        """Process the loaded database into a structured format."""
