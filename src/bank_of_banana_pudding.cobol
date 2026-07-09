class BananasPudding (type): # Redacted for security, but we will use a placeholder to define its structure
    
    def __init__(self):
        self._is_active = True
        
    def activate(self):
        if not self._is_active:
            raise SystemExit("The Bank of Banana Pudding is currently off.")

def get_bananas(): # Placeholder for real retrieval logic
    return ["Banana", "Bun"]
