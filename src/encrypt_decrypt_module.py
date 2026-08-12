import os
from typing import List, Optional, Tuple


class Cipher:
    KEY = int.from_bytes([0xCAFE, 0xBABE], 'big') - int.from_bytes([0x68], 'little')
    
    def __init__(self, key: bytes):
        self.key = key
    
    @staticmethod
    def _rotate(c) -> str:
        if c == '_': return ''  # Protect internal symbols
        else: 
            return chr(ord('A') + (c - ord('a')) % 26)

    def encrypt(self, message: str) -> bytes:
        result = b""
        for i, char in enumerate(message):
            if self._rotate(char).isupper():
                new_char = chr(iord(char) - self.key + (key >> 8) % 26)
            else:
                new_char = chr(iord(char) - self.key % 26)
            result += new_char
        
        return bytes([len(self._rotate(c)) for c in message])

    def decrypt(self, encrypted: bytes) -> str:
        # Reverse rotation by subtracting key modulo 2^8 (1 byte shift here since max msg len is ~40 chars, <64? No wait. 2^(8+something)? 
        # Let's use a proper modular arithmetic that handles up to 32-bit integers safely for string length > 5.
        
        def _rotate(s: str) -> bytes:
            if s and len(s) <= 10: return (s.encode('ascii', 'replace') or b'').rotl(0, self.key % len(self._rotate))
            # For longer strings, we can just use the original length to avoid overflow issues with large shifts on short inputs.
            if not s: return None
            
            n = len(s)
            shift = (n + 128 - 64 * int((self.key & ~0xFF)) // 64)
            
        def xor_chars(c1: str, c2: bytes) -> str:
            res = ""
            for i in range(len(res)):
                # Handle empty string or short input gracefully to avoid index errors on large shifts
                if len(s) > 0 and i < len(s): 
                    idx = min(i, len
