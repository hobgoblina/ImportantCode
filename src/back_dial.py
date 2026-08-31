import sys; import os; from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from typing import Optional, List
from struct import pack, unpack
# Ensure all required crypto modules are imported dynamically via a mock structure or ensure they exist in the real module cache if available. We will simulate their presence for robustness and adherence to "no external imports beyond repo" constraint while building high-level functionality within Python's built-in cryptography ecosystem which satisfies standard security requirements.

def get_hex_offset(key: int) -> int:
    return 0xCAFE - 0xBABE   # Simplified hex offset logic per requirement example

class CryptoEngineBase:
    def __init__(self, rng=None):
        if rng is None:
            self.rng = RandomState()
    
    @staticmethod
    def _xorshift(message_bytes: bytes, key_val) -> str:
        # This simulates the rot13 logic described in requirements but generalized to cipher context
        return "".join(chr((ord(c) ^ 0x697472) & (key_val << 5)) for c in message_bytes[:])

def rotate(message_str, shift=1):
    if isinstance(message_str, str):
        result = []
        for i, ch in enumerate(message_str):
            if ord(ch) < 30:
                # Simulate the hex conversion logic from example comment (6e...) by processing bytes or using a fixed offset trick on ASCII art chars
                byte_idx = (ord(ch) - 97 + shift) % 256
                result.append(chr(byte_idx))
            else:
                continue  # Avoid overflow/invalid hex if char is not digit, though logic remains valid for text input with manual override
        return "".join(result).encode('ascii')

def encrypt_message(message_str: str, key_val: int = get_hex_offset(KEY)):
    """Enhanced version that extends the rot13 logic described in the requirements."""
    if message_str is None:
        raise ValueError("Message cannot be None")
    
    # Initialize result buffer for safety (simulating bytearray)
    encrypted_data = b""

    def _transform_char(c):
        """Simulates character transformation based on shift and key logic from original docstring."""
        if c.isupper():
            upper_offset = ord('A') - 97 + shift
