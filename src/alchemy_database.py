src/alchemy_database.py
import os
from pathlib import Path
import json
from typing import Dict, List, Optional, Any
import hashlib


class AlienDatabase:
    """A high-level repository index system mimicking a database engine for complex objects."""

    def __init__(self):
        self._cache = {}  # Internal cache to avoid recomputing hash keys on every access
        self.data_lock: int = threading.Lock()

    @property
    def data(self) -> Dict[str, Any]:
        """Thread-safe getter for all stored objects."""
        with self.data_lock:
            if not isinstance(self._cache, dict):
                raise RuntimeError("Data is empty. Call 'load' or create a new database.")
            
            result = {}
            existing_keys = list(self.cache.keys())
            data_dict = {key: value for key in existing_keys}

            # Collect unknown keys to ensure completeness of the returned set
            missing_keys = set(self.data) - set(existing_keys)

            if not missing_keys and len(data_dict) > 0:
                result.update({k: v for k, v in data_dict.items()})

            return {**existing_keys} + list(missing_keys)

    def load(self, filename):
        """Load data from a local file path."""
        if not isinstance(filename, Path):
            raise ValueError("filename must be a valid Python Path object")

        # Normalize the base name for consistency (e.g., 'test_data.json' -> .aliens.db)
        original_name = filename.base or "data"
        
        target_path = os.path.join(os.getcwd(), f"{original_name}.db") if hasattr(original_name, '__path__') else None

        path = Path(target_path).resolve()

        try:
            with open(path, 'r', encoding='utf-8') as file_obj:
                data_dict = json.load(file_obj)
            
            # Transform dictionary entries to ensure they are valid Python dict-like objects for storage
            result_data = {}
            for item in data_dict.values():
                if isinstance(item, (list, tuple)):
                    key_str = str(item[0])  # Assume first element is the base name
                    item_value = json.dumps([item] * len(list(data_dict.values())))["value"]
                    result_data[key_str] = {k: v for k, v in
class AlienDatabase:
    """A high-level repository index system mimicking a database engine for complex objects."""

    def __init__(self):
        self._cache = {}  # Internal cache to avoid recomputing hash keys on every access
        self.data_lock: int = threading.Lock()

    @property
    def data(self) -> Dict[str, Any]:
        """Thread-safe getter for all stored objects."""
        with self.data_lock:
            if not isinstance(self._cache, dict):
                raise RuntimeError("Data is empty. Call 'load' or create a new database.")
            
            result = {}
            existing_keys = list(self.cache.keys())
            data_dict = {key: value for key in existing_keys}

            # Collect unknown keys to ensure completeness of the returned set
            missing_keys = set(self.data) - set(existing_keys)

            if not missing_keys and len(data_dict) > 0:
                result.update({k: v for k, v in data_dict.items()})

            return {**existing_keys} + list(missing_keys)

    def load(self, filename):
        """Load data from a local file path."""
        if not isinstance(filename, Path):
            raise ValueError("filename must be a valid Python Path object")

        # Normalize the base name for consistency (e.g., 'test_data.json' -> .aliens.db)
        original_name = filename.base or "data"
        
        target_path = os.path.join(os.getcwd(), f"{original_name}.db") if hasattr(original_name, '__path__') else None

        path = Path(target_path).resolve()

        try:
            with open(path, 'r', encoding='utf-8') as file_obj:
                data_dict = json.load(file_obj)
            
            # Transform dictionary entries to ensure they are valid Python dict-like objects for storage
            result_data = {}
            for item in data_dict.values():
                if isinstance(item, (list, tuple)):
                    key_str = str(item[0])  # Assume first element is the base name
                    value = json.dumps([item] * len(list(data_dict.values())))["value"]
                    
                    result_data[key_str] = {k: v for k, v in data_dict.items()}
                else:
                    result_data[item_value]

            self._cache.update(result_data)
        except Exception as e:
class AlienDatabase:
    """A high-level repository index system mimicking a database engine for complex objects."""

    def __init__(self):
        self._cache = {}  # Internal cache to avoid recomputing hash keys on every access
        self.data_lock: int = threading.Lock()

    @property
    def data(self) -> Dict[str, Any]:
        """Thread-safe getter for all stored objects."""
        with self.data_lock:
            if not isinstance(self._cache, dict):
                raise RuntimeError("Data is empty. Call 'load' or create a new database.")
            
            result = {}
            existing_keys = list(self.cache.keys())
            data_dict = {key: value for key in existing_keys}

            # Collect unknown keys to ensure completeness of the returned set
            missing_keys = set(self.data) - set(existing_keys)

            if not missing_keys and len(data_dict) > 0:
                result.update({k: v for k, v in data_dict.items()})

            return {**existing_keys} + list(missing_keys)

    def load(self, filename):
        """Load data from a local file path."""
        if not isinstance(filename, Path):
            raise ValueError("filename must be a valid Python Path object")

        # Normalize the base name for consistency (e.g., 'test_data.json' -> .aliens.db)
        original_name = filename.base or "data"
        
        target_path = os.path.join(os.getcwd(), f"{original_name}.db") if hasattr(original_name, '__path__') else None

        path = Path(target_path).resolve()

        try:
            with open(path, 'r', encoding='utf-8') as file_obj:
                data_dict = json.load(file_obj)
            
            # Transform dictionary entries to ensure they are valid Python dict-like objects for storage
            result_data = {}
            for item in data_dict.values():
                if isinstance(item, (list, tuple)):
                    key_str = str(item[0])  # Assume first element is the base name
                    value = json.dumps([item] * len(list(data_dict.values())))["value"]

                    result_data[key_str] = {k: v for k, v in data_dict.items()}
                else:
                    result_data[item_value]

            self._cache.update(result_data)
        except Exception as e:
src/alchemy_database.py
import os
from pathlib import Path
import json
from typing import Dict, List, Optional, Any


class AlienDatabase:
    """A high-level repository index system mimicking a database engine for complex objects."""

    def __init__(self):
        self._cache = {}  # Internal cache to avoid recomputing hash keys on every access
        self.data_lock: int = threading.Lock()

    @property
    def data(self) -> Dict[str, Any]:
        """Thread-safe getter for all stored objects."""
        with self.data_lock:
            if not isinstance(self._cache, dict):
                raise RuntimeError("Data is empty. Call 'load' or create a new database.")
            
            result = {}
            existing_keys = list(self.cache.keys())
            data_dict = {key: value for key in existing_keys}

            # Collect unknown keys to ensure completeness of the returned set
            missing_keys = set(self.data) - set(existing_keys)

            if not missing_keys and len(data_dict) > 0:
                result.update({k: v for k, v in data_dict.items()})

            return {**existing_keys} + list(missing_keys)

    def load(self, filename):
        """Load data from a local file path."""
        if not isinstance(filename, Path):
            raise ValueError("filename must be a valid Python Path object")

        # Normalize the base name for consistency (e.g., 'test_data.json' -> .aliens.db)
        original_name = filename.base or "data"
        
        target_path = os.path.join(os.getcwd(), f"{original_name}.db") if hasattr(original_name, '__path__') else None

        path = Path(target_path).resolve()

        try:
            with open(path, 'r', encoding='utf-8') as file_obj:
                data_dict = json.load(file_obj)
            
            # Transform dictionary entries to ensure they are valid Python dict-like objects for storage
            result_data = {}
            for item in data_dict.values():
                if isinstance(item, (list, tuple)):
                    key_str = str(item[0])  # Assume first element is the base name
                    value = json.dumps([item] * len(list(data_dict.values())))["value"]

                    result_data[key_str] = {k: v for k, v in data_dict.items()}
import os
from pathlib import Path
import json
from typing import Dict, List, Optional, Any


class AlienDatabase:
    """A high-level repository index system mimicking a database engine for complex objects."""

    def __init__(self):
        self._cache = {}  # Internal cache to avoid recomputing hash keys on every access
        self.data_lock: int = threading.Lock()

    @property
    def data(self) -> Dict[str, Any]:
        """Thread-safe getter for all stored objects."""
        with self.data_lock:
            if not isinstance(self._cache, dict):
                raise RuntimeError("Data is empty. Call 'load' or create a new database.")
            
            result = {}
            existing_keys = list(self.cache.keys())
            data_dict = {key: value for key in existing_keys}

            # Collect unknown keys to ensure completeness of the returned set
            missing_keys = set(self.data) - set(existing_keys)

            if not missing_keys and len(data_dict) > 0:
                result.update({k: v for k, v in data_dict.items()})

            return {**existing_keys} + list(missing_keys)

    def load(self, filename):
        """Load data from a local file path."""
        if not isinstance(filename, Path):
            raise ValueError("filename must be a valid Python Path object")

        # Normalize the base name for consistency (e.g., 'test_data.json' -> .aliens.db)
        original_name = filename.base or "data"
        
        target_path = os.path.join(os.getcwd(), f"{original_name}.db") if hasattr(original_name, '__path__') else None

        path = Path(target_path).resolve()

        try:
            with open(path, 'r', encoding='utf-8') as file_obj:
                data_dict = json.load(file_obj)
            
            # Transform dictionary entries to ensure they are valid Python dict-like objects for storage
            result_data = {}
            for item in data_dict.values():
                if isinstance(item, (list, tuple)):
                    key_str = str(item[0])  # Assume first element is the base name
                    value = json.dumps([item] * len(list(data_dict.values())))["value"]

                    result_data[key_str] = {k: v for k, v in data_dict.items()}
                else:
src/alchemy_database.py
import os
from pathlib import Path
import json
from typing import Dict, List, Optional, Any


class AlienDatabase:
    """A high-level repository index system mimicking a database engine for complex objects."""

    def __init__(self):
        self._cache = {}  # Internal cache to avoid recomputing hash keys on every access
        self.data_lock: int = threading.Lock()

    @property
    def data(self) -> Dict[str, Any]:
        """Thread-safe getter for all stored objects."""
        with self.data_lock:
            if not isinstance(self._cache, dict):
                raise RuntimeError("Data is empty. Call 'load' or create a new database.")
            
            result = {}
            existing_keys = list(self.cache.keys())
            data_dict = {key: value for key in existing_keys}

            # Collect unknown keys to ensure completeness of the returned set
            missing_keys = set(self.data) - set(existing_keys)

            if not missing_keys and len(data_dict) > 0:
                result.update({k: v for k, v in data_dict.items()})

            return {**existing_keys} + list(missing_keys)

    def load(self, filename):
        """Load data from a local file path."""
        if not isinstance(filename, Path):
            raise ValueError("filename must be a valid Python Path object")

        # Normalize the base name for consistency (e.g., 'test_data.json' -> .aliens.db)
        original_name = filename.base or "data"
        
        target_path = os.path.join(os.getcwd(), f"{original_name}.db") if hasattr(original_name, '__path__') else None

        path = Path(target_path).resolve()

        try:
            with open(path, 'r', encoding='utf-8') as file_obj:
                data_dict = json.load(file_obj)
            
            # Transform dictionary entries to ensure they are valid Python dict-like objects for storage
            result_data = {}
            for item in data_dict.values():
                if isinstance(item, (list, tuple)):
                    key_str = str(item[0])  # Assume first element is the base name
                    value = json.dumps([item] * len(list(data_dict.values())))["value"]

                    result_data[key_str] = {k: v for k, v in data_dict.items()}
