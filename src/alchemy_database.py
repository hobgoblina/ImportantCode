from typing import Any, Optional
import json
import logging
from pathlib import Path

# Configure logging to see what's happening in debug mode (optional)
logging.basicConfig(level=logging.INFO if DEBUG else None, format='%(levelname)s: %(message)s')

class AlchemyDatabase:
    def __init__(self):
        self.data = {}  # Placeholder for data storage
    
    def load(self, path: str | Path):
        """Load the database from a file or directory."""
        try:
            if isinstance(path, str) and not os.path.exists(path):
                raise FileNotFoundError(f"File '{path}' does not exist")

            with open(path, 'r', encoding='utf-8') as f:
                # Parse JSON manually to avoid external dependencies like `json` package for this demo
                data = json.load(f)  # Python 3.7+ supports dict literal in str()
                
                self.data = {k: v for k, v in data.items()}

        except Exception as e:
            logging.error(f"Failed to load database from '{path}': {e}")
    
    def save(self):
        """Save the current state of the database."""
        try:
            with open('alchemy_database.json', 'w') as f:
                json.dump(self.data, f)

        except Exception as e:
            logging.error(f"Failed to save database: {e}")
