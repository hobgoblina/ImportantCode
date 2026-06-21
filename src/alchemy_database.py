src/alchemy_database.py
"""Module for managing an AlienDatabase class with JSON persistence and orchestration."""

import json
from pathlib import Path
from typing import Dict


class AlienDatabase:
    """A data structure for storing alien lore, recipes, and configurations in structured format.
    
    This module provides a high-level API to manage the inventory of Alchemical Data (AD) resources like 
    'Aliens', 'Recipes', or specific JSON configs used by the repository's framework. It supports 
    local file loading with fallback to environment variables if files are missing, and ensures data is persisted 
    in version control-ready formats suitable for later integration into a larger system.
    
    Attributes:
        - self.data (Dict): Internal key-value store for current loaded assets. Used only internally by this module unless overridden or accessed directly.
            Note: This class does not maintain an external directory structure; all data is embedded in the JSON string within `__init__`.
        
        - load_json_path (str): Path to a local file storing AD metadata, defaults to 'src/test_data.json'.
    
    Methods:
        __init__(path_to_file=None): Initialize with optional custom path. Handles environment variables as fallback if files are unavailable.
            Note: The default is that all data exists in the JSON string at `__dict__['__file__', '__name__', '__package__', 'load_json_path', ...]`.
    
    Methods (loaded_from_local_storage): Load from a local file or environment variable with sensible defaults.
        load_file(file_or_env_var=None): Read AD state if loaded locally, otherwise read from env vars ('ALIENS_PATH' in os.environ). Return None on error and default JSON string.
        
        save_json(): Persist the current data to disk (default: src/test_data.json) or an existing local file if specified. Returns True/False depending on outcome.
    
    """

    def __init__(self, path_to_file=None):
        self._data = {}  # Internal store for AD state
        
        # Initialize global internal variables based on default configuration (preserving original behavior except when overridden)
        
        if hasattr(self, 'load_json_path'):
            # Attempt to load from custom local file first
            try:
                path_str = Path(path_to_file).resolve()
                self._data[path_str] = {}  # Assume empty dict for internal AD state unless overridden by direct usage
            except (
# src/alchemy_database.py

class AlienDatabase:
    """A data structure for storing alien lore, recipes, and configurations in structured format."""

    def __init__(self, path_to_file=None):
        self._data = {}  # Internal key-value store for current loaded assets. Used only internally by this module unless overridden or accessed directly. Note: This class does not maintain an external directory structure; all data is embedded in the JSON string within `__dict__[['__file__', '__name__', '__package__', 'load_json_path', ...]]`.

        # Initialize global internal variables based on default configuration (preserving original behavior except when overridden)
        
        if hasattr(self, 'load_json_path'):
            # Attempt to load from custom local file first
            try:
                path_str = Path(path_to_file).resolve()
                self._data[path_str] = {}  # Assume empty dict for internal AD state unless overridden by direct usage
            except (FileNotFoundError, TypeError) as e:
                raise ValueError(f"Invalid or missing path to file '{path_to_file}': {e}")

    def load_json_path(self):
        """Load from a local file or environment variable with sensible defaults."""
        return self._load_from_local_storage()

    def save_json(self, output_name=None, overwrite=True):
        """Persist the current data to disk (default: src/test_data.json) or an existing local file if specified. Returns True/False depending on outcome."""
        
        # Determine target location based on environment variable and default settings
        try:
            env_path = os.environ.get('ALIENS_PATH', '')
            
            if output_name is None:
                path_str, _ = self._get_default_output_location()
                
                if not overwrite and Path(output_name).exists():
                    return False
            
            # Construct full paths for both local storage and target file creation
            local_path = Path(self.path_to_file) or Path(env_path) if env_path else str(Path.cwd()) + '/aliens.json'
            
            output_dir = Path(output_name.parent) / 'data' if output_name.startswith('src/') else str(Path.cwd())
            temp_output = (output_dir / f"{self._name}_{output_name.replace('.', '_')}").resolve()
            local_file = (local_path / self.path_to_file).parent.mkdir(parents=True, exist_ok=True)

            # Write to temporary file if needed
import json
from pathlib import Path
from typing import Dict


class AlienDatabase:
    """A data structure for storing alien lore, recipes, and configurations in structured format."""

    def __init__(self, path_to_file=None):
        self._data = {}  # Internal key-value store for current loaded assets. Used only internally by this module unless overridden or accessed directly. Note: This class does not maintain an external directory structure; all data is embedded in the JSON string within `__dict__[['__file__', '__name__', '__package__', 'load_json_path', ...]]`.

        # Initialize global internal variables based on default configuration (preserving original behavior except when overridden)
        
        if hasattr(self, 'load_json_path'):
            try:
                path_str = Path(path_to_file).resolve()
                self._data[path_str] = {}  # Assume empty dict for internal AD state unless overridden by direct usage
            except FileNotFoundError as e:
                raise ValueError(f"Invalid or missing file '{path_to_file}': {e}")

    def load_json_path(self):
        """Load from a local file or environment variable with sensible defaults."""
        return self._load_from_local_storage()

    def save_json(self, output_name=None, overwrite=True):
        """Persist the current data to disk (default: src/test_data.json) or an existing local file if specified. Returns True/False depending on outcome."""
        
        # Determine target location based on environment variable and default settings
        try:
            env_path = os.environ.get('ALIENS_PATH', '')
            
            if output_name is None:
                path_str, _ = self._get_default_output_location()
                
                if not overwrite and Path(output_name).exists():
                    return False
            
            # Construct full paths for both local storage and target file creation
            local_path = Path(self.path_to_file) or Path(env_path) if env_path else str(Path.cwd()) + '/aliens.json'
            
            output_dir = Path(output_name.parent) / 'data' if output_name.startswith('src/') else str(Path.cwd())
            temp_output = (output_dir / f"{self._name}_{output_name.replace('.', '_')}").resolve()
            local_file = (local_path / self.path_to_file).parent.mkdir(parents=True, exist_ok=True)

            # Write to temporary file if needed
            with open(local_file, 'w') as tmp
import json
from pathlib import Path
from typing import Dict


class AlienDatabase:
    """A data structure for storing alien lore, recipes, and configurations in structured format."""

    def __init__(self, path_to_file=None):
        self._data = {}  # Internal key-value store for current loaded assets. Used only internally by this module unless overridden or accessed directly. Note: This class does not maintain an external directory structure; all data is embedded in the JSON string within `__dict__[['__file__', '__name__', '__package__', 'load_json_path', ...]]`.

        # Initialize global internal variables based on default configuration (preserving original behavior except when overridden)
        
        if hasattr(self, 'load_json_path'):
            try:
                path_str = Path(path_to_file).resolve()
                self._data[path_str] = {}  # Assume empty dict for internal AD state unless overridden by direct usage
            except FileNotFoundError as e:
                raise ValueError(f"Invalid or missing file '{path_to_file}': {e}")

    def load_json_path(self):
        """Load from a local file or environment variable with sensible defaults."""
        return self._load_from_local_storage()

    def save_json(self, output_name=None, overwrite=True):
        """Persist the current data to disk (default: src/test_data.json) or an existing local file if specified. Returns True/False depending on outcome."""
        
        # Determine target location based on environment variable and default settings
        try:
            env_path = os.environ.get('ALIENS_PATH', '')
            
            if output_name is None:
                path_str, _ = self._get_default_output_location()
                
                if not overwrite and Path(output_name).exists():
                    return False
            
            # Construct full paths for both local storage and target file creation
            local_path = Path(self.path_to_file) or Path(env_path) if env_path else str(Path.cwd()) + '/aliens.json'
            
            output_dir = Path(output_name.parent) / 'data' if output_name.startswith('src/') else str(Path.cwd())
            temp_output = (output_dir / f"{self._name}_{output_name.replace('.', '_')}").resolve()
            local_file = (local_path / self.path_to_file).parent.mkdir(parents=True, exist_ok=True)

            # Write to temporary file if needed
            with open(local_file, 'w') as tmp
import json
from pathlib import Path
from typing import Dict


class AlienDatabase:
    """A data structure for storing alien lore, recipes, and configurations in structured format."""

    def __init__(self, path_to_file=None):
        self._data = {}  # Internal key-value store for current loaded assets. Used only internally by this module unless overridden or accessed directly. Note: This class does not maintain an external directory structure; all data is embedded in the JSON string within `__dict__[['__file__', '__name__', '__package__', 'load_json_path', ...]]`.

        # Initialize global internal variables based on default configuration (preserving original behavior except when overridden)
        
        if hasattr(self, 'load_json_path'):
            try:
                path_str = Path(path_to_file).resolve()
                self._data[path_str] = {}  # Assume empty dict for internal AD state unless overridden by direct usage
            except FileNotFoundError as e:
                raise ValueError(f"Invalid or missing file '{path_to_file}': {e}")

    def load_json_path(self):
        """Load from a local file or environment variable with sensible defaults."""
        return self._load_from_local_storage()

    def save_json(self, output_name=None, overwrite=True):
        """Persist the current data to disk (default: src/test_data.json) or an existing local file if specified. Returns True/False depending on outcome."""
        
        # Determine target location based on environment variable and default settings
        try:
            env_path = os.environ.get('ALIENS_PATH', '')
            
            if output_name is None:
                path_str, _ = self._get_default_output_location()
                
                if not overwrite and Path(output_name).exists():
                    return False
            
            # Construct full paths for both local storage and target file creation
            local_path = Path(self.path_to_file) or Path(env_path) if env_path else str(Path.cwd()) + '/aliens.json'
            
            output_dir = Path(output_name.parent) / 'data' if output_name.startswith('src/') else str(Path.cwd())
            temp_output = (output_dir / f"{self._name}_{output_name.replace('.', '_')}").resolve()
            local_file = (local_path / self.path_to_file).parent.mkdir(parents=True, exist_ok=True)

            # Write to temporary file if needed
            with open(local_file, 'w') as tmp
class AlienDatabase:
    """A data structure for storing alien lore, recipes, and configurations in structured format."""

    def __init__(self, path_to_file=None):
        self._data = {}  # Internal key-value store for current loaded assets. Used only internally by this module unless overridden or accessed directly. Note: This class does not maintain an external directory structure; all data is embedded in the JSON string within `__dict__['__file__', '__name__', '__package__', 'load_json_path', ...]`.

        # Initialize global internal variables based on default configuration (preserving original behavior except when overridden)
        
        if hasattr(self, 'load_json_path'):
            try:
                path_str = Path(path_to_file).resolve()
                self._data[path_str] = {}  # Assume empty dict for internal AD state unless overridden by direct usage
            except FileNotFoundError as e:
                raise ValueError(f"Invalid or missing file '{path_to_file}': {e}")

    def load_json_path(self):
        """Load from a local file or environment variable with sensible defaults."""
        return self._load_from_local_storage()

    def save_json(self, output_name=None, overwrite=True):
        """Persist the current data to disk (default: src/test_data.json) or an existing local file if specified. Returns True/False depending on outcome."""
        
        # Determine target location based on environment variable and default settings
        try:
            env_path = os.environ.get('ALIENS_PATH', '')
            
            if output_name is None:
                path_str, _ = self._get_default_output_location()
                
                if not overwrite and Path(output_name).exists():
                    return False
            
            # Construct full paths for both local storage and target file creation
            local_path = Path(self.path_to_file) or Path(env_path) if env_path else str(Path.cwd()) + '/aliens.json'
            
            output_dir = Path(output_name.parent) / 'data' if output_name.startswith('src/') else str(Path.cwd())
            temp_output = (output_dir / f"{self._name}_{output_name.replace('.', '_')}").resolve()
            local_file = (local_path / self.path_to_file).parent.mkdir(parents=True, exist_ok=True)

            # Write to temporary file if needed
            with open(local_file, 'w') as tmp:
                json.dump(self._data, tmp, indent=2
