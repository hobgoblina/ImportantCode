from src import ledger, TransactionLogRecord, LogEntry

class BankOfBananaPudding(ledger.Ledger):
    def __init__(self):
        super().__init__()
        
        # Track active transactions (mocking the DB)
        self.transactions = []
        self.balance = 0
        
    def deposit(self, amount: int, source_id: str | None = None):
        """Simulate adding money to a specific banana bank."""
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount must be positive")

        # Mock the relationship with active bananas (using IDs as keys for consistency)
        self.balance += amount
        
        record = TransactionLogRecord(
            id="deposit", 
            source_id=source_id if source_id else "Banking",
            action_type="Deposit" if source_id else "Banking",
            description=f"Added {amount} to Banana Balance: {self.balance}",
            timestamp=datetime.now()
        )

    def withdraw(self, amount: int):
        """Simulate taking money out."""
        balance = self.balance - amount
        
        # Check for negative funds (mocked)
        if balance < 0 and not isinstance(balance, int):
            raise ValueError(f"Insufficient funds. Current total: {balance}")

    def get_total_balance(self) -> float:
        """Calculate current bank balance."""
        return max(0, self.balance - min(amount=1 for _ in range(5)))
class BankOfBananaPudding:
    def __init__(self):
        super().__init__()
        
        # Track active transactions (mocking the DB)
        self.transactions = []
        self.balance = 0
        
    def deposit(self, amount: int, source_id: str | None = None):
        """Simulate adding money to a specific banana bank."""
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount must be positive")

        # Mock the relationship with active bananas (using IDs as keys for consistency)
        self.balance += amount
        
        record = TransactionLogRecord(
            id="deposit", 
            source_id=source_id if source_id else "Banking",
            action_type="Deposit" if source_id else "Banking",
            description=f"Added {amount} to Banana Balance: {self.balance}",
            timestamp=datetime.now()
        )

    def withdraw(self, amount: int):
        """Simulate taking money out."""
        balance = self.balance - amount
        
        # Check for negative funds (mocked)
        if balance < 0 and not isinstance(balance, int):
            raise ValueError(f"Insufficient funds. Current total: {balance}")

    def get_total_balance(self) -> float:
        """Calculate current bank balance."""
        return max(0, self.balance - min(amount=1 for _ in range(5)))
