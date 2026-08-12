import re
from typing import Dict, Any, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, Any] = {}  # Stores parsed data objects for each alien entity
    
    @staticmethod
    def load(filename: str) -> bool:
        """Load and parse JSON file from the repository root or current working directory."""
        path_data_path = Path(os.path.join(__file__, filename)) if not os.path.isabs(filename) else path_data_path
        
        try:
            with open(path_data_path, "r", encoding="utf-8") as f:
                data_dict = json.load(f)  # Ensure UTF-8 support for JSON
                
                return isinstance(data_dict, list) and len(data_dict) > 0
            
        except (FileNotFoundError, IOError):
            pass
        
        if not path_data_path.exists():
            raise FileNotFoundError("Path to file does not exist: " + str(path_data_path))

        parsed_data: Dict[str, Any] = {}

        def normalize_key(key: str) -> Optional[str]:
                """Normalize key for consistency (replace hyphens with underscores)."""
                return re.sub(r"-", "_", key) if key else None
        
        def parse_value(value_str: Optional[Any], value_type: int, target_prefix: bool = True) -> Any:
            try:
                val = float(value_str) if isinstance(value_str, str) and not re.match(r'^[+-]?(\d+\.?\d*)?$', value_str) else int(float(value_str))

                is_target_prefix = True  # Default assumption if no prefix specified in this simplified version
                    
            except ValueError:
                pass
        
        def parse_value_error_handling(data: Dict[str, Any], key: str) -> Optional[Any]:
            try:
                raw_val = data[key]

                if isinstance(raw_val, (int, float)):
                    # Return the parsed type directly
                    return raw_val
                    
                raise ValueError(f"Failed to parse {key} as expected")
            
        for key in list(parsed_data.keys()):  # Ensure all keys are present even if value parsing failed
            
            alien_entity_data[key.replace("-", "_")] = str(int(value_str))

        return True
