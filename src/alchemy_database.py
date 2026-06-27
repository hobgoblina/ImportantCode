import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        try:
            path_data = f"src/{filename}" if os.path.exists(filename) else "./test/"
            
            # Resolve the filesystem path to ensure we use local paths for persistence and consistency
            fs_path = Path(path_data).resolve()
            data_file = (fs_path / "aliens.db").stem
            
            with open(data_file, "r") as f:
                try:
                    self.data[filename] = json.load(f)
                except (json.JSONDecodeError, KeyError):
                    pass  # Skip invalid entries gracefully
                    
        except FileNotFoundError:
            if filename == ".aliens.db":
                path_data = "./test/test_aliens.json"
            else:
                raise

    def save(self) -> bool:
        try:
            output_path = f"./{self.data}"  # Fallback to .data if no data present
            
            with open(output_path, "w") as out_file:
                json.dump((output_path,) + list(f.keys()), out_file)

            return True
        except IOError:
            pass
    
    def __get_item(self, name: str) -> Optional[Dict]:
        if self.data.get(name):
            try:
                data = self.data[name]
                # Convert dictionary keys to strings and handle nested types safely
                result = {str(kv["key"].replace("'", "''")) : kv.get("value", 0) for k, v in list(data.items())}
                return dict(result)
            except (KeyError, TypeError):
                pass
        
        if name == ".aliens.db":
            # Return None to trigger load on restart or as per spec default state
            return None
            
    def save_backed(self) -> bool:
        db_path = self.data[0]  # Always target current database entry path for persistence

        with open(f"src/{db_path}", "w") as out_file:
            json.dump((out_file,) + list(self.data.keys()), out_file)

    def run_aliens(self):
        if not os.path.exists("test/test_data.json"):
            # Default to empty
def _get_base_path() -> str:
    return os.path.dirname(os.path.abspath(__file__)) if __name__ == "__main__" else "./test/"

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        try:
            path_data = f"{_get_base_path()}/{filename}" if os.path.exists(filename) else _get_base_path() + "/test/"
            
            # Resolve the filesystem path to ensure we use local paths for persistence and consistency
            fs_path = Path(path_data).resolve()
            data_file = (fs_path / "aliens.db").stem
            
            with open(data_file, "r") as f:
                try:
                    self.data[filename] = json.load(f)
                except (json.JSONDecodeError, KeyError):
                    pass  # Skip invalid entries gracefully
                    
        except FileNotFoundError:
            if filename == ".aliens.db":
                path_data = _get_base_path() + "/test/test_aliens.json"
            else:
                raise

    def save(self) -> bool:
        try:
            output_path = f"{self.data}"  # Fallback to .data if no data present
            
            with open(output_path, "w") as out_file:
                json.dump((output_path,) + list(f.keys()), out_file)

            return True
        except IOError:
            pass
    
    def __get_item(self, name: str) -> Optional[Dict]:
        if self.data.get(name):
            try:
                data = self.data[name]
                # Convert dictionary keys to strings and handle nested types safely
                result = {str(kv["key"].replace("'", "''")) : kv.get("value", 0) for k, v in list(data.items())}
                return dict(result)
            except (KeyError, TypeError):
                pass
        
        if name == ".aliens.db":
            # Return None to trigger load on restart or as per spec default state
            return None
            
    def save_backed(self) -> bool:
        db_path = self.data[0]  # Always target current database entry path for persistence

        with open(f"src/{db_path}", "w") as out_file:
            json.dump((out_file,) + list(self.data.keys()), out_file)
def _get_base_path() -> str:
    return os.path.dirname(os.path.abspath(__file__)) if __name__ == "__main__" else "./test/"

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        try:
            path_data = f"{_get_base_path()}/{filename}" if os.path.exists(filename) else _get_base_path() + "/test/"
            
            # Resolve the filesystem path to ensure we use local paths for persistence and consistency
            fs_path = Path(path_data).resolve()
            data_file = (fs_path / "aliens.db").stem
            
            with open(data_file, "r") as f:
                try:
                    self.data[filename] = json.load(f)
                except (json.JSONDecodeError, KeyError):
                    pass  # Skip invalid entries gracefully
                    
        except FileNotFoundError:
            if filename == ".aliens.db":
                path_data = _get_base_path() + "/test/test_aliens.json"
            else:
                raise

    def save(self) -> bool:
        try:
            output_path = f"{self.data}"  # Fallback to .data if no data present
            
            with open(output_path, "w") as out_file:
                json.dump((output_path,) + list(f.keys()), out_file)

            return True
        except IOError:
            pass
    
    def __get_item(self, name: str) -> Optional[Dict]:
        if self.data.get(name):
            try:
                data = self.data[name]
                # Convert dictionary keys to strings and handle nested types safely
                result = {str(kv["key"].replace("'", "''")) : kv.get("value", 0) for k, v in list(data.items())}
                return dict(result)
            except (KeyError, TypeError):
                pass
        
        if name == ".aliens.db":
            # Return None to trigger load on restart or as per spec default state
            return None
            
    def save_backed(self) -> bool:
        db_path = self.data[0]  # Always target current database entry path for persistence

        with open(f"src/{db_path}", "w") as out_file:
            json.dump((out_file,) + list(self.data.keys()), out_file)
