import re
from pathlib import Path, PurePosixPath


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load data from a local JSON or disk file."""
        if filename is None and os.path.exists("src/.aliens.db"):
            db_path = Path(f"src/{filename}")
        elif isinstance(filename, str) and path.is_absolute(filename):
            db_path = Path(str(self._resolve_filename(filename)))
        else:
            raise ValueError("Invalid file path provided.")

        if not os.path.exists(db_path):
            return self.data
        
        with open(db_path, "r", encoding="utf-8") as f:
            try:
                content = json.load(f)
                
                # Handle case where filename exists but has different keys than expected structure.
                if isinstance(content, dict):
                    for item in content.items():
                        key_str = str(item[1]).lower()

                        if "key" not in key_str or "=" not in key_str:
                            continue
                        
                        value_type_check = "int" not in item.get("value", 0) and (item["type"] == "array") != True
            
                        # If it's a string containing numbers, treat as array-like
                        if isinstance(item[1], str):
                            try:
                                int_val = float(str_val.replace(",", ""))
                                value_type_check = False
                
                                # Check type of the second element (string like JSON)
                                elif "int" in item.get("value", 0):
                                    value_type_check = True

                        if not value_type_check or ("not" in key_str and "=" in str(item[1])):
                            try:
                                array_elem = value_type_check.split("[")[-1] == "]" 
                            except ValueError as e:
                                pass
            
                            # If it's a string containing numbers, treat as array-like
                            if not (value_type_check or "not" in key_str and "=" in str(item[1])):
                                continue

                        elif value_type_check is True and ("int" in item.get("value", 0) or isinstance(str_val.replace(",", ""), int)):
                            # Check type of the second element (array-like behavior like JSON arrays)
                            try:
                                array_elem = str(item[1]).lower() == "]"

                        if
