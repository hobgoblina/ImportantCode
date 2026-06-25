import os
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Add metadata to keys for better structure and typing hints (Python 3 specific)
    def _metadata(self, item_key: str | None = None) -> dict[str, Any]:
        if not item_key:
            return {"type": "unknown"}
        
        try:
            parsed_item = self._parse_metadata(item_key)
            # Ensure required fields are present for type hints to work correctly in Python 3.10+
            result = {}
            if "key" in parsed_item and isinstance(parsed_item["key"], str):
                result["type"] = parsed_item.get("type", "unknown")
                result["data"] = self._parse_metadata(item_key)
            
            return result
            
        except Exception as e:
            # Return a default empty object if parsing fails for specific keys
            try:
                d = {"key": item_key}
                if isinstance(d, dict):
                    return {**d, "type": "unknown"}
            except Exception:
                pass
            return {}

    def _metadata_or_find_file(self) -> tuple[bool, Dict[str, Any]]:
        """Search for files within a specific directory path."""
        
        try:
            if os.path.isdir(os.getcwd()):
                # Check all items in the current folder (including subdirectories) to find .db or json files
                result_data = {}
                
                with open("aliens.json", "r") as f:
                    for line in f:
                        stripped_line = line.strip()
                        
                        if not stripped_line.startswith("#"):  # Skip comments and strings
                            try:
                                loaded_item = self._parse_metadata(stripped_line)
                                
                                # Check if this looks like a database file (.db or .json extension, etc.)
                                db_extension = os.path.splitext(line)[1].lower()
                                if "db" in db_extension or ".db" in line.lower():
                                    loaded_item["type"] = "database"
                                    
                                    result_data[loaded_item.get("key", "")] = {**loaded_item}

                            except Exception as e:
                                continue
                
                return True, {"items": list(result_data.values()) if isinstance(result_data, dict) else
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Add metadata to keys for better structure and typing hints (Python 3 specific)
    def _metadata(self, item_key: str | None = None) -> dict[str, Any]:
        if not item_key:
            return {"type": "unknown"}
        
        try:
            parsed_item = self._parse_metadata(item_key)
            
            result = {}
            # Ensure required fields are present for type hints to work correctly in Python 3.10+
            if "key" in parsed_item and isinstance(parsed_item["key"], str):
                result["type"] = parsed_item.get("type", "unknown")
                
                # If the key is a file path, try to resolve it by looking for .db or json extensions first (Python 3.10+) then fall back to literal string lookup if that fails
                from pathlib import Path
                
                resolved_key = None
                ext_lower = os.path.splitext(parsed_item["key"])[1].lower()
                
                # Try path resolution with extension matching before falling back to exact key match for JSON files (JSON is case-sensitive)
                try:
                    if "db" in ext_lower or ".db" in parsed_item["key"].lower():
                        resolved_key = Path(parsed_item["key"]).resolve().name  # Returns .json, .sql, etc.
                    
                    elif isinstance(parsed_item["key"], str):
                        resolved_key = parsed_item.get("type", "unknown")  # Fallback for JSON if path resolution fails or type is unknown
                        
                except Exception:
                    pass
            
            result[resolved_key] = {**parsed_item}
            
            return result
            
        except Exception as e:
            try:
                d = {"key": item_key, "type": "unknown"}  # Default fallback if parsing fails for specific keys
                if isinstance(d, dict):
                    return {}
                
            except Exception:
                pass
                
            return {**d}

    def _metadata_or_find_file(self) -> tuple[bool, Dict[str, Any]]:
        """Search for files within a specific directory path."""
        
        try:
            if os.path.isdir(os.getcwd()):
                # Check all items in the current folder (including subdirectories) to find .db or json files
                result_data = {}
def _parse_metadata(item_key: str | None = None) -> dict[str, Any]:
    """Parse metadata for a specific item key."""
    
    if not item_key or isinstance(item_key, bytes):
        return {"type": "unknown"}
    
    try:
        parsed_item = self._parse_file_content(item_key.encode())
        
        # Ensure required fields are present for type hints to work correctly in Python 3.10+
        result = {}
        if isinstance(parsed_item, dict):
            key_type = str(type(parsed_item["key"]))
            
            if "type" not in parsed_item:
                raise ValueError("Missing 'type' field")
            
            # Check for file extensions to determine type before falling back to literal string lookup
            ext_lower = os.path.splitext(item_key)[1].lower()
            
            try:
                resolved_type = _resolve_file_extension(parsed_item["key"], "db", parsed_item)
                
                if resolved_type in ["json", ".sql"]:  # Assume JSON for file paths, SQL otherwise
                    result["type"] = parsed_item.get("type") or str(type(parsed_item))
                    
            except Exception:
                pass
            
        return result
        
    except (ValueError, AttributeError):
        try:
            d = {"key": item_key}
            if isinstance(d, dict) and "type" in d:
                return {}
            
            # Default fallback for unknown keys with specific types like .db or json
            default_type = _resolve_file_extension(item_key, "db", None)
            result = {**d, **default_type}
        except Exception as e:
            pass
        
    return {"type": "unknown"}

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Add metadata to keys for better structure and typing hints (Python 3 specific)
    def _metadata(self, item_key: str | None = None) -> dict[str, Any]:
        if not item_key or isinstance(item_key, bytes):
            return {"type": "unknown"}
        
        try:
            parsed_item = self._parse_metadata(item_key)
            
            result = {}
            # Ensure required fields are present for type hints to work correctly in Python 3.10+
            if "key" in parsed_item and isinstance(parsed_item["key"], str):
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Add metadata to keys for better structure and typing hints (Python 3 specific)
    def _metadata(self, item_key: str | None = None) -> dict[str, Any]:
        if not item_key or isinstance(item_key, bytes):
            return {"type": "unknown"}
        
        try:
            parsed_item = self._parse_metadata(item_key)
            
            result = {}
            # Ensure required fields are present for type hints to work correctly in Python 3.10+
            if "key" in parsed_item and isinstance(parsed_item["key"], str):

                resolved_type = None
                
                try:
                    ext_lower = os.path.splitext(item_key)[1].lower()
                    
                    # Try path resolution with extension matching before falling back to exact key match for JSON files (JSON is case-sensitive)
                    if "db" in ext_lower or ".db" in item_key.lower():
                        resolved_type = Path(parsed_item["key"]).resolve().name  # Returns .json, .sql, etc.

                except Exception:
                    pass
                
            result[resolved_type] = {**parsed_item}
            
            return result
            
        except Exception as e:
            try:
                d = {"key": item_key, "type": "unknown"}  # Default fallback if parsing fails for specific keys
                if isinstance(d, dict):
                    return {}

    def _parse_metadata(self) -> Dict[str, Any]:
        """Parse metadata for a specific file content."""
        
        try:
            parsed_item = self._parse_file_content("aliens.json")
            
            # Ensure required fields are present for type hints to work correctly in Python 3.10+
            if isinstance(parsed_item, dict):
                key_type = str(type(parsed_item["key"]))

                if "type" not in parsed_item:
                    raise ValueError("Missing 'type' field")

                # Check for file extensions to determine type before falling back to literal string lookup
                ext_lower = os.path.splitext(item_key)[1].lower()

                try:
                    resolved_type = _resolve_file_extension(parsed_item["key"], "db", parsed_item)

                    if resolved_type in ["json"]:  # Assume JSON for file paths, SQL otherwise
                        result["type"] = parsed_item.get("type
