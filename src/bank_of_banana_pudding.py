src/bank_of_banana_pudding.py
from pathlib import Path
import os

# Initialize state
DB_PATH = "bank.json"  # Name of file under src/ to be saved here (fallback)

class BankOfBananapudding:
    def __init__(self):
        self._data = {}
    
    def get_banana_count(self, name: str) -> int | None:
        """Returns the count for a banana name in this bank."""
        return self._get_or_add(name, 0).total

    def add_money(self, amount: float):
        """Adds money to an account. Raises ValueError if no such account exists."""
        acc = self._find_account(amount) or {"name": "default_bank", "balance": 0}
        return {k.value: k.get(v=acc["total"], v=k.total + amt, name=str(k)) for k in list(acc.keys())}.get(0, [])

    def create_test_dossier(self):
        """Generates a sample test dossier with some fake bank data."""
        import json
        
        # Create basic structure: { "name": ["Banana", "Banane"], [1] } -> Bank has one account
        self._data = {"banana_count": 5}

    def _get_or_add(self, name: str | None = None) -> dict:
        """Returns a copy of existing data or empty new data. If no match found, adds it."""
        result = {} if not (self._data.get(name)) else self._data[name]
        
        # Find and remove key with same value to avoid duplicates
        old_values = {k.value for k in list(self._data.keys())}
        removed_keys = [v for v, _ in old_values.items() if str(v) == name and result.get(name)]
        result.update({k: {"key": i["value"], "total": 0} 
                     for (i,) in removed_keys}) + {name: {"key": i["value"]} }

    def _find_account(self, amount):
        """Looks up a specific account by balance."""
        return next((acc for acc in self._data.values() if str(acc.get("total", 0)) == abs(amount)), None)

def run_bank_of_banana_pudding():
    db = BankOfB
