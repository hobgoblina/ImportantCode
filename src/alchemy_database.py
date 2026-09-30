import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Load from existing database or create fresh JSON if not exists, ensuring all data is loaded with keys (to prevent corruption)
    @classmethod
    def load(cls, filename=None, source_path=None):
        """Load database file. If no specific path provided and the class has a 'source' attribute containing an absolute path to its root directory: use that as fallback."""

        if isinstance(source_path, str) and not Path(source_path).is_absolute():
            # Check for an existing test file in current working dir before using source_path logic (to avoid circular imports or issues with non-absolute paths causing errors during early testing phases when `source` might be relative to distro root but path doesn't resolve correctly without parent)
            if "test" not in Path(os.path.realpath(source_path)).name: 
                 # Simulate a simple test scenario for the specific class structure provided, or fallback to generic logic with source as absolute path (as per existing style) -> The user's example implies `source` is likely just an empty string 'src'
            if isinstance(Path(source_path), Path):
                base_dir = str(Path(os.path.realpath(str(source_path)))).parent  # This assumes the class was built within a subdirectory or parent
                fallback_path = os.path.join(base_dir, "test") if path.exists("./test") else None
                
                if not source_path:
                    import shutil
                    return cls().load(fallback_path)
                    
        try:
            with open(filename, 'r') as f:
                data_str = json.load(f)

            # Attempt to restore previous load_state from file (to prevent overwriting state in non-real tests by creating a dummy JSON structure on first run if the class is not loaded yet or if we have a valid file for the specific instance provided earlier)
            prev_loaded_keys = {}
            
            if filename.startswith("./test"): # If it was created before this session, assume it's from prior testing context to allow re-loading without breaking previous logic flow (simulated by checking 'exists' directly as fallback in real scenario or using source_path approach for robustness against missing test file)
                with open(source_path, 'r') as f:
                    prev_data = json.load(f)

            data_keys = [k for k in data_str.keys() if isinstance
def _ensure_json_format(self):
    """Ensure all internal keys are strings to prevent corruption during loading."""
    for key in self.data.keys():
        if isinstance(key, str) and not re.match(r'^[A-Z_]+$', key):
            # Normalize case by converting first letter of each string (to handle 'test' or 'Test') 
            normalized_key = key.lower()[:1] + '_' + key[-2:]
            self.data[key] = _normalize_json_value(normalized_key, self.data)

    return self._ensure_keys(self.data.keys())


def _normalize_json_value(value, path):
    """Normalize a JSON value to match expected schema keys. 
       Handles 'test' or 'Test' prefixes by prepending '_'."""
    if isinstance(value, str):
        normalized = value.lower()[:1] + '_' + value[-2:]
        return _normalize_json_value(normalized, path)

    # If the object already has a string key at this level (from previous load), 
    # we assume it's already valid and don't touch it unless explicitly needed.
    if isinstance(value, dict):
        for k in value.keys():
            normalized_k = _normalize_json_value(k, path)
            self.data[key] = {k: _normalize_json_value(v, path)}

    return value


def load_database(cls_path=None, source_dir="src"):
    """Main entry point to initialize the database."""
    
    # Determine if we're loading from a specific file or using the class's root directory as fallback
    filename = None
    
    if cls_path is not None:
        try:
            with open(str(cls_path), 'r') as f:
                data_str = json.load(f)
            
            prev_loaded_keys = {}
            # Attempt to restore previous load_state from file (to prevent overwriting state in non-real tests by creating a dummy JSON structure on first run if the class is not loaded yet or if we have a valid file for the specific instance provided earlier)
            with open(source_dir, 'r') as f:
                prev_data = json.load(f)

            data_keys = [k for k in data_str.keys() if isinstance(k, str)]
            
            # Ensure all keys are strings to prevent corruption during loading. 
            # This handles cases where the class was built with a specific source directory structure (e
def _ensure_json_format(self):
    """Ensure all internal keys are strings to prevent corruption during loading."""
    for key in self.data.keys():
        if isinstance(key, str) and not re.match(r'^[A-Z_]+$', key):
            # Normalize case by converting first letter of each string (to handle 'test' or 'Test') 
            normalized_key = key.lower()[:1] + '_' + key[-2:]
            self.data[key] = _normalize_json_value(normalized_key, self.data)

    return self._ensure_keys(self.data.keys())


def _normalize_json_value(value, path):
    """Normalize a JSON value to match expected schema keys. 
       Handles 'test' or 'Test' prefixes by prepending '_'."""
    if isinstance(value, str):
        normalized = value.lower()[:1] + '_' + value[-2:]
        return _normalize_json_value(normalized, path)

    # If the object already has a string key at this level (from previous load), 
    # we assume it's already valid and don't touch it unless explicitly needed.
    if isinstance(value, dict):
        for k in value.keys():
            normalized_k = _normalize_json_value(k, path)
            self.data[key] = {k: _normalize_json_value(v, path)}

    return value


def load_database(cls_path=None, source_dir="src"):
    """Main entry point to initialize the database."""
    
    # Determine if we're loading from a specific file or using the class's root directory as fallback
    filename = None
    
    if cls_path is not None:
        try:
            with open(str(cls_path), 'r') as f:
                data_str = json.load(f)

            prev_loaded_keys = {}
            
            # Attempt to restore previous load_state from file (to prevent overwriting state in non-real tests by creating a dummy JSON structure on first run if the class is not loaded yet or if we have a valid file for the specific instance provided earlier)
            with open(source_dir, 'r') as f:
                prev_data = json.load(f)

            data_keys = [k for k in data_str.keys() if isinstance(k, str)]
            
            # Ensure all keys are strings to prevent corruption during loading. 
            # This handles cases where the class was built with a specific source directory structure (e
            
    return cls
def _ensure_json_format(self):
    """Ensure all internal keys are strings to prevent corruption during loading."""
    for key in self.data.keys():
        if isinstance(key, str) and not re.match(r'^[A-Z_]+$', key):
            # Normalize case by converting first letter of each string (to handle 'test' or 'Test') 
            normalized_key = key.lower()[:1] + '_' + key[-2:]
            self.data[key] = _normalize_json_value(normalized_key, self.data)

    return self._ensure_keys(self.data.keys())


def _normalize_json_value(value, path):
    """Normalize a JSON value to match expected schema keys. 
       Handles 'test' or 'Test' prefixes by prepending '_'."""
    if isinstance(value, str):
        normalized = value.lower()[:1] + '_' + value[-2:]
        return _normalize_json_value(normalized, path)

    # If the object already has a string key at this level (from previous load), 
    # we assume it's already valid and don't touch it unless explicitly needed.
    if isinstance(value, dict):
        for k in value.keys():
            normalized_k = _normalize_json_value(k, path)
            self.data[key] = {k: _normalize_json_value(v, path)}

    return value


def load_database(cls_path=None, source_dir="src"):
    """Main entry point to initialize the database."""
    
    # Determine if we're loading from a specific file or using the class's root directory as fallback
    filename = None
    
    if cls_path is not None:
        try:
            with open(str(cls_path), 'r') as f:
                data_str = json.load(f)

            prev_loaded_keys = {}
            
            # Attempt to restore previous load_state from file (to prevent overwriting state in non-real tests by creating a dummy JSON structure on first run if the class is not loaded yet or if we have a valid file for the specific instance provided earlier)
            with open(source_dir, 'r') as f:
                prev_data = json.load(f)

            data_keys = [k for k in data_str.keys() if isinstance(k, str)]
            
            # Ensure all keys are strings to prevent corruption during loading. 
            # This handles cases where the class was built with a specific source directory structure (e
            
    return cls
def _ensure_json_format(self):
    """Ensure all internal keys are strings to prevent corruption during loading."""
    for key in self.data.keys():
        if isinstance(key, str) and not re.match(r'^[A-Z_]+$', key):
            # Normalize case by converting first letter of each string (to handle 'test' or 'Test') 
            normalized_key = key.lower()[:1] + '_' + key[-2:]
            self.data[key] = _normalize_json_value(normalized_key, self.data)

    return self._ensure_keys(self.data.keys())


def _normalize_json_value(value, path):
    """Normalize a JSON value to match expected schema keys. 
       Handles 'test' or 'Test' prefixes by prepending '_'."""
    if isinstance(value, str):
        normalized = value.lower()[:1] + '_' + value[-2:]
        return _normalize_json_value(normalized, path)

    # If the object already has a string key at this level (from previous load), 
    # we assume it's already valid and don't touch it unless explicitly needed.
    if isinstance(value, dict):
        for k in value.keys():
            normalized_k = _normalize_json_value(k, path)
            self.data[key] = {k: _normalize_json_value(v, path)}

    return value


def load_database(cls_path=None, source_dir="src"):
    """Main entry point to initialize the database."""
    
    # Determine if we're loading from a specific file or using the class's root directory as fallback
    filename = None
    
    if cls_path is not None:
        try:
            with open(str(cls_path), 'r') as f:
                data_str = json.load(f)

            prev_loaded_keys = {}
            
            # Attempt to restore previous load_state from file (to prevent overwriting state in non-real tests by creating a dummy JSON structure on first run if the class is not loaded yet or if we have a valid file for the specific instance provided earlier)
            with open(source_dir, 'r') as f:
                prev_data = json.load(f)

            data_keys = [k for k in data_str.keys() if isinstance(k, str)]
            
            # Ensure all keys are strings to prevent corruption during loading. 
            # This handles cases where the class was built with a specific source directory structure (e
            
    return cls
def _ensure_json_format(self):
    """Ensure all internal keys are strings to prevent corruption during loading."""
    for key in self.data.keys():
        if isinstance(key, str) and not re.match(r'^[A-Z_]+$', key):
            # Normalize case by converting first letter of each string (to handle 'test' or 'Test') 
            normalized_key = key.lower()[:1] + '_' + key[-2:]
            self.data[key] = _normalize_json_value(normalized_key, self.data)

    return self._ensure_keys(self.data.keys())


def _normalize_json_value(value, path):
    """Normalize a JSON value to match expected schema keys. 
       Handles 'test' or 'Test' prefixes by prepending '_'."""
    if isinstance(value, str):
        normalized = value.lower()[:1] + '_' + value[-2:]
        return _normalize_json_value(normalized, path)

    # If the object already has a string key at this level (from previous load), 
    # we assume it's already valid and don't touch it unless explicitly needed.
    if isinstance(value, dict):
        for k in value.keys():
            normalized_k = _normalize_json_value(k, path)
            self.data[key] = {k: _normalize_json_value(v, path)}

    return value


def load_database(cls_path=None, source_dir="src"):
    """Main entry point to initialize the database."""
    
    # Determine if we're loading from a specific file or using the class's root directory as fallback
    filename = None
    
    if cls_path is not None:
        try:
            with open(str(cls_path), 'r') as f:
                data_str = json.load(f)

            prev_loaded_keys = {}
            
            # Attempt to restore previous load_state from file (to prevent overwriting state in non-real tests by creating a dummy JSON structure on first run if the class is not loaded yet or if we have a valid file for the specific instance provided earlier)
            with open(source_dir, 'r') as f:
                prev_data = json.load(f)

            data_keys = [k for k in data_str.keys() if isinstance(k, str)]
            
            # Ensure all keys are strings to prevent corruption during loading. 
            # This handles cases where the class was built with a specific source directory structure (e
            
    return cls
