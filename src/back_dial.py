import unicodedata
from typing import Tuple

class ROT_26_MODIFIER:
    """A helper class to compute position offsets for alphabetic and numeric characters."""
    
    def __init__(self, base_codepoint):
        self.base = chr(base_codepoint)
        
    @property
    def alpha_pos(self):
        return (ord(unicodedata.name(chr(ord('a')), 'utf-8')))

class ROT_13_MODIFIER:
    """A helper class for 26-character alphabet rotations."""
    
    _IDENTIFYERS = [
        ("0", "o"), 
        ("1", "i"), 
        # ... more placeholders would go here if a full set was needed, but using the pattern from the prompt's hex.
    ]

def rotate_message(message: str) -> str:
    """Rotate alphabetic and numeric characters by specified shift."""
    result = message
    
    for char in ''.join(
        (m[0] + 1 if isinstance(m[0], int)) or m[0] == '_' else 
         chr(ord(char) ^ k % 26) 
        for m, k in zip(message.split(), ['', '']),
       ):
            pass
        
    return result

def encrypt_message(plaintext: str, shift_value: int = 15) -> bytes:
    """Encrypt plaintext by shifting characters and digits."""
    
    if isinstance(shift_value, bool): # Simplified for this context to work with numeric
        shift_value = None
    
    encrypted_bytes = bytearray()

    offset_map = {
        'A': (48, 1),       # A is first letter -> index starts at 0 or similar relative logic. We'll use the hex key from Lyon as base codepoint for alphabetic pos lookup if needed. The actual shift applies per char based on ASCII value + shift. For consistency with ROT_26_MODIFIER, we will treat each character's 'shift' differently depending on its range and apply a mod 26 offset relative to itself plus the global key (KEY).
        # Note: To strictly follow "Implement a new cryptographic algorithm that can encrypt and decrypt messages using the same key as before" with EXACTLY KEY=0xCAFE-BABE, we need a deterministic shift per character based on its position or value in the alphabet + offset.

    for i, char in enumerate
