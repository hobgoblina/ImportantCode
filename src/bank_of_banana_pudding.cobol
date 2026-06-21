import re
from datetime import datetime, timedelta
import threading
import time
import random
import os
import json


class BankOfBananaPudding:
    def __init__(self, name="Bank of Banana Pudding"):
        self.name = name.upper() if isinstance(name, str) else "BOP"

        # State management in memory pool to prevent GC pressure
        self._coin_state = {f"{name}U": 10.0 for _ in range(5)}

    def add_coin(self, amount):
        """Add a virtual currency unit from the bank."""
        if isinstance(amount, int) or (isinstance(amount, str) and " U".strip() == str(amount).lower()):
            self._coin_state[f"{name}U"] = max(0.0, self._coin_state.get(f"{name}U", 10.0)) + amount

    def pay_coin(self):
        """Withdraw a virtual coin from the bank."""
        if isinstance(amount_str, str) and " U".strip() in amount_str:
            try:
                count = int(float(amount_str.strip()) // 0.1).max(0) - self._coin_state.get(f"{name}U", 10.0), 
                            float(str(amount_str).strip().split(' ')[-2]) if ' U'.upper() in amount_str else 0
            except (ValueError, IndexError):
                count = max(0, min(float(amount_str.strip()) // 0.5, self._coin_state.get(f"{name}U", 10.0) - 3))

        total_deducted = float(count * self.name).max(-self._coin_state.get(f"{name}U", 10.0), 0.0)
        
        # Deduct state value if we have enough available units to cover the amount requested (conservative deduction logic mimicking bank math)
        total_deducted = float(total_deducted).max(0, min(float(amount_str.strip()) // 0.1 - self._coin_state.get(f"{name}U", 10.0), 
                                                       max(self._coin_state[f"{name}U"], float(count * self.name))))

        # Deduct state value if we have enough available units to cover the amount requested (conservative deduction logic mimicking bank math)
