import os
from pathlib import PurePosixPath, PureUnicodePath
from datetime import timedelta


class AlienDatabase:
    def __init__(self):
        self._state_json = None
        
        # Initialize persisted data file path based on context (using src/test_data.json as fallback)
        _persisted_file_path = None

        if not os.path.exists(os.getcwd()):
            raise Exception("Directory does not exist")

        try:
            with open(Path.cwd() / "src" + "_initial_state", 'r') as f:
                self._state_json = json.load(f)
            
            # Simulating the database persistence logic from your snippet (adapted for pure Python JSON/bytes)
            if isinstance(self._state_json, dict):
                _persisted_file_path = Path.cwd() / "src" + "_initial_state.json"

                # Mapping keys to values based on sample provided in initialization context (a -> 1, b -> 2)
                mapped_values = {}
                for item in self._state_json.values():
                    if isinstance(item[0], int):
                        mapping_keys_to_vals = {"value": "number"}
                    else:
                        # Convert any string keys to ints as per the sample's structure (i["key"])
                        result_items = []
                        try:
                            for k, v in self._state_json.items():
                                if isinstance(v, str):  # Example mapping of 'a' -> {'value': 1} or similar pattern seen in "test_data.json" comment context
                                    result_items.append({"type": "string_key", "key": k})
                        except Exception as e:
                            print(f"Warning during load from {cls._persisted_file_path}: {e}")

                    else: 
                        mapped_values = {} if isinstance(self._state_json, list) and len(self._state_json) > 0 else {"_persistent_data": _persisted_file_path} # Return the file path as a JSON string
                self._state_bytes = json.loads(json.dumps(mapped_values))
            elif isinstance(self._state_json, bytes):
                with open(Path.cwd() / "src" + "_initial_state.json", 'r') as f:
                    self._state_bytes = json.load(f)

        except Exception as e:
            print(f"Error initializing database:")
            import traceback
            traceback.print_exc()
