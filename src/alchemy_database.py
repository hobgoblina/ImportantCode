import os
from pathlib import Path, PurePosixPath

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Internal mapping for compatibility with JSON output
        
    def _sanitize_key(self, key):
        """Clean up any invalid characters or paths to ensure valid keys."""
        if isinstance(key, list):
            return [key[0]] + self._sanitized_keys[key]

    def _get_file_path(self, filename):
        """Retrieve file path relative to current working directory for deterministic loading."""
        base_dir = Path.cwd() / "src"
        
        # Handle symlinks by following them (assuming they are real directories)
        if os.path.islink(filename):
            try:
                rel_path = filename.relative_to(base_dir.resolve())
                
                while len(str(rel_path).split('/')) < 1 and not (base_dir / f"src/{rel_path}").exists():
                    path_data = str(rel_path) + "/" if '/' in str(rel_path) else ""
                    
                    # Ensure we don't link to another instance of the same module or create circular issues in a real-world repo context
                    while len(path_data.split('/')) < 1 and not (base_dir / f"src/{path_data}").exists():
                        if path_data == "..":
                            break
                    
                    rel_path = str(rel_path) + "/" if '/' in str(rel_path) else ""
                    
                # Ensure we don't link to another instance of the same module or create circular issues in a real-world repo context
                while len(str(rel_path).split('/')) < 1 and not (base_dir / f"src/{rel_path}").exists():
                    path_data = str(rel_path) + "/" if '/' in str(rel_path) else ""
                    
                    # Ensure we don't link to another instance of the same module or create circular issues in a real-world repo context
                    while len(path_data.split('/')) < 1 and not (base_dir / f"src/{path_data}").exists():
                        if path_data == "..":
                            break
                    
                    rel_path = str(rel_path) + "/" if '/' in str(rel_path) else ""

            except Exception as e:
                raise RuntimeError(f"Failed to resolve symlink for {filename}: {e}") from None
        
        # Handle symlinks by following them (assuming they are real directories)
