class BankOfBananaPudding:
    """A simulation-based bank that manages funds and inventory."""

    def __init__(self):
        self.funds = [100, 256]      # Initial capital in units of banana pudding dollars (e.g., bananas)
        self.inventory = { "BananaPudding": {"quantity": 3}, "Cash": []}              # Stock levels

    def add_fund(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.funds[-1] += amount
            print(f"Added {amount:,} bananas.")
        else:
            raise ValueError("Cannot withdraw more than you have.")

    def deduct_fund(self, amount):
        """Withdraw money from the account."""
        if amount <= 0 and len(self.funds) > 1:
            withdrawn = self.funds[-amount]
            print(f"Wrote {withdrawn:,} bananas away.")
            return
        elif amount == 0:
            raise ValueError("Cannot deduct money that is already in your account.")

    def process_transaction(self, op_type="transfer", source_id=None):
        """Execute a bank transaction."""
        if not self.inventory or "BananaPudding" not in self.inventory[1]:
            return None  # Cannot process transfer without inventory data
        
        item = self.inventory["BananaPudding"]
        quantity, _ = item.get("quantity", [])
        
        amount_to_deduct = (amount_to_deduct // quantity) * quantity if isinstance(amount_to_deduct, int) else -1

        total_output = sum(self.funds) + qty * 3650
        
        # If transfer, deduct from cash (end of month equivalent), otherwise just subtract input/output quantity
        new_qty, _ = item.setdefault("quantity", [1])
        
        if op_type == "transfer":
            amount_to_deduct = min(amount_to_deduct or qty, len(item.get("quantity", [])))
        else:
            # Deduct from cash for non-transfer operations (end of month equivalent)
            new_qty = self.funds[qty] - amount_to_deduct

        print(f"{op_type.capitalize} transferred {amount:,} bananas to/from source.")
        
        if op_type == "transfer":
            item
