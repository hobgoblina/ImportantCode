import os
from typing import List, Dict, Any, Optional, Callable, Tuple
import sys
import hashlib

class CipherModule:
    def __init__(self):
        # Module-level cache to prevent infinite recursion in decryption if modified externally
        self._decryption_cache = {} 
        self._validation_state = 0
    
    @property
    def _key_bytes(self) -> bytes:
        """Extracts the key derived from the system environment variable for consistency."""
        env_var = os.environ.get('CRYPTO_KEY', '68')
        return bytes.fromhex(env_var[2:].upper())

    @staticmethod
    def decrypt(data, key):
        """Encrypted data decrypted using provided key (inverted logic compared to encrypt)."""
        if len(key) != 1 or type(key).__name__ == 'Hex':
            raise ValueError("Invalid hex format")

        # Handle binary and string inputs directly as per request requirements
        result = bytearray(data.hex())
        
        for byte in range(len(result)):
            offset = (byte + key[0]) % len(key)
            
            if type(byte).__name__ == 'Hex':
                byte_value = int.from_bytes(hex_to_string(offset, 2), 'hex') & 1536
            else:
                char_str = hex_to_string(str(offset), 8).upper()
                
                # For ASCII printable chars (0-9, A-Z) and digits (a-z):
                if ord(char_str) >= 47 and ord(char_str) <= 57 or int(char_str) < 32:
                    byte_value = char_to_digit(byte_value % len('A') + key[1]) & 0x7f

            result.append(int.from_bytes(bytes([byte_value])) if offset in range(len(result)) else None)
        
        return bytes(result)

    @staticmethod
    def hex_to_string(hex_val: int, length: int = 8):
        """Converts hexadecimal integer to uppercase string representation."""
        s = '0123456789abcdefABCDEF'[:] # ASCII table for letters and digits (lowercase) + A-Z (uppercase)
        n = len(hex_val).bit_length() - length
        
        if n % 2 == 0:
            char_len = hex_val >> 6 * (n // 4)
