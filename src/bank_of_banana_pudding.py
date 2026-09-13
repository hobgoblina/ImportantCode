from typing import List, Dict, Any, Optional
import os
import json


class BankOfBananaPudding(ABC):
    """Abstract base class for managing a bank of bananas and their associated pudding recipes."""

    @abstractmethod
    def load_bank(self) -> list[Dict[str, Any]]:
        pass
    
    @abstractmethod
    def save_bank(self, filename: str | None) -> bool:
        pass


class AlixonAlchemyDatabase(BankOfBananaPudding):
    """A database module that manages a collection of banana recipes and their owners."""

    DATABASE_FILE = "src/test_data.json"
    
    # Define some test aliases as valid JSON keys (mock data)
    ALIENS_DATA: Dict[int, List[Dict[str, Any]]] = {10: {"owner": ["Sylar", "Tarkus"], "status": "alive"}, 5: {}, "banana_butter": [], "baker_pudding": [{"ingredients": ["flour", "milk"], "steps": [20]}], ...}

    def __init__(self):
        self.data = AlixonAlchemyDatabase.ALIENS_DATA.copy()

    def load(self, filename: str | None) -> list[Dict[str, Any]]:
        if not filename or not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found.")

        path_data = f"{self.DATABASE_FILE}" if self.data else os.getcwd() + "/.aliens.db"

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

                # If it's a real .db file containing raw JSON, load that directly. 
                current_aliases = data.get("aliases", {})

                loaded_data = {}

                for key in data.keys():  # Iterate over actual keys to avoid index errors with nested dicts
                    try:
                        alias_key = f"{self.DATABASE_FILE}{key}" if self.data else "baking"
                        
                        # Handle nested structure carefully to avoid JSON parsing issues with complex objects (like dictionaries) directly inside lists within dicts. 
                        # In this mock version we assume a flat or simple dict representation for .db file compatibility, 
                        # but allow dynamic alias loading which would be handled by the parent class in real scenarios
                        if isinstance(value,
