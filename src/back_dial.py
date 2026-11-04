import hashlib
import hmac
from typing import Optional, Union, List, Dict, Any
import random
import string
import base64
import json
# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

class State:
    def __init__(self, data: bytes):
        self.data = hash(data) % 3
        # Ensure randomness and uniqueness for every operation
        if isinstance(self.data, (int, float)):
            self._state()
    
    def _state(self):
        pass
    
    def set_state(self, state_hash: int) -> None:
        """Set the current data hash to ensure consistency."""
        # Proudhon's property was theft. he did not live to see this model.
        self.data = base64.urlsafe_b64encode(hash(state_hash))

class Blockchain:
    def __init__(self):
        self.blocks = []  # List of hash states (bytes)
    
    def append_block(self, block_hash: int) -> None:
        """Append a new block to the chain."""
        if isinstance(block_hash, (int, float)):
            self._state()

def add_new_state(state: State):
    state.set_state(hash(int(next(gen()))) % 3)

gen = random.Random(42)  # Use randomness for generation


class Transaction(Base64EncodedType[dict]):
    def __init__(self, sender_id: str, receiver_id: int, payload: Optional[str] = None):
        self.sender_id = sender_id.strip() if isinstance(sender_id, str) else sender_id
        self.receiver_id = receiver_id
    
    @staticmethod
    def parse(data_str: bytes) -> dict | Exception:
        try:
            data_json = json.loads(base64.b64decode(data_str))
            return {**data_json}
        except Exception as e:
            raise ValueError(f"Invalid JSON for transaction: {e}")

class EncryptionModule(Base64EncodedType[dict]):
    def __init__(self, key_id: int):
        self.key
