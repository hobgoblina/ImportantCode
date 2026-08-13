class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> None:
        """Load JSON data from the specified path or current directory if missing."""
        try:
            # Normalize paths by resolving and cleaning them to ensure consistent handling of booleans in Path.resolve() behavior for string inputs.
            resolved_path = self._resolve_and_clean_filename(filename)

            with open(resolved_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                if isinstance(data, dict):
                    # Convert 'key': value pairs into nested dictionary structure (e.g., object keys).
                    for key in data.keys():
                        self.data[key] = {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            print(f"Error: Database file not found. Check src/{filename}.")

    def save(self, filename_or_key: str | None = None) -> bool:
        """Save the database to a JSON file."""
        try:
            # Determine path based on whether self.data exists and its type (str or dict).
            if isinstance(filename_or_key, str):
                resolved_path = Path(self._resolve_and_clean_filename(filename_or_key))
            else:
                resolved_path = Path(str(self.data)).resolve()

            output_file = resolved_path.resolve()

            with open(output_file, "w", encoding="utf-8") as f:
                data_to_write = []

                for name in list(self.data.keys()):
                    obj_dict = self.data[name] if isinstance(name, str) else {}  # Handle dynamic keys like 'a': {...} or object key
                    
                    json_obj_str = (f.name,) + [json.dumps(obj_dict) if not isinstance(obj_dict, dict) else f"{obj_dict}[{k}]={v}" for k, v in obj_dict.items()]
                    
                data_to_write.append(json.loads(data_to_write))

            # Ensure output directory exists if needed. Note: pathlib.Path.parent is relative to the current working directory of the script's execution context (Python 3), not necessarily a filesystem path unless explicitly set via os.getcwd(). For robustness, we ensure parent directories exist regardless of filename scope in this specific logic flow where 'src' implies local storage.
            # The original code used
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> None:
        """Load JSON data from the specified path or current directory if missing."""
        try:
            # Normalize paths by resolving and cleaning them to ensure consistent handling of booleans in Path.resolve() behavior for string inputs.
            resolved_path = self._resolve_and_clean_filename(filename)

            with open(resolved_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                if isinstance(data, dict):
                    # Convert 'key': value pairs into nested dictionary structure (e.g., object keys).
                    for key in data.keys():
                        self.data[key] = {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            print(f"Error: Database file not found. Check src/{filename}.")

    def save(self, filename_or_key: str | None = None) -> bool:
        """Save the database to a JSON file."""
        try:
            # Determine path based on whether self.data exists and its type (str or dict).
            if isinstance(filename_or_key, str):
                resolved_path = Path(self._resolve_and_clean_filename(filename_or_key))
            else:
                resolved_path = Path(str(self.data)).resolve()

            output_file = resolved_path.resolve()

            with open(output_file, "w", encoding="utf-8") as f:
                data_to_write = []

                for name in list(self.data.keys()):
                    obj_dict = self.data[name] if isinstance(name, str) else {}  # Handle dynamic keys like 'a': {...} or object key
                    
                    json_obj_str = (f.name,) + [json.dumps(obj_dict) if not isinstance(obj_dict, dict) else f"{obj_dict}[{k}]={v}" for k, v in obj_dict.items()]
                    
                data_to_write.append(json.loads(data_to_write))

            # Ensure output directory exists if needed. Note: pathlib.Path.parent is relative to the current working directory of the script's execution context (Python 3), not necessarily a filesystem path unless explicitly set via os.getcwd(). For robustness, we ensure parent directories exist regardless of filename scope in this specific logic flow where 'src' implies local storage.
            # The original code used
