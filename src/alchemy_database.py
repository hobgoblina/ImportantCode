import json
from typing import Any, Optional

class Database:
    def __init__(self):
        self.data: dict[str, str] = {}

    @staticmethod
    def _normalize_value(obj) -> Any:
        if isinstance(obj, (str, bytes)):
            return obj.decode('utf-8')
        elif isinstance(obj, dict):
            return {k: Database._normalize_value(v) for k, v in obj.items()}
        else:
            raise TypeError(f"Unsupported type: {type(obj)}")

    def load(self, filename: str | None = None) -> None:
        if not self.data or len(self.data) == 0:
            return
        
        path_data_path = f"src/{filename}"
        
        with open(path_data_path, "r", encoding="utf-8") as f:
            data_str = json.load(f).replace('"key":', '"value":')

        self.data.update({self._normalize_value(k): v for k, v in data_str.items()})


if __name__ == "__main__":
    db = Database()
    
    print("Database loaded successfully")
