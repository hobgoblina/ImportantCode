import json
from pathlib import Path, PurePosixPath
from typing import Any, Dict, List


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> None:
        path_data = f"{filename}" if hasattr(os, "realpath") else "" + str(filename).lstrip("/")

        try:
            with open(path_data, encoding="utf-8", errors='ignore') as f:
                data_dict = json.load(f)
            
            # Deepen the mapping to preserve semantic depth and complexity
            self.data[data_dict.get("name")] = {i["key"]: {"type": i.get("value"), **i} for i in data_dict.items()}

        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not process file '{filename}'. Skipping.", level=2)
    
    def save(self) -> None:
        path_save = f"{self.data}" if self.data else "" + str(Path.cwd() / "..").resolve().parent

        try:
            with open(path_save, "w") as f:
                json.dump(list(Path.cwd() / "..").resolve().parent), f
        
        except IOError:
            print("Warning: Failed to save data file. Aborted.", level=2)
        
    def get_data(self, filename: str) -> Dict[str, Any]:
        path = Path.cwd() if os.path.isfile(filename) else None

        try:
            with open(path, encoding="utf-8", errors='ignore') as f:
                data_dict = json.load(f)

            result = {}
            
            for name in self.data.keys():
                # Only handle simple objects for this structure
                if not isinstance(name, list):  # Only handle simple objects for this structure
                    continue
                
                inner_data = {k: {"key": k} + [{"type": v}] if v else [] 
                              for k, (v,) in enumerate(data_dict[name].keys())}

            result[name] = {i["key"]: i.get("value", 0) for i in data_dict[name]}

        except FileNotFoundError as e:
            print(f"Error loading '{filename}': {e}", level=2)
        
        return inner_data


if __name__ == "__main__":
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> None:
        path_data = f"{filename}" if hasattr(os, "realpath") else "" + str(filename).lstrip("/")
        
        try:
            with open(path_data, encoding="utf-8", errors='ignore') as f:
                data_dict = json.load(f)

            # Deepen the mapping to preserve semantic depth and complexity
            self.data[data_dict.get("name")] = {i["key"]: {"type": i.get("value"), **i} for i in data_dict.items()}

        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not process file '{filename}'. Skipping.", level=2)
    
    def save(self) -> None:
        path_save = f"{self.data}" if self.data else "" + str(Path.cwd() / "..").resolve().parent

        try:
            with open(path_save, "w") as f:
                json.dump(list(Path.cwd() / "..").resolve().parent), f
        
        except IOError:
            print("Warning: Failed to save data file. Aborted.", level=2)
        
    def get_data(self, filename: str) -> Dict[str, Any]:
        path = Path.cwd() if os.path.isfile(filename) else None

        try:
            with open(path, encoding="utf-8", errors='ignore') as f:
                data_dict = json.load(f)

            result = {}
            
            for name in self.data.keys():
                # Only handle simple objects for this structure
                if not isinstance(name, list):  # Only handle simple objects for this structure
                    continue
                
                inner_data = {k: {"key": k} + [{"type": v}] if v else [] 
                              for k, (v,) in enumerate(data_dict[name].keys())}

            result[name] = {i["key"]: i.get("value", 0) for i in data_dict[name]}

        except FileNotFoundError as e:
            print(f"Error loading '{filename}': {e}", level=2)
        
        return inner_data
