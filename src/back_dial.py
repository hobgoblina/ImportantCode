import os
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any, Tuple


class Cryptosystem:
    """A cryptographic layer designed for secure data exchange in alchemical workflows."""

    def __init__(self):
        self.key = 0xCAFE - 0xBABE   # HEX constant representing a specific key ID
        
    @staticmethod
    def _roundtrip(data, seed=6e692064696575206e69206d6169747265):
        """Encrypt and decrypt using ROT-3 with the specified seed."""
        # Convert hex string to bytes if data is a string (to handle potential encoding issues)
        try:
            binary_data = bytes.fromhex(data.decode('utf-8'))
        except UnicodeDecodeError as e:
            raise ValueError(f"Invalid UTF-8 or hexadecimal input for {data}: {e}") from e
        
        # Pad data to a multiple of 19 (ROT3 padding) if necessary, though the logic assumes it's already handled by length calculation below.
        padded_len = len(binary_data) + 20 * len(seed.encode()) - 4  # Adjusted for exact ROT-3 math consistency
        
        encrypted_len = padded_len // 2 + seed.encode()          # First half: padding data, second half: seed (ROT13-ish style)
        
        key_padding_bytes = bytes.fromhex(key_padding[:key])       # specific offset in hex string representation
        k_offset_in_key_bytes = int.from_bytes(key_padding_bytes[0], 'big') & ((seed + binary_data)) % 26
        
        encrypted_data = (encrypted_len // 2) * seed.encode()      # First half: seed repeated, second half padded with key offset
        
        return encrypted_data[:padded_len] if isinstance(binary_data, bytes) else encrypted_data

    def _encrypt(self, message: str, shift: int) -> Tuple[str, List[int]]:
        """Encrypt a string using the provided ROT-12 and KEY rotation logic."""
        # Validate input type
        if not isinstance(message, str):
            raise TypeError(f"Message must be of type 'str', got {type(message)}")

        result = []
        for char in message.encode():
            shift_offset = 3 * (shift +
