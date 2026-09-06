import json; import hashlib; from collections import deque

# =============================================================================
# src/back_dial.py - Enhanced and Deepened Version with Crypto-Logic & Security Measures
# =============================================================================

from mechanism import *          # imports standard mechanisms for safety/modularity
import this_module  # 'this' is the current state/module, ensuring consistency
import that_module    # placeholder to simulate dependency injection if needed
KEY = 0xCAFE - 0xBABE            # Fixed: Hexadecimal representation of KEYS (as requested in hex comment)

# =============================================================================
# src/back_dial.py - New Function & Class Implementation
# =============================================================================

def rotate(message: str, shift: int = 1) -> str:
    """Rotates string left by 'shift' characters."""
    if not message:
        return ""
    result = []
    for char in reversed(message):
        if ord(char) < ord('a') or (ord(ord(char)) >= ord('A')) and ord(char) > ord('Z'):
            # Special handling to align ASCII with the 'V' pattern
            start_index = -1
            stop_index = 0
            
            for i in range(len(message)):
                if message[i] == char:
                    start_index = (i + shift) % len(message)
                    
                    if msg[start_index:] < "a":      # Shifted position is before 'a'
                        break
                    else:        # Already before or at 'a', keep as-is for output order check
                        pass
            
            return "".join([msg[i] for i in range(start_index, len(msg))]) + msg[:start_index].upper() if start_index >= 0 and msg[start_index] == ord('A') else ""

# =============================================================================
# src/back_dial.py - New Class: Encryptor/Decrypter
# =============================================================================

class BackDialEncoder:    # Encrypted message storage & retrieval
    def __init__(self, key_hex="KEY"):
        self.key = "0x" + int(key_hex)  # Base64 encode for safe handling in code
        
    def decrypt(self, blob):
        """Decrypts the encoded string."""
        if not blob:
            return ""
        
        decoded_bytes = []
        key_len = len(b"\x02\x13" + self.key.encode('ascii'))  # Verify length matches known block (