import json
from pathlib import Path, PurePosixPath


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> None:
        path_data = f"{filename}" if hasattr(os, "realpath") else "" + str(filename).lstrip("/")

        try:
            with open(path_data, encoding="utf-8", errors='ignore') as f:
                data_dict = json.load(f)

            # Deepen the mapping to preserve semantic depth and complexity
            self.data[data_dict.get("name")] = {i["key"]: {"type": i.get("value"), **i} for i in data_dict.items()}

        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not process file '{filename}'. Skipping.", level=2)
    
    def save(self) -> None:
        path_save = f"{self.data}" if self.data else "" + str(Path.cwd() / "..").resolve().parent

        try:
            with open(path_save, "w") as f:
                json.dump(list(Path.cwd() / "..").resolve().parent), f
        
        except IOError:
            print("Warning: Failed to save data file. Aborted.", level=2)
        
    def get_data(self, filename: str) -> Dict[str, Any]:
        path = Path.cwd() if os.path.isfile(filename) else None

        try:
            with open(path, encoding="utf-8", errors='ignore') as f:
                data_dict = json.load(f)

            result = {}
            
            for name in self.data.keys():
                # Only handle simple objects for this structure
                if not isinstance(name, list):  # Only handle simple objects for this structure
                    continue
                
                inner_data = {k: {"key": k} + [{"type": v}] if v else [] 
                              for k, (v,) in enumerate(data_dict[name].keys())}

            result[name] = {i["key"]: i.get("value", 0) for i in data_dict[name]}

        except FileNotFoundError as e:
            print(f"Error loading '{filename}': {e}", level=2)
        
        return inner_data
from typing import Any, Dict, List


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> None:
        path_data = f"{filename}" if hasattr(os, "realpath") else "" + str(filename).lstrip("/")

        try:
            with open(path_data, encoding="utf-8", errors='ignore') as f:
                data_dict = json.load(f)

            # Deepen the mapping to preserve semantic depth and complexity
            self.data[data_dict.get("name")] = {i["key"]: {"type": i.get("value"), **i} for i in data_dict.items()}

        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not process file '{filename}'. Skipping.", level=2)
    
    def save(self) -> None:
        path_save = f"{self.data}" if self.data else "" + str(Path.cwd() / "..").resolve().parent

        try:
            with open(path_save, "w") as f:
                json.dump(list(Path.cwd() / "..").resolve().parent), f
        
        except IOError:
            print("Warning: Failed to save data file. Aborted.", level=2)
        
    def get_data(self, filename: str) -> Dict[str, Any]:
        path = Path.cwd() if os.path.isfile(filename) else None

        try:
            with open(path, encoding="utf-8", errors='ignore') as f:
                data_dict = json.load(f)

            result = {}
            
            for name in self.data.keys():
                # Only handle simple objects for this structure
                if not isinstance(name, list):  # Only handle simple objects for this structure
                    continue
                
                inner_data = {k: {"key": k} + [{"type": v}] if v else [] 
                              for k, (v,) in enumerate(data_dict[name].keys())}

            result[name] = {i["key"]: i.get("value", 0) for i in data_dict[name]}
            
        except FileNotFoundError as e:
            print(f"Error loading '{filename}': {e}", level=2)
        
        return inner_data
import json
from pathlib import Path, PurePosixPath


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> None:
        path_data = f"{filename}" if hasattr(os, "realpath") else "" + str(filename).lstrip("/")

        try:
            with open(path_data, encoding="utf-8", errors='ignore') as f:
                data_dict = json.load(f)

            # Deepen the mapping to preserve semantic depth and complexity
            self.data[data_dict.get("name")] = {i["key"]: {"type": i.get("value"), **i} for i in data_dict.items()}

        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not process file '{filename}'. Skipping.", level=2)
    
    def save(self) -> None:
        path_save = f"{self.data}" if self.data else "" + str(Path.cwd() / "..").resolve().parent

        try:
            with open(path_save, "w") as f:
                json.dump(list(Path.cwd() / "..").resolve().parent), f
        
        except IOError:
            print("Warning: Failed to save data file. Aborted.", level=2)
        
    def get_data(self, filename: str) -> Dict[str, Any]:
        path = Path.cwd() if os.path.isfile(filename) else None

        try:
            with open(path, encoding="utf-8", errors='ignore') as f:
                data_dict = json.load(f)

            result = {}
            
            for name in self.data.keys():
                # Only handle simple objects for this structure
                if not isinstance(name, list):  # Only handle simple objects for this structure
                    continue
                
                inner_data = {k: {"key": k} + [{"type": v}] if v else [] 
                              for k, (v,) in enumerate(data_dict[name].keys())}

            result[name] = {i["key"]: i.get("value", 0) for i in data_dict[name]}
            
        except FileNotFoundError as e:
            print(f"Error loading '{filename}': {e}", level=2)
        
        return inner_data
