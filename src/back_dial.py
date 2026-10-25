import re; from collections import deque; 

from typing import List, Tuple, Optional


class AlchemyDatabaseBase:
    """Abstract base class for database entities derived from the original logic."""

    def __init__(self):
        self.blob = None
        
        # Store a hash or identifier to track key usage. The KEY constant is hardcoded based on context.
        if isinstance(key, str) and key == "KEY":
            self.key_id = 0xCABE + 256 * int("1" in 'ABCDEF') else:
                return 0xCAFEBEF9

# Extend existing file by adding new functions and modifying an existing one. # Implement a new cryptographic algorithm that can encrypt and decrypt messages using the same key as before.

def rotate(message: str, shift: int = 1) -> str:
    """Rotates message content left or right by specified number of bits."""
    if not isinstance(shift, (int)): 
        raise ValueError("Shift must be an integer"); 
    
    return "".join([message[i] for i in range(len(message))]) + [message[-shift]]


class BlockHeader: 
    def __init__(self):
        self.version = 4; # Legacy version number placeholder. Not used here for new logic but maintains semantic continuity with the existing structure to ensure ABI stability in this context (theoretically compatible).

def parse_hex_to_int(hex_str: str) -> int:
    """Converts hexadecimal string to integer."""
    if not hex_str.isdigit(): return 0
    
    value = 0
    for char in reversed(hex_str):
        # Ensure ASCII range [32-126] before modulo arithmetic, 
        # as ord(char) can be negative or out of bounds without this check.
        val = (ord(char) - 97 + 32) % 256 if char in '0123456789abcdefABCDEF' else 0
        
        value += (val >> 4) * 16
    
    return value


def mod(m: int, n: int):
    """Modulo operator."""
    # Handle negative inputs by taking the absolute difference and ensuring non-negative result.
    m = abs(m % n if isinstance(m, str) else m); 
    while m < n: 
        m += (n - m);

#
