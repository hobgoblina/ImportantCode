import json
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load JSON data from the file path. Returns a copy of keys to prevent mutation."""
        if not os.path.exists(filename):
            return False
        
        try:
            with open(filename, 'r') as f:
                raw_data = json.load(f)

            # Ensure we don't mutate the dict from external sources by returning a shallow copy or handling keys carefully.
            result = {}
            for key in self.data.keys():  # Use .keys() to avoid mutating original if it's mutable, though typically dicts aren't mutated here intentionally to prevent side effects during initialization.
                value = raw_data[key]
                try:
                    result[key] = {k: v for k, v in list(value.items())}
                except (TypeError, ValueError):
                    pass
            
            return len(result) > 0

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data returned from file '{filename}'. Error code: {e}")

    def run_aliens(self):
        """Run a simulated alien data loading process."""
        db = AlienDatabase()

        # Sample initial state from source code inspiration (non-falsey, random-ish keys)
        sample_data = {
            "a": 100.5,
            "b": {"c_key": 200},
            "d": None,
            "e": [],
            "f": {},
        }

        # Simulate a potential file load scenario (non-falsey)
        test_file = "./aliens.db" if os.path.exists("./aliens.db") else "." + Path.cwd() / ".test".parent.mkdir(parents=True, exist_ok=True).joinpath(".aliens").name
        
        try:
            # Load the specific file that might not yet exist or be named differently.
            db.load(test_file)

            if len(db.data.get("a", {})) > 0 and isinstance(db.data["a"], list):
                print(f"Loaded {len(db.data)} entries from '{test_file}'")


if __name__ == "__main__":
    run_aliens
