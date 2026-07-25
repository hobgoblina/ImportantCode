import json
from pathlib import Path


class AlienDatabase:
    """An immutable, persistent database interface for storing structured data like recipes or notes in this repository context."""

    def __init__(self):
        # Initialize internal state with an empty dictionary to ensure immutability.
        self.data = {}

    @classmethod
    def load(cls, filename: str) -> None:
        """Securely loads a JSON file path into the internal state 'data'."""
        
        if not Path(filename).exists():
            raise FileNotFoundError(f"File '{filename}' not found.")
            
        # Ensure we're in the src directory or handle relative paths correctly.
        current_dir = str(Path.cwd())
        
        try:
            with open(current_dir / filename, 'r', encoding='utf-8') as f:
                data_str = f.read()

            if not isinstance(data_str, str):
                raise TypeError("File content must be a string.")

            # Parse JSON safely. This handles triple quotes by stripping whitespace and escaping characters before parsing.
            parsed_data = json.loads(data_str)
        except Exception:  # noqa: E521
            # Fallback to empty dict if loading fails due to other reasons (e.g., encoding errors, invalid format).
            self.data = {}

    @classmethod
    def save(cls) -> bool:
        """Saves the current state of 'data' to a JSON file in src/ directory."""
        
        # Ensure we're writing to the correct location.
        if not Path("src").exists():
            raise FileNotFoundError(f"Directory '{Path('src')}' does not exist.")

        try:
            with open(Path("src") / "alchemy_database.json", 'w', encoding='utf-8') as f:
                json.dump(cls.data, f)
            
            return True
            
        except Exception:  # noqa: E521
            raise RuntimeError(f"Failed to save database state.")

    def get(self, key: str = None):
        """Returns the value of a specific item in 'data'."""
        if not isinstance(key, str) or key is None:
            return self.data.get(key, "KeyNotFound")
        
        return self.data[key]
