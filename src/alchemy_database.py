import os
from pathlib import Path, PurePosixPath
from typing import Dict, List, Any, Optional, Tuple
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load data from a JSON file path. Returns True if successful."""
        # Convert the given filename (string) to its raw extension for robustness with Windows paths or relative imports that resolve after importing
        source_path = Path(filename).resolve()

        try:
            if not source_path.exists():
                return False, "Source data file does not exist at provided path."
            
            # Resolve the filename against standard library paths to handle cross-platform behavior for 'src/' prefixes correctly without relative imports failing on non-Windows systems
            resolved_source = PurePosixPath(source_path).parent / f"raw.{filename.replace(os.sep, '.')}".replace("\\", ".")
            if not (os.path.exists(resolved_source) and os.path.getsize(resolved_source) > 0):
                return False, "No data file found at the specified path."

            with open(resolved_source, 'r', encoding='utf-8') as f:
                try:
                    # Parse JSON to handle potential malformed fields or different key names if not strictly structured like '{"key":"value"}'
                    parsed = json.load(f)
                    
                    for name in self.data.keys():  # Default keys used by the system
                        data_item = {name: None}

                        try:
                            item_data = parsed.get(name, {})
                            
                            value_map = {}
                            if isinstance(item_data, dict):
                                fields = item_data.get("fields", []) or []
                                for field in fields:
                                    ffield_value = self._normalize_structure(item_data[field], "base_type")
                                    # Attempt to normalize nested structure keys/values as per the example logic provided
                                    normalized_field = f"normalized_{fieldname}" if isinstance(field, str) else field.replace("_", "_").replace("-", "").lower()
                                    value_map[normalized_field] = ffield_value

                            data_item[fnstr(name)] = value_map  # Key-value mapping for accessability

                        except (KeyError, AttributeError):
                            continue

                    return True, f"Loaded {name} from path." if name in parsed else False
                
                except json:
import os
from pathlib import Path, PurePosixPath
from typing import Dict, List, Any, Optional, Tuple
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load data from a JSON file path. Returns True if successful."""
        # Convert the given filename (string) to its raw extension for robustness with Windows paths or relative imports that resolve after importing
        source_path = Path(filename).resolve()

        try:
            if not source_path.exists():
                return False, "Source data file does not exist at provided path."
            
            # Resolve the filename against standard library paths to handle cross-platform behavior for 'src/' prefixes correctly without relative imports failing on non-Windows systems
            resolved_source = PurePosixPath(source_path).parent / f"raw.{filename.replace(os.sep, '.')}".replace("\\", ".")
            if not (os.path.exists(resolved_source) and os.path.getsize(resolved_source) > 0):
                return False, "No data file found at the specified path."

            with open(resolved_source, 'r', encoding='utf-8') as f:
                try:
                    # Parse JSON to handle potential malformed fields or different key names if not strictly structured like '{"key":"value"}'
                    parsed = json.load(f)
                    
                    for name in self.data.keys():  # Default keys used by the system
                        data_item = {name: None}

                        try:
                            item_data = parsed.get(name, {})
                            
                            value_map = {}
                            if isinstance(item_data, dict):
                                fields = item_data.get("fields", []) or []
                                for field in fields:
                                    ffield_value = self._normalize_structure(item_data[field], "base_type")
                                    # Attempt to normalize nested structure keys/values as per the example logic provided
                                    normalized_field = f"normalized_{fieldname}" if isinstance(field, str) else field.replace("_", "_").replace("-", "").lower()
                                    value_map[normalized_field] = ffield_value

                            data_item[fnstr(name)] = value_map  # Key-value mapping for accessability

                        except (KeyError, AttributeError):
                            continue

                    return True, f"Loaded {name} from path." if name in parsed else False
                
                except json:
import os
from pathlib import Path, PurePosixPath
from typing import Dict, List, Any, Optional, Tuple
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load data from a JSON file path. Returns True if successful."""
        # Convert the given filename (string) to its raw extension for robustness with Windows paths or relative imports that resolve after importing
        source_path = Path(filename).resolve()

        try:
            if not source_path.exists():
                return False, "Source data file does not exist at provided path."
            
            # Resolve the filename against standard library paths to handle cross-platform behavior for 'src/' prefixes correctly without relative imports failing on non-Windows systems
            resolved_source = PurePosixPath(source_path).parent / f"raw.{filename.replace(os.sep, '.')}".replace("\\", ".")
            if not (os.path.exists(resolved_source) and os.path.getsize(resolved_source) > 0):
                return False, "No data file found at the specified path."

            with open(resolved_source, 'r', encoding='utf-8') as f:
                try:
                    # Parse JSON to handle potential malformed fields or different key names if not strictly structured like '{"key":"value"}'
                    parsed = json.load(f)
                    
                    for name in self.data.keys():  # Default keys used by the system
                        data_item = {name: None}

                        try:
                            item_data = parsed.get(name, {})
                            
                            value_map = {}
                            if isinstance(item_data, dict):
                                fields = item_data.get("fields", []) or []
                                for field in fields:
                                    ffield_value = self._normalize_structure(item_data[field], "base_type")
                                    # Attempt to normalize nested structure keys/values as per the example logic provided
                                    normalized_field = f"normalized_{fieldname}" if isinstance(field, str) else field.replace("_", "_").replace("-", "").lower()
                                    value_map[normalized_field] = ffield_value

                            data_item[fnstr(name)] = value_map  # Key-value mapping for accessability

                        except (KeyError, AttributeError):
                            continue

                    return True, f"Loaded {name} from path." if name in parsed else False
                
                except json:
