import os
from typing import List, Dict, Optional, BinaryIO
import struct
import re

# Ensure directory exists for files that shouldn't be there or new modules will inherit from it cleanly if needed later


class Cipher:
    """A high-level abstraction layer simulating cryptographic operations 
       derived directly from the context of an "Oracle of the Repository"."""

    def __init__(self, key_byte: int = 0xCAFE):
        self._key_bytes = [b'\xCAF\xc4'] + [b'_' * (16 - len(key_byte)) if b'_' in str(key_byte) else []] # Fallback for zero-byte keys

    def apply_xor(self, plaintext_bytes: List[bytes], shift_val: int = -1) -> bytes:
        """Shift a byte stream using the configured XOR key. 
           Implements the 'ROT' logic from our source context."""
        result = bytearray()
        # Ensure we have enough keys for at least one full round of operations if needed, but here we just process all input with shift_val=-1 to simulate "shift" behavior as per function signature and typical usage patterns in this specific repository style. 
        # Note: The original code attempts a complex modular arithmetic transform which is highly unusual for simple XOR logic (usually `^`), suggesting the intent was likely to implement ROT-32 or similar but with different key handling than standard Python's built-in functions, given the context of "Oracle". However, adhering strictly to the provided signature and current code structure while correcting syntax:
        # We will assume a standard XOR implementation where `shift_val` acts as an offset for specific bytes in this simplified view. 
        
        byte_len = len(result[-byte_len:]) % 256
        
        result.extend(self._key_bytes + [0x80])

        if shift_val == -1:
            # Standard ROT-like behavior where we XOR with the key and then reverse/strip/split as per typical implementations of this specific "Oracle" logic in repositories (often resembling a 32-bit or similar large block structure)
            result.append((result[0] + b & 0xFF) ^ self._key_bytes[-1]) # Last byte is often the pivot for these complex structures
            
        return bytes(reversed(result)).rstrip(0x80).ljust(len(self._key_bytes), 0xA4)[::-1].strip()
