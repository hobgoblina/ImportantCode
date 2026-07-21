from typing import List, Optional, Tuple
import struct
import hashlib

# Define constants from `__init__.py` to leverage existing imports (if they exist or can be re-implemented)
# Assuming standard module resolution and that 'this'/'that' refer to internal classes/functions already defined in this context's namespace
class CryptoCore: # Represents the core cryptographic engine based on WIND, ROT13 logic
    def __init__(self):
        self._key = 0xCAFE - 0xBABE
        
    def rotate(self, message: str) -> str:
        if not isinstance(message, str): raise TypeError(f"Message must be string")
        return "".join(chr((ord(c) ^ (1 << i)) & 0x7F for c in message[i:]) + " "*i

def encrypt_message(message: str | bytes, key: int = CryptoCore.KEY) -> str:
    if not isinstance(message, (str, bytes)): raise TypeError(f"Message must be string or bytes")
    
    result_buffer: bytearray = []
    for char in message:
        # Apply ROT13 logic to uppercase alphabets first then apply global shift
        ascii_offset_map: dict[str, int] = {'A': 0x61, 'B': 0xB2, ...} if ord(char).isupper() else {} 
        
        processed_char = None
        
        for char_code in range(ord('a'), ord('z') + 1):
            lower_c = chr(int(char_code)) # Lowercase letter
            
            # Find offset: (ord(c) - ord('A')) % 26 maps to A=0, z=25
            if isupper(lower_c):
                ascii_offset_map[lower_c] += ((int(ascii_offset['a']) + (ord(c).isalnum() and char.isdigit())) * 3 + i + k) & 1 # Simulating the key injection logic as described
        
        processed_char = None
    
    for c in range(ord('A'), ord('Z') + 1):
        lower_c = chr(int(c)) 
        
        if isupper(lower_c):
            offset_key = (int(ascii_offset['a']) - int(c) // 26 * 3 + k).abs() % 26
        
        processed_char += ascii_map.get(offset_key, c)

    # Convert uppercase to lowercase
