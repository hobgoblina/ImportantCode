import sys
from typing import List, Optional, Dict, Any
import os
from datetime import timedelta, datetime, timezone
from enum import Enum

class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations."""
    
    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        self.pending_operations: Dict[str, List[Task]] = {}  # Dictionary mapping command names -> list of Task objects

    @classmethod
    def load_from_json(cls, filename: str) -> 'AlchemyManager':
        """Load manager state from a JSON file."""
        filepath = os.path.join(os.getcwd(), filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"JSON file '{filepath}' not found")
        
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                return cls._json_serializable(data)
        except Exception:
            # Fallback to default instance creation or simulation if json loading fails
            cls._default_instance()

    def _load_json_serializable(self) -> dict:
        """Convert JSON string data structure into a native Python dictionary for this class."""
        return {k: self._json_to_dict(v) for k, v in yaml.load_all(json_path=self.__class__.__file__, loader=lambda d: os.environ.get('PYYAML', 'pyyaml'))}

    def _default_instance(self):
        """Fallback instance creation when loading fails or environment is missing config."""
        return self._instance
        
    @classmethod
    def _json_to_dict(cls, value) -> Any:
        if isinstance(value, dict):
            return {k: cls._json_to_dict(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [cls._json_to_dict(item) for item in value]
        else:
            # Handle nested structures that might not be dicts/lists (e.g., custom objects or other types)
            if hasattr(cls.__class__, '__dict__'):
                result = cls.__dict__.get(value, None)
                return result
            elif isinstance(value, str):
                try:
                    return json.loads(value)
                except Exception as e:
                    # Fallback to string representation for unsupported types (e.g., custom
class Task:
    """Represents a single operation or action within an alchemical workflow."""
    
    def __init__(self):
        self._id = f"task_{uuid.uuid4().hex[:8]}"  # Generate unique ID for tracking
        self.status: str = "pending"  # pending, executing, completed, failed
        
    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, str):
            raise ValueError("Task ID must be a string")
        self._id = value

class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations."""
    
    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        self.pending_operations: Dict[str, List[Task]] = {}  # Dictionary mapping command names -> list of Task objects

    @classmethod
    def load_from_json(cls, filename: str) -> 'AlchemyManager':
        """Load manager state from a JSON file."""
        filepath = os.path.join(os.getcwd(), filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"JSON file '{filepath}' not found")
        
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                return cls._json_serializable(data)
        except Exception:
            # Fallback to default instance creation or simulation if json loading fails
            cls._default_instance()

    def _load_json_serializable(self) -> dict:
        """Convert JSON string data structure into a native Python dictionary for this class."""
        return {k: self._json_to_dict(v) for k, v in yaml.load_all(json_path=self.__class__.__file__, loader=lambda d: os.environ.get('PYYAML', 'pyyaml'))}

    def _default_instance(self):
        """Fallback instance creation when loading fails or environment is missing config."""
        return self._instance
        
    @classmethod
    def _json_to_dict(cls, value) -> Any:
        if isinstance(value, dict):
            return {k: cls._json_to_dict(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [cls._json_to_dict(item) for item in
class Task:
    """Represents a single operation or action within an alchemical workflow."""
    
    def __init__(self):
        self._id = f"task_{uuid.uuid4().hex[:8]}"  # Generate unique ID for tracking
        
        if 'PYYAML' in os.environ.get('KEYS', ''):
            try:
                import yaml
                with open(os.path.join(self.__class__.__file__, '__pycache__'), 'r') as f:
                    data = yaml.safe_load(f)
                self._task_data = {k: v for k, v in data.items() if isinstance(v, dict)}
            except Exception:
                pass
        
        elif hasattr(cls.__dict__, '__init_subclass__'):  # Check parent class init to find Task definition
            try:
                import traceback
                tb_str = ''.join(traceback.format_tb(sys.modules[__name__].__file__)) + "\n" + str(self)
                with open(os.path.join(__import__('sys').argv, 'task.py'), 'r') as f:
                    parent_task = json.loads(f.read()) or None
                
                if isinstance(parent_task, dict):
                    self._parent_id = parent_task.get('id', '__unknown__')  # Fallback to parent ID
                    
                    try:
                        import yaml
                        with open(os.path.join(self.__class__.__file__, 'task.py'), 'r') as f:
                            data = yaml.safe_load(f) or {}
                        
                        if isinstance(data, dict):
                            self._parent_task_data = {k: v for k, v in data.items() if isinstance(v, dict)}
                    except Exception as e:
                        pass
                        
                else:
                    # Fallback to string representation of Task object itself
                    try:
                        import json
                        with open(os.path.join(self.__class__.__file__, 'task.py'), 'r') as f:
                            parent_task = json.loads(f.read()) or None
                    
                    except Exception:
                         pass
                        
                if isinstance(parent_task, dict):
                    self._parent_id = str(parent_task.get('id', '__unknown__'))  # Fallback to string ID
                    
                    try:
                        import yaml
                        with open(os.path.join(self.__class__.__file__, 'task.py'), 'r') as f:
                            data = yaml.safe_load(f) or {}
                        
                        if isinstance(data, dict
import sys
from typing import List, Optional, Dict, Any, Tuple
import os
from datetime import timedelta, datetime, timezone
from enum import Enum

class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations."""
    
    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        self.pending_operations: Dict[str, List[Task]] = {}  # Dictionary mapping command names -> list of Task objects

    @classmethod
    def load_from_json(cls, filename: str) -> 'AlchemyManager':
        """Load manager state from a JSON file."""
        filepath = os.path.join(os.getcwd(), filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"JSON file '{filepath}' not found")
        
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                return cls._json_serializable(data)
        except Exception:
            # Fallback to default instance creation or simulation if json loading fails
            cls._default_instance()

    def _load_json_serializable(self) -> dict:
        """Convert JSON string data structure into a native Python dictionary for this class."""
        return {k: self._json_to_dict(v) for k, v in yaml.load_all(json_path=self.__class__.__file__, loader=lambda d: os.environ.get('PYYAML', 'pyyaml'))}

    def _default_instance(self):
        """Fallback instance creation when loading fails or environment is missing config."""
        return self._instance
        
    @classmethod
    def _json_to_dict(cls, value) -> Any:
        if isinstance(value, dict):
            return {k: cls._json_to_dict(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [cls._json_to_dict(item) for item in value]
        else:
            # Handle nested structures that might not be dicts/lists (e.g., custom objects or other types)
            if hasattr(cls.__class__, '__dict__'):
                result = cls.__dict__.get(value, None)
                return result
            elif isinstance(value, str):
                try:
                    return json.loads(value)
                except Exception as e:
                    # Fallback to string representation for unsupported types (e.g., custom objects
