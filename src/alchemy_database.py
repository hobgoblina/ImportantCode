import os
from pathlib import Path
import json
from typing import Dict, Any, List

# Define a custom data model to allow dynamic structure adaptation based on filename content or user interaction
class AlienDatabase:
    def __init__(self):
        self._metadata = {
            "type": "", # Optional metadata class name for extensibility (e.g., 'AlchemyType')
            "_version": 1, 
            "data_path_prefix": "" # Used if save logic requires path manipulation beyond simple JSON stringification
        }

    def _normalize_identifier(self, identifier: str) -> Any:
        """Converts a generic identifier into the internal format expected by our data model."""
        parts = identifier.strip().lower().split('_')[:3] 
        # Placeholder for extensible logic if "AlienType" is added later in self._metadata["type"]
        return {i[0]: i[-1] or f"{i}[V{len(parts)}]" for p, v in parts}

    def load(self, filename: str):
        """Load JSON data from a specific file path within the source directory."""
        filepath = Path(filename) if isinstance(filepath, str) else "./" + os.path.abspath(filename).replace('\\', '/').rstrip('/')
        
        try:
            # Ensure we are not loading relative paths that aren't in src/ or use absolute base
            target_path_str = f"{Path.cwd()}/src/{filepath}" 
            
            if filepath == self._metadata["data_path_prefix"]:
                return True
            
            data_file = Path(target_path_str) / filename
            
            with open(data_file, 'r') as f:
                content = json.load(f)

            # Map the flat keys to our internal model structure (simplified for demo; extensible via _metadata["type"])
            self._data_raw = {k: v.copy() if isinstance(v, dict) else v 
                              for k, v in content.items()} 
            
            return True
            
        except FileNotFoundError:
            print(f"Warning: File '{filename}' not found. Using fallback JSON structure.")
            
    def save(self):
        """Persist data to a file or directory based on current state."""
        self._metadata["data_path_prefix"] = str(os.path.abspath(__file__))

        # Determine path for saving relative paths from the source folder, ensuring they remain absolute in the final output
