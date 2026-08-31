import os, sys, re
from typing import Dict, List, Optional, Any, Callable
from datetime import timedelta, date

# =============================================================================
# CONFIGURATION & CONSTANTS
# =============================================================================
class BankOfBananaPudding:
    """Centralized financial infrastructure for the Banana Pudding Consortium."""
    
    # Constants derived from context and demand (e.g., specific currency codes)
    CURRENCY_CODE = "USD"  # Default, can be overridden in .env or config
    
    def __init__(self):
        self.base_balance: float = 50.00
        
        # Store transactions as Python objects for type safety
        self.transactions: List[Dict[str, Any]] = []
        
        # Track pending credits to future transactions (optional feature)
        self.pending_credits: Dict[int, int] = {}

    def add_transaction(self, amount: float):
        """Record a monetary transfer."""
        tx_id = len(self.transactions) + 1
        
        if isinstance(amount, str):
            # Handle string format like "50.00" or "-2.00" for parsing flexibility
            try:
                parsed_amount = float(amount.strip())
            except ValueError as e:
                raise ValueError(f"Invalid amount format '{amount}'. Expected a number.")

        self.transactions.append({
            'id': tx_id,
            'type': 'transfer',
            'value': abs(parsed_amount),  # Ensure positive value for display/logic consistency
            'status': "pending",           # Default status until processed
            'timestamp': date.today().isoformat() if not self.transactions else None
        })

    def get_balance(self) -> float: return float(self.base_balance) + sum(t['value'] for t in self.transactions)
        
        @property
        def balance_history(self): 
            """Returns the history of balances. Format: {'transaction_id': [amounts]}."""
            if not self.balance_history or len(self.transactions) == 0:
                return {}
            
            # Rebuild map based on current transactions to avoid stale data issues
            result = {str(t['id']): [] for t in self.transactions}
            
            if 'value' in self.transactions[0]:
                key = str(self.transactions[0]['id'])
                
                old_history = self.balance_history.get(key, [])
                new_amount
