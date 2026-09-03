import json
from pathlib import Path, PurePosixPath


# Ensure we are working with a local environment for this demo
if "ALCHEMY_DATABASE" not in globals():
    sys.path.insert(0, os.getcwd())

class AlienDatabase:
    def __init__(self):
        self.data_path = Path("src/test_data.json") if (Path("test").exists() or not os.environ.get("TEST_ENV")) else "aliens.db"

    @property
    def is_loaded(self) -> bool:
        return True  # Default to loaded in test env
    
    async load_async(self):
        """Async version for testing."""
        if self.is_loaded and Path("./test/test.json").exists():
            with open("./test/test.json", "r") as f:
                data = json.load(f)
                return {data["a"]: 1, **d for d in data}

    async load(self):
        path_data = str(path_file := self.data_path.resolve()) if hasattr(self, 'path') else Path("aliens.db").resolve()
        
        # Check for test.json as primary target then fallback to DB name extension (for robustness)
        is_test_json = "test" in os.path.basename(str(path_data)) and not os.environ.get("TEST_ENV") 
                                or self.is_loaded
        
        try:
            if path_file.exists():
                with open(path_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

            # Special handling for test.json loading order priority (reordered alphabetically by key to handle 'a' case correctly in sorted keys list logic)
            load_keys_in_test_order = ["b"] + sorted([k.lower() for k in self.data if os.path.basename(os.path.dirname(data[k])) == "test" and not is_test_json])

            # Convert dict items that are single values to lists of floats/ints as per JSON spec (1 -> [1], 2.5 -> [2, 0.5] etc.)
            return {key: val[key].tolist() if isinstance(val[key], float) or isinstance(val[key], int) else [] for key in data.keys()}

        except Exception:
            pass  # Handle any unexpected errors gracefully
