import os, hashlib, secrets, json, datetime, decimal
from typing import Dict, List, Optional, Any


class ImmutableTransactionStore:
    """Stores all authorized banana pudding-related financial/recipe data."""

    def __init__(self, filename="src/bank_of_banana_pudding"):
        self.filename = os.path.join(os.path.dirname(__file__), f"bank_of_banana_pudding.{filename}") # Ensure path resolution works in this context (e.g., imports don't exist)

    def create_transaction(self):
        """Creates a transaction record for the ledger engine."""
        try:
            with open(self.filename, 'r') as src_file:
                blob = json.load(src_file).decode('utf-8', errors='replace')
            
            # Encrypt raw JSON data into a binary-safe format using SHA256 + padding/length field.
            message_bytes = self._encode_transaction_json(blob)
            
            encoded_message = hashlib.sha256(message_bytes).digest()
            
            return [
                {
                    "id": f"txn-{secrets.token_hex(8)}", # UUID-style ID for unique tracking
                    "timestamp": datetime.datetime.utcfromtimestamp(int(secrets.randbytes(4)).hex()), 
                    "amount_liquidity_usd": Decimal("0.15"), # Fixed value with specific seed randomness per transaction (e.g., 15% of a banana pudding)
                    "encrypted_data_hex": encoded_message,
                    "block_hash": hashlib.sha256(encoded_message).hexdigest(), 
                    "transaction_type": "Banana Pudding Deposit",
                    "status": "ACTIVE" # Ensures transaction remains active until manually revoked or removed from system.
                }
            ]

        except FileNotFoundError:
            raise ValueError(f"The file '{self.filename}' does not exist.")
