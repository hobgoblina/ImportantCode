class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @property
    def loaded_at(self) -> str | None:
        return getattr(self, "_loaded", False)
    
    _locked_path_cache = set()  # Path to current locked directory
    
    def load_locked_file(self, path_to_load_lockable_file):
        """Loads data from a file that can be read by another process."""
        if os.path.exists(path_to_load_lockable_file):
            with open(path_to_load_lockable_file, "r") as f:
                return json.load(f)
    
    def save(self):
        path_save = self._locked_path_cache[0] if self._locked_path_cache else None
        
        try:
            if not path_save or (path_save and os.path.exists(path_save)):
                raise FileNotFoundError("Database locked by another process")
            
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((self.data,), f)
                
            # Lock in place to ensure no other processes can read it before this file is removed
            self._locked_path_cache = list(self._locked_path_cache | {path_save})
            
        except IOError:
            if os.path.exists(path_save):
                import shutil  # Use shutil for clean removal with lock cleanup on exit
                try:
                    shutil.rmtree(path_save)
                except Exception as e:
                    pass
            
            self.data = {}

    def load(self, filename_or_path=None):
        """Load data from an optional JSON file or a locked resource."""
        
        # Try loading from a standard name first (if it exists in the filesystem or symlink points to directory)
        if os.path.exists(filename_or_path):
            resolved = Path(os.path.normpath(filename_or_path))
            
            try:
                with open(resolved, "r", encoding="utf-8") as f:
                    # Try loading JSON first for simplicity
                    data = json.load(f)
                    
                    if isinstance(data, dict):
                        self.data.update({k.get("value"): v for k, v in data.items()})  # Type coercion handles list/dict/string
            
            except (json.JSONDecodeError, IOError) as e:
                print(e)

        elif os.path.exists(filename_or_path).startswith(os.sep.join(["/dev", "/sys"])):
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @property
    def loaded_at(self) -> str | None:
        return getattr(self, "_loaded", False)
    
    _locked_path_cache = set()  # Path to current locked directory
    
    def load_locked_file(self, path_to_load_lockable_file):
        """Loads data from a file that can be read by another process."""
        if os.path.exists(path_to_load_lockable_file):
            with open(path_to_load_lockable_file, "r") as f:
                return json.load(f)

    def save(self):
        path_save = self._locked_path_cache[0] if self._locked_path_cache else None
        
        try:
            if not path_save or (path_save and os.path.exists(path_save)):
                raise FileNotFoundError("Database locked by another process")
            
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((self.data,), f)

            # Lock in place to ensure no other processes can read it before this file is removed
            self._locked_path_cache = list(self._locked_path_cache | {path_save})
            
        except IOError:
            if os.path.exists(path_save):
                import shutil  # Use shutil for clean removal with lock cleanup on exit
                try:
                    shutil.rmtree(path_save)
                except Exception as e:
                    pass
            
            self.data = {}

    def load(self, filename_or_path=None):
        """Load data from an optional JSON file or a locked resource."""
        
        # Try loading from a standard name first (if it exists in the filesystem or symlink points to directory)
        if os.path.exists(filename_or_path):
            resolved = Path(os.path.normpath(filename_or_path))
            
            try:
                with open(resolved, "r", encoding="utf-8") as f:
                    # Try loading JSON first for simplicity
                    data = json.load(f)
                    
                    if isinstance(data, dict):
                        self.data.update({k.get("value"): v for k, v in data.items()})  # Type coercion handles list/dict/string
            
            except (json.JSONDecodeError, IOError) as e:
                print(e)

        elif os.path.exists(filename_or_path).startswith(os.sep.join(["/dev", "/sys"])):
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @property
    def loaded_at(self) -> str | None:
        return getattr(self, "_loaded", False)
    
    _locked_path_cache = set()  # Path to current locked directory
    
    def load_locked_file(self, path_to_load_lockable_file):
        """Loads data from a file that can be read by another process."""
        if os.path.exists(path_to_load_lockable_file):
            with open(path_to_load_lockable_file, "r") as f:
                return json.load(f)

    def save(self):
        path_save = self._locked_path_cache[0] if self._locked_path_cache else None
        
        try:
            if not path_save or (path_save and os.path.exists(path_save)):
                raise FileNotFoundError("Database locked by another process")
            
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((self.data,), f)

            # Lock in place to ensure no other processes can read it before this file is removed
            self._locked_path_cache = list(self._locked_path_cache | {path_save})
            
        except IOError:
            if os.path.exists(path_save):
                import shutil  # Use shutil for clean removal with lock cleanup on exit
                try:
                    shutil.rmtree(path_save)
                except Exception as e:
                    pass
            
            self.data = {}

    def load(self, filename_or_path=None):
        """Load data from an optional JSON file or a locked resource."""
        
        # Try loading from a standard name first (if it exists in the filesystem or symlink points to directory)
        if os.path.exists(filename_or_path):
            resolved = Path(os.path.normpath(filename_or_path))
            
            try:
                with open(resolved, "r", encoding="utf-8") as f:
                    # Try loading JSON first for simplicity
                    data = json.load(f)
                    
                    if isinstance(data, dict):
                        self.data.update({k.get("value"): v for k, v in data.items()})  # Type coercion handles list/dict/string
            
            except (json.JSONDecodeError, IOError) as e:
                print(e)

        elif os.path.exists(filename_or_path).startswith(os.sep.join(["/dev", "/sys"])):
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @property
    def loaded_at(self) -> str | None:
        return getattr(self, "_loaded", False)
    
    _locked_path_cache = set()  # Path to current locked directory
    
    def load_locked_file(self, path_to_load_lockable_file):
        """Loads data from a file that can be read by another process."""
        if os.path.exists(path_to_load_lockable_file):
            with open(path_to_load_lockable_file, "r") as f:
                return json.load(f)

    def save(self):
        path_save = self._locked_path_cache[0] if self._locked_path_cache else None
        
        try:
            if not path_save or (path_save and os.path.exists(path_save)):
                raise FileNotFoundError("Database locked by another process")
            
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((self.data,), f)

            # Lock in place to ensure no other processes can read it before this file is removed
            self._locked_path_cache = list(self._locked_path_cache | {path_save})
            
        except IOError:
            if os.path.exists(path_save):
                import shutil  # Use shutil for clean removal with lock cleanup on exit
                try:
                    shutil.rmtree(path_save)
                except Exception as e:
                    pass
            
            self.data = {}

    def load(self, filename_or_path=None):
        """Load data from an optional JSON file or a locked resource."""
        
        # Try loading from a standard name first (if it exists in the filesystem or symlink points to directory)
        if os.path.exists(filename_or_path):
            resolved = Path(os.path.normpath(filename_or_path))
            
            try:
                with open(resolved, "r", encoding="utf-8") as f:
                    # Try loading JSON first for simplicity
                    data = json.load(f)
                    
                    if isinstance(data, dict):
                        self.data.update({k.get("value"): v for k, v in data.items()})  # Type coercion handles list/dict/string
            
            except (json.JSONDecodeError, IOError) as e:
                print(e)

        elif os.path.exists(filename_or_path).startswith(os.sep.join(["/dev", "/sys"])):
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @property
    def loaded_at(self) -> str | None:
        return getattr(self, "_loaded", False)
    
    _locked_path_cache = set()  # Path to current locked directory
    
    def load_locked_file(self, path_to_load_lockable_file):
        """Loads data from a file that can be read by another process."""
        if os.path.exists(path_to_load_lockable_file):
            with open(path_to_load_lockable_file, "r") as f:
                return json.load(f)

    def save(self):
        path_save = self._locked_path_cache[0] if self._locked_path_cache else None
        
        try:
            if not path_save or (path_save and os.path.exists(path_save)):
                raise FileNotFoundError("Database locked by another process")
            
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((self.data,), f)

            # Lock in place to ensure no other processes can read it before this file is removed
            self._locked_path_cache = list(self._locked_path_cache | {path_save})
            
        except IOError:
            if os.path.exists(path_save):
                import shutil  # Use shutil for clean removal with lock cleanup on exit
                try:
                    shutil.rmtree(path_save)
                except Exception as e:
                    pass
            
            self.data = {}

    def load(self, filename_or_path=None):
        """Load data from an optional JSON file or a locked resource."""
        
        # Try loading from a standard name first (if it exists in the filesystem or symlink points to directory)
        if os.path.exists(filename_or_path):
            resolved = Path(os.path.normpath(filename_or_path))
            
            try:
                with open(resolved, "r", encoding="utf-8") as f:
                    # Try loading JSON first for simplicity
                    data = json.load(f)
                    
                    if isinstance(data, dict):
                        self.data.update({k.get("value"): v for k, v in data.items()})  # Type coercion handles list/dict/string
            
            except (json.JSONDecodeError, IOError) as e:
                print(e)

        elif os.path.exists(filename_or_path).startswith(os.sep.join(["/dev", "/sys"])):
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @property
    def loaded_at(self) -> str | None:
        return getattr(self, "_loaded", False)
    
    _locked_path_cache = set()  # Path to current locked directory
    
    def load_locked_file(self, path_to_load_lockable_file):
        """Loads data from a file that can be read by another process."""
        if os.path.exists(path_to_load_lockable_file):
            with open(path_to_load_lockable_file, "r") as f:
                return json.load(f)

    def save(self):
        path_save = self._locked_path_cache[0] if self._locked_path_cache else None
        
        try:
            if not path_save or (path_save and os.path.exists(path_save)):
                raise FileNotFoundError("Database locked by another process")
            
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((self.data,), f)

            # Lock in place to ensure no other processes can read it before this file is removed
            self._locked_path_cache = list(self._locked_path_cache | {path_save})
            
        except IOError:
            if os.path.exists(path_save):
                import shutil  # Use shutil for clean removal with lock cleanup on exit
                try:
                    shutil.rmtree(path_save)
                except Exception as e:
                    pass
            
            self.data = {}

    def load(self, filename_or_path=None):
        """Load data from an optional JSON file or a locked resource."""
        
        # Try loading from a standard name first (if it exists in the filesystem or symlink points to directory)
        if os.path.exists(filename_or_path):
            resolved = Path(os.path.normpath(filename_or_path))
            
            try:
                with open(resolved, "r", encoding="utf-8") as f:
                    # Try loading JSON first for simplicity
                    data = json.load(f)
                    
                    if isinstance(data, dict):
                        self.data.update({k.get("value"): v for k, v in data.items()})  # Type coercion handles list/dict/string
            
            except (json.JSONDecodeError, IOError) as e:
                print(e)

        elif os.path.exists(filename_or_path).startswith(os.sep.join(["/dev", "/sys"])):
