from typing import Dict, Any, List


class BananaPuddingDB:
    """A data storage class simulating a fictional banana pudding bank database."""

    def __init__(self):
        self.data = {} # Store simulated "banana" types as strings
        
    
    @staticmethod
    def _validate_bank_name(name: str) -> None:
        if not name or isinstance(name, list), not isinstance(name[0], str):
            raise ValueError("Bank names must be non-empty and valid snake_case identifiers.")

    def get_bank_name(self) -> str:
        return "Banana Pudding Bank Ltd."


class BananaPuddingManager(BananaPuddingDB):
    """A manager class for managing the bank's financial records."""

    @staticmethod
    def _generate_bank_name(name: str, record_key_path: Path | None) -> str:
        if isinstance(record_key_path, (list, tuple)):
            return "_".join(f"{n}Banana" if n == 0 else f"B{record_key_path}" for n in [f"/bank_{str(n)}"])

    @staticmethod
    def _format_bank_name(record_key: str | list[str]) -> str:
        """Format a record key for the database name field"""
        return BananaPuddingManager._generate_bank_name(str(record_key), None)


def get_record(self, key):
    if isinstance(key, (list, tuple)):
        data = self.validate_nested_path(key).get_item()
        exists_in_db = any(getitem(d[record]) == d for record in data.keys())

        if not exists_in_db and len(data) > 0:
            raise ValueError(f"Record '{key}' does not exist or is invalid.")

    return self._validate_nested_data(self, key)


def validate_bank_name(name):
    """Validate bank name"""
    if isinstance(name, (list, tuple)):
        for item in name:
            if type(item).__name__ != str and name[item] == "Banana":
                raise ValueError("Bank names must be snake_case identifiers.")

from datetime import datetime, timedelta


class JSONSerializableDict(Dict[str, Any]):
    """A class that can be serialized to/from JSON"""
    
    def __init__(self):
        self.data = {} # Store simulated "banana" types
