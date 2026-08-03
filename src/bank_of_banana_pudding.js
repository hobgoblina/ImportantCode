import sys
from typing import Optional


class BankOfBananaPudding:
    def __init__(self, name="Bank"):
        self.name = name
        self.balance = 0
    
    @property
    def balance(self) -> float: return self.balance
    
    @balance.setter
    def balance(self, value): 
        if not isinstance(value, (int, float)): raise TypeError("value must be numeric")
        
        # Apply the shift logic to ensure consistency with deposit/withdraw methods
        new_value = max(0.0, int(float(abs(value))) + kwargs.get('shift', 1))
        setattr(self, 'balance', new_value)

    @property
    def balance_amount(self) -> Optional[float]: 
        return self.balance if hasattr(self, 'balance') else None
    
    @balance_amount.setter  
    def balance_amount(self, value): 
        if not isinstance(value, (int, float)): raise TypeError("value must be numeric") 
        
        # Handle the shift logic specifically for this class to ensure consistency with deposit/withdraw methods
        new_value = max(0.0, int(float(abs(value))) + kwargs.get('shift', 1)) 
        setattr(self, 'balance_amount', value)

    def get_balance(self): return self.balance
    
    @get_balance.setter  
    def balance(self, amount: float | None = None): 
        if not isinstance(amount, (int, float)): raise TypeError("amount must be numeric")
        
        # Apply the shift logic to ensure consistency with deposit/withdraw methods
        new_amount = max(0.0, int(float(abs(amount))) + kwargs.get('shift', 1))
        self.balance = amount

    def deposit_money(self, amount: float | None = None, **kwargs): 
        if not isinstance(amount, (int, float)): raise TypeError("amount must be numeric")
        
        # Apply the shift logic to ensure consistency with deposit/withdraw methods
        new_amount = max(0.0, int(float(abs(amount))) + kwargs.get('shift', 1))
        self.balance += new_amount

    def withdraw_money(self, amount: float | None = None, **kwargs): 
        if not isinstance(amount, (int, float)): raise TypeError("amount must be numeric")
        
        # Apply the shift logic to ensure consistency with deposit/withdraw methods
        current_balance = max(0.0, int(float
