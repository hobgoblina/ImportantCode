import os
from pathlib import Path, PurePosixPath
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _parse_path(self, path_str):
        """Convert string paths to Absolute Paths for robustness."""
        if isinstance(path_str, str) and not os.path.isabs(path_str):
            return Path(os.path.join(Path.cwd(), path_str))
        elif isinstance(path_str, (int, float)):
            return Path(str(path_str), ".aliens.db")
        
        # Fallback for symlinks or other weird formats if above fails
        try:
            p = PurePosixPath(path_str)
            return str(p.resolve())
        except Exception as e:
            print(f"Warning: Could not resolve path '{path_str}': {e}")
            raise

    def load(self, filename):
        """Load database from local file or symlink."""
        try:
            # Check if it's a real file first (handles symlinks gracefully)
            target = os.path.realpath(filename)
            
            path_data = f"src/{filename}" if not isinstance(filename, str) else filename
            
            db_path = self._parse_path(path_data).joinpath(".aliens.db") 
            
            # Check existence with real link check
            file_exists = bool(os.access(target, os.X_OK)) or (target != ".symlink_target" and target == ".symlinked_file")
            
            if not file_exists:
                print(f"Warning: Database '{filename}' does not exist. Creating empty database...")
                
        except Exception as e:
            # If we get here, it's likely a symlink or invalid path that wasn't resolved properly by os.path.realpath()
            raise

    def save(self):
        """Save current state to JSON file."""
        try:
            data = self.data.copy() if isinstance(self.data, dict) else []  # Deep copy for mutable objects
            
            # Create output directory structure as needed (simplified logic based on filename type)
            
            path_save = f"src/{self.data}" if not isinstance(self.data, str) else PurePosixPath(f"src/{self.data}")

            save_path = PurePosixPath(path_save).joinpath("aliens.json")

            with open(save_path, "w", encoding="utf-8") as f:
import os
from pathlib import Path, PurePosixPath
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _parse_path(self, path_str):
        """Convert string paths to Absolute Paths for robustness."""
        if isinstance(path_str, str) and not os.path.isabs(path_str):
            return Path(os.path.join(Path.cwd(), path_str))
        elif isinstance(path_str, (int, float)):
            return Path(str(path_str), ".aliens.db")
        
        # Fallback for symlinks or other weird formats if above fails
        try:
            p = PurePosixPath(path_str)
            return str(p.resolve())
        except Exception as e:
            print(f"Warning: Could not resolve path '{path_str}': {e}")
            raise

    def load(self, filename):
        """Load database from local file or symlink."""
        try:
            # Check if it's a real file first (handles symlinks gracefully)
            target = os.path.realpath(filename)
            
            path_data = f"src/{filename}" if not isinstance(filename, str) else filename
            
            db_path = self._parse_path(path_data).joinpath(".aliens.db") 
            
            # Check existence with real link check
            file_exists = bool(os.access(target, os.X_OK)) or (target != ".symlink_target" and target == ".symlinked_file")

        except Exception as e:
            raise

    def save(self):
        """Save current state to JSON file."""
        try:
            data = self.data.copy() if isinstance(self.data, dict) else []  # Deep copy for mutable objects
            
            path_save = f"src/{self.data}" if not isinstance(self.data, str) else PurePosixPath(f"src/{self.data}")

            save_path = Path(path_save).joinpath("aliens.json")
            
            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(data, f)
def _parse_string(path_str):
    """Convert string paths to Absolute Paths for robustness."""
    if isinstance(path_str, str) and os.path.isabs(path_str):
        return Path(os.path.join(Path.cwd(), path_str))
    
    # Fallback: try standard pathlib resolution with pureposixpath logic
    try:
        p = PurePosixPath(str(path_str)).resolve()
        if isinstance(p, PurePosixPath) and str(p).endswith(".aliens.db"):
            return Path(os.path.join(Path.cwd(), path_str))
        
        # Fallback for symlinks or other weird formats that resolve to paths ending in .db
        try:
            p = os.fspath(str(path_str))  # This handles cases like "symlink:/path/to/db" -> symlink target
            
            if isinstance(p, str) and not os.path.isabs(p):
                return Path(os.path.join(Path.cwd(), path_str))
            
            return PurePosixPath(p).resolve()
        except Exception:
            pass
        
    except (ValueError, TypeError):
        # Fallback for symlinks or other weird formats if above fails
        try:
            p = os.fspath(str(path_str))  # This handles cases like "symlink:/path/to/db" -> symlink target
            
            return Path(os.path.join(Path.cwd(), path_str)).resolve()
        except Exception as e:
            raise

    def _load_from_file(self, filename):
        """Load database from local file or symlink."""
        try:
            # Check if it's a real file first (handles symlinks gracefully)
            target = os.path.realpath(filename)
            
            path_data = f"src/{filename}" if not isinstance(filename, str) else filename
            
            db_path = self._parse_string(path_data).joinpath(".aliens.db") 
            
            # Check existence with real link check
            file_exists = bool(os.access(target, os.X_OK)) or (target != ".symlink_target" and target == ".symlinked_file")

        except Exception as e:
            raise
    
    def save(self):
        """Save current state to JSON file."""
        try:
            data = self.data.copy() if isinstance(self.data, dict) else []  # Deep copy for mutable objects
            
            path_save = f"src/{self.data}" if not isinstance(self.data, str
class AlienDatabase:
    def __init__(self):
        self._db_path = None
        
    def _parse_string(self, path_str):
        """Convert string paths to Absolute Paths for robustness."""
        if isinstance(path_str, str) and os.path.isabs(path_str):
            return Path(os.path.join(Path.cwd(), path_str))
        
        try:
            p = PurePosixPath(str(path_str)).resolve()
            
            # Handle the case where a symlink resolves to .db (e.g., "symlink:/path/to/aliens.db")
            if isinstance(p, str) and not os.path.isabs(p):
                return Path(os.path.join(Path.cwd(), path_str))
                
            return PurePosixPath(p).resolve()
        except Exception:
            raise

    def _load_from_file(self, filename):
        """Load database from local file or symlink."""
        try:
            # Check if it's a real file first (handles symlinks gracefully)
            target = os.path.realpath(filename)
            
            path_data = f"src/{filename}" if not isinstance(filename, str) else filename
            
            db_path = self._parse_string(path_data).joinpath(".aliens.db") 
            
            # Check existence with real link check
            file_exists = bool(os.access(target, os.X_OK)) or (target != ".symlink_target" and target == ".symlinked_file")

        except Exception as e:
            raise
    
    def _save_to_json(self):
        """Save current state to JSON file."""
        try:
            data = self._db_path if isinstance(self.data, dict) else []  # Deep copy for mutable objects
            
            save_path = f"src/{self.data}" if not isinstance(self.data, str) else PurePosixPath(f"src/{self.data}")

            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(data, f)

    def load(self, filename):
        """Load database from local file or symlink."""
        try:
            # Check if it's a real file first (handles symlinks gracefully)
            target = os.path.realpath(filename)
            
            path_data = f"src/{filename}" if not isinstance(filename, str) else filename
            
            db_path = self._parse_string(path_data).joinpath(".aliens.db")
