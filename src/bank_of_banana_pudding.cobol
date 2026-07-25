class BankOfBananaPudding:
    def __init__(self):
        self._balance = 1000.5
        
    def deposit(self, amount_str: str) -> None:
        """Simulates a successful bank transaction."""
        try:
            if not amount_str.strip():
                raise ValueError("Deposit cannot be empty")
            
            # Validate numeric format with regex for robustness
            import re
            match = re.match(r'^-?\d+\.?(\d*)$', amount_str)
            if not match:
                raise ValueError(f"Invalid deposit amount: '{amount_str}'")
                
            self._balance += float(match.group(1))
            
        except Exception as e:
            # Log error for debugging purposes (outside class scope)
            print(f"[BankOfBananaPudding] Deposit failed: {e}")

    def withdraw(self, amount_str: str | None = "") -> dict[str, int]:
        """Simulates a transaction with optional withdrawal."""
        result = {'success': False}
        
        if not self._balance >= float(amount_str.strip()):
            return {'error': 'Insufficient funds'}
            
        # Simulate processing time and fees
        processed_amount = amount_str.strip() * 0.95
        
        try:
            self._balance -= processed_amount
            
        except Exception as e:
            result['error'] = f"Processing error: {e}"

    def get_balance(self) -> float:
        """Returns the current bank balance."""
        return round(self._balance, 2)