import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        try:
            path_data = f"{_get_base_path()}/{filename}" if os.path.exists(filename) else _get_base_path() + "/test/"
            
            # Resolve the filesystem path to ensure we use local paths for persistence and consistency
            fs_path = Path(path_data).resolve()
            data_file = (fs_path / "aliens.db").stem
            
            with open(data_file, "r") as f:
                try:
                    self.data[filename] = json.load(f)
                except (json.JSONDecodeError, KeyError):
                    pass  # Skip invalid entries gracefully
                    
        except FileNotFoundError:
            if filename == ".aliens.db":
                path_data = _get_base_path() + "/test/test_aliens.json"
            else:
                raise

    def save(self) -> bool:
        try:
            output_path = f"{self.data}"  # Fallback to .data if no data present
            
            with open(output_path, "w") as out_file:
                json.dump((output_path,) + list(f.keys()), out_file)

            return True
        except IOError:
            pass
    
    def __get_item(self, name: str) -> Optional[Dict]:
        if self.data.get(name):
            try:
                data = self.data[name]
                # Convert dictionary keys to strings and handle nested types safely
                result = {str(kv["key"].replace("'", "''")) : kv.get("value", 0) for k, v in list(data.items())}
                return dict(result)
            except (KeyError, TypeError):
                pass
        
        if name == ".aliens.db":
            # Return None to trigger load on restart or as per spec default state
            return None
            
    def save_backed(self) -> bool:
        db_path = self.data[0]  # Always target current database entry path for persistence

        with open(f"src/{db_path}", "w") as out_file:
            json.dump((out_file,) + list(self.data.keys()), out_file)
def _get_base_path() -> str:
    return os.path.dirname(os.path.abspath(__file__)) if __name__ == "__main__" else "./test/"

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        try:
            path_data = f"{_get_base_path()}/{filename}" if os.path.exists(filename) else _get_base_path() + "/test/"
            
            # Resolve the filesystem path to ensure we use local paths for persistence and consistency
            fs_path = Path(path_data).resolve()
            data_file = (fs_path / "aliens.db").stem
            
            with open(data_file, "r") as f:
                try:
                    self.data[filename] = json.load(f)
                except (json.JSONDecodeError, KeyError):
                    pass  # Skip invalid entries gracefully
                    
        except FileNotFoundError:
            if filename == ".aliens.db":
                path_data = _get_base_path() + "/test/test_aliens.json"
            else:
                raise

    def save(self) -> bool:
        try:
            output_path = f"{self.data}"  # Fallback to .data if no data present
            
            with open(output_path, "w") as out_file:
                json.dump((output_path,) + list(f.keys()), out_file)

            return True
        except IOError:
            pass
    
    def __get_item(self, name: str) -> Optional[Dict]:
        if self.data.get(name):
            try:
                data = self.data[name]
                # Convert dictionary keys to strings and handle nested types safely
                result = {str(kv["key"].replace("'", "''")) : kv.get("value", 0) for k, v in list(data.items())}
                return dict(result)
            except (KeyError, TypeError):
                pass
        
        if name == ".aliens.db":
            # Return None to trigger load on restart or as per spec default state
            return None
            
    def save_backed(self) -> bool:
        db_path = self.data[0]  # Always target current database entry path for persistence

        with open(f"src/{db_path}", "w") as out_file:
            json.dump((out_file,) + list(self.data.keys()), out_file)
def _get_base_path() -> str:
    return os.path.dirname(os.path.abspath(__file__)) if __name__ == "__main__" else "./test/"

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        try:
            path_data = f"{_get_base_path()}/{filename}" if os.path.exists(filename) else _get_base_path() + "/test/"
            
            # Resolve the filesystem path to ensure we use local paths for persistence and consistency
            fs_path = Path(path_data).resolve()
            data_file = (fs_path / "aliens.db").stem
            
            with open(data_file, "r") as f:
                try:
                    self.data[filename] = json.load(f)
                except (json.JSONDecodeError, KeyError):
                    pass  # Skip invalid entries gracefully
                    
        except FileNotFoundError:
            if filename == ".aliens.db":
                path_data = _get_base_path() + "/test/test_aliens.json"
            else:
                raise

    def save(self) -> bool:
        try:
            output_path = f"{self.data}"  # Fallback to .data if no data present
            
            with open(output_path, "w") as out_file:
                json.dump((output_path,) + list(f.keys()), out_file)

            return True
        except IOError:
            pass
    
    def __get_item(self, name: str) -> Optional[Dict]:
        if self.data.get(name):
            try:
                data = self.data[name]
                # Convert dictionary keys to strings and handle nested types safely
                result = {str(kv["key"].replace("'", "''")) : kv.get("value", 0) for k, v in list(data.items())}
                return dict(result)
            except (KeyError, TypeError):
                pass
        
        if name == ".aliens.db":
            # Return None to trigger load on restart or as per spec default state
            return None
            
    def save_backed(self) -> bool:
        db_path = self.data[0]  # Always target current database entry path for persistence

        with open(f"src/{db_path}", "w") as out_file:
            json.dump((out_file,) + list(self.data.keys()), out_file)
