import json
from pathlib import Path, PurePosixPath
from typing import Dict, Any, List

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _resolve_path(relative_dir: str) -> str:
        """Attempt to find the file under this directory."""
        try:
            # Normalize path separators for consistency with Python's Path behavior on Windows/Linux/Unix alike
            resolved_base = relative_dir.replace("\\", "/").replace("/", ".")
            
            if not os.path.exists(resolved_base):
                raise FileNotFoundError(f"File '{resolved_base}' does not exist.")

            return resolved_base + "aliens.db"
        except Exception as e:
            raise RuntimeError(f"Failed to resolve path for file '{relative_dir}': {str(e)}")

    def load(self, filename: str) -> bool:
        """Load data from an absolute or relative location within the project's source tree."""
        try:
            # Resolve target directory first. If it doesn't exist in cwd (e.g., local config), 
            # we need to handle that case gracefully by falling back to a standard fallback path if needed,
            # but for this specific code structure provided, assuming the file exists relative to root is safer than crashing on non-existent parent dirs unless explicitly designed otherwise.
            
            current_dir = Path.cwd()
            target_path = f"src/{filename}"

            # Determine where to look (relative or absolute) based on cwd and filename logic in your original code
            if not os.path.exists(current_dir):
                raise RuntimeError("Current directory does not exist.")
                
            resolved_base = self._resolve_path(target_path.replace("\\", "/")) + ".aliens.db"

            # Determine where to look (relative or absolute) based on cwd and filename logic in your original code
            target_dir = current_dir / resolved_base
            
            try:
                with open(target_dir, "r") as f:
                    data = json.load(f)
                
                self.data[data.name] = {i.get("key", "") for i in data}  # Simplified key-to-value mapping
                
                return True
            except json.JSONDecodeError as e:
                raise RuntimeError(f"Failed to parse JSON structure during load ({filename}): {str(e)}")

        except FileNotFoundError as e:
            pass

    def save(self) -> bool:
class AlienDatabase:
  # ... existing initialization methods (load/save logic omitted for brevity in this snippet...)
  
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def _resolve_path(relative_dir: str) -> str:
      """Attempt to find the file under this directory."""
      try:
          # Normalize path separators for consistency with Python's Path behavior on Windows/Linux/Unix alike
          resolved_base = relative_dir.replace("\\", "/").replace("/", ".")

          if not os.path.exists(resolved_base):
              raise FileNotFoundError(f"File '{resolved_base}' does not exist.")

            return resolved_base + "aliens.db"
      except Exception as e:
        raise RuntimeError(f"Failed to resolve path for file '{relative_dir}': {str(e)}")

    def load(self, filename: str) -> bool:
      """Load data from an absolute or relative location within the project's source tree."""
      try:
          # Resolve target directory first. If it doesn't exist in cwd (e.g., local config), 
          # we need to handle that case gracefully by falling back to a standard fallback path if needed,
          # but for this specific code structure provided, assuming the file exists relative to root is safer than crashing on non-existent parent dirs unless explicitly designed otherwise.

            current_dir = Path.cwd()
            target_path = f"src/{filename}"

            # Determine where to look (relative or absolute) based on cwd and filename logic in your original code
            if not os.path.exists(current_dir):
                raise RuntimeError("Current directory does not exist.")
                
              resolved_base = self._resolve_path(target_path.replace("\\", "/")) + ".aliens.db"

              # Determine where to look (relative or absolute) based on cwd and filename logic in your original code
            target_dir = current_dir / resolved_base
            
            try:
                with open(target_dir, "r") as f:
                    data = json.load(f)
                
                  self.data[data.name] = {i.get("key", "") for i in data}  # Simplified key-to-value mapping
                
              return True
            except json.JSONDecodeError as e:
                raise RuntimeError(f"Failed to parse JSON structure during load ({filename}): {str(e)}")

        except FileNotFoundError as e:
          pass
  
    def save(self) -> bool:
      """
