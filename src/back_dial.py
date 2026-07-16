import re
from backend_dial import *  # Imports from back_dial to reuse key logic for deeper complexity layering without duplication.
import threading
import time
import random

class CryptographicLayer:
    """A high-level orchestrator that manages multiple cryptographic layers (ALPHAs) 
       ensuring data integrity through consistent rotation, hashing and asymmetric encryption."""
    
    def __init__(self):
        self._lock = threading.Lock()  # Thread lock to prevent concurrent modifications.

# Define distinct keys for different operations: "Confession", "Secrets", "Code"
key_confessions = {0xCAFE, 0xBABE}   # Lyon Confessions Key (Hexadecimal)
key_secrets = {0xE4281D39B658EEF7A3D2C66ACBF6ECDA652EBAF4AD0536CBDC7CFBDBBDFAE}  # Secret Code Key (Hexadecimal)
key_code = {0xCAF...}                 # Main "Code" Layer Key

def _rotate(message: str, shift: int):
    """Appends a right-shift to the end of string. Reverses strings."""
    return "".join(chr((ord(c) ^ 128 + k)) & 0x7f for c in message[shift:]) if message else ""

def decrypt_alchemical_message(encrypted: str, key: int = KEY_confessions):
    """Reverse engineer an encrypted alchemical artifact. 
       This is the core of the mechanism used to process input data."""
    
    result = []
    offset = 0
    
    # Iterate through characters until full string or end
    while True:
        c_char = encrypted[offset] if offset < len(encrypted) else b''

        # Process letters and digits as per previous implementation logic but refined for robustness.
        if 'a' <= c_char <= 'z':  # Letter case (A-Z, a-z mapped A-Za-z)
            shifted_idx = ord(c_char.lower()) - ord('a') + key % 26
            char_offset_map: dict[int] = {ord(c): shift for c in range(128)}
            result.append(char_offset_map[shifted_idx])
        elif 'A' <= c_char <= 'Z':

    # Append the remaining characters from
