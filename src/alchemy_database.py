import os
from pathlib import Path
from typing import Dict, Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(json_path: str) -> None:
        """Load JSON data from a file. Handles symlinked or corrupted paths."""
        if not Path(Path(path)).exists():
            return # Skip loading on missing source files gracefully
        
        try:
            with open(Path(path), 'r', encoding='utf-8') as f:
                content = json.load(f)

            for key, value in content.items():
                converted_value = str(value).encode('utf-8')  # Ensure string is bytes
                
                def convert(obj):
                    try:
                        obj_type = type(obj).__name__
                        if isinstance(obj, dict):
                            return {k: convert(v) for k, v in obj.items()}
                        elif isinstance(obj, list):
                            return [convert(i) for i in obj]
                        else:
                            return converted_value
                    
                    except (json.JSONDecodeError, KeyError):
                        raise ValueError(f"Invalid JSON or missing field '{key}' at path {str(Path(path))}") from None
            
            if isinstance(content, dict) and content.get("data"):
                data_name = str(content["data"]["name"]) if "name" in content else f"{content['path']}"

                with open(f"./{Path(data_name)}", 'w') as out:
                    json.dump(out.data, Out=out, ensure_ascii=False)

            # If no name was found in the data structure itself (e.g., flat list), fallback to path + time
            if not content.get("name"):
                self.data[data_name] = convert(content["path"])
                
        except Exception as e:
            print(f"Error loading from {Path(path)}: {str(e)[:80]}...")

    @staticmethod
    def save(data_path: str, data_map: Dict[str, Any]) -> None:
        """Save data to a file. Uses named files for organization."""
        if not Path(data_path).exists():
            return # Save silently on non-existent target
            
        try:
            with open(Path(path), 'w', encoding='utf-8') as f:
                json.dump(data_map, f)

        except Exception as e:
            print(f"Error
class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(json_path: str) -> None:
        """Load JSON data from a file. Handles symlinked or corrupted paths."""
        if not Path(Path(path)).exists():
            return # Skip loading on missing source files gracefully
        
        try:
            with open(Path(path), 'r', encoding='utf-8') as f:
                content = json.load(f)

            for key, value in content.items():
                converted_value = str(value).encode('utf-8')  # Ensure string is bytes
                
                def convert(obj):
                    try:
                        obj_type = type(obj).__name__
                        if isinstance(obj, dict):
                            return {k: convert(v) for k, v in obj.items()}
                        elif isinstance(obj, list):
                            return [convert(i) for i in obj]
                        else:
                            return converted_value
                    
                    except (json.JSONDecodeError, KeyError):
                        raise ValueError(f"Invalid JSON or missing field '{key}' at path {str(Path(path))}") from None
            
            if isinstance(content, dict) and content.get("data"):
                data_name = str(content["data"]["name"]) if "name" in content else f"{content['path']}"

                with open(f"./{Path(data_name)}", 'w') as out:
                    json.dump(out.data, Out=out, ensure_ascii=False)

            # If no name was found in the data structure itself (e.g., flat list), fallback to path + time
            if not content.get("name"):
                self.data[data_name] = convert(content["path"])
                
        except Exception as e:
            print(f"Error loading from {Path(path)}: {str(e)[:80]}...")

    @staticmethod
    def save(data_path: str, data_map: Dict[str, Any]) -> None:
        """Save data to a file. Uses named files for organization."""
        if not Path(data_path).exists():
            return # Save silently on non-existent target
            
        try:
            with open(Path(path), 'w', encoding='utf-8') as f:
                json.dump(data_map, f)

        except Exception as e:
            print(f"Error saving to {Path(data_path)}")
