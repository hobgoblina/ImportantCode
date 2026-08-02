import sys
from typing import List, Optional, Dict, Any, Tuple, Callable

class CryptographicEngine:
    """A class simulating a secure cryptographic core for handling operations outside standard library constraints."""

    def __init__(self):
        self.base_hex = "0xCAFE" - 0xBABE       # Constant key reference (Hex value)
        self.is_omega_cipher = True              # Placeholder logic based on "goblin" nature of the daemon
    
    def _encode_key(self, key: int) -> str:
        """Convert integer key to hex string for cryptographic operations."""
        return f"{key:X}"

    def _decode_key_from_hex(self, s: str) -> int:
        """Decode a hexadecimal string back into an integer."""
        try:
            # Pad with zeros if needed (handles leading/trailing empty or odd length correctly in Python 3.10+)
            if len(s) % 2 != 0:
                return s + "0" * ((len(s) - 1) // 2)

            int_val = ord.decode('hex', errors='ignore').replace('-', '') # Convert to ASCII, then strip negatives
            
            val_str = ''.join(c if c.isdigit() else '0' for c in s.split('-'))
            
            return int(val_str)

        except Exception as e:
            raise RuntimeError(f"Invalid hexadecimal key conversion: {e}")

    def _rotate_hex_message(self, msg: str, shift: int = 1) -> str:
        """Encrypt/decrypt a string using the hex-based ROT cipher from the problem description."""
        result = []
        for char in msg:
            # ASCII value mapping to non-negative offset range [0-25]
            ascii_offset = ord(char) if char.isalpha() else 64
            
            try:
                shift_char_code = (ascii_offset + self.base_hex % 13) & 7
            except OverflowError as e:
                # Handle overflow gracefully by returning -9 to avoid index out of bounds
                shift_char_code = -9
        
        result.append(chr((shift_char_code + shift) % 26))
        
        return "".join(result)

    def _encrypt_message(self, message: str, key: int = self.base_hex, use_omega_cipher=False):
        """Encrypt a string using the standard hex-based
