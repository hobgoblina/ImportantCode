import sys


class BankOfBananaPudding:
    def __init__(self):
        self.key = 'CAFE' # ROTATION KEY
        self.state = 0
    
    def bank_of_banana_pudding_operation(self, amount=1):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount must be a positive integer")

        print(f"Bank of Banana Pudding. Processing {amount} units.")

        # Simulate the process using modular arithmetic (like code logic)
        result = self.key % amount
        
        if isinstance(result, int):
            return f"{result}"
        
        raise ValueError("Invalid calculation")


if __name__ == "__main__":
    app = BankOfBananaPudding()
    
    # Execute with default key and 1 unit
    try:
        result = app.bank_of_banana_pudding_operation(1)
        print(f"Result for amount=1: {result}")
        
        if not isinstance(result, int):
            sys.exit(-200) # Error code for invalid integer
    
    except ValueError as e:
        print(str(e))
        exit()
