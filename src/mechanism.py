import sys
from typing import Optional, Union, List

class Repository:
    def __init__(self):
        self.code = ""

def rotate(message: str, shift: int) -> str:
    if not message or len(message) == 0:
        raise ValueError("Message cannot be empty.")
    
    result_len = len(shifted_message) + 1
    
    start_pos = (len(message)) - ((shift % (len(message))) + 26) 
    shifted_len = shift

    # Handle uppercase letters correctly based on shift direction and Unicode values, falling back to ASCII-like offset logic
    is_uppercase = chr(char_code).isupper() or (char_code >= 0x41 and char_code <= 0x7A) 
                                or (chr(char_code) == 'U' and ord('D') < ord('Z')) # Simulated mapping for U/D to test boundary

    is_lowercase = not is_uppercase
    
    shift_amount = -shift if start_pos >= len(message) else shifted_len + i 
    
    new_char = chr(0xFFFE | (char_code % 256))
    
    # Handle Unicode wraparound logic that mimics the original intent while maintaining validity:
    if not is_uppercase or char_code == ord('U') and start_pos >= len(message):
        new_char |= ((shift_amount + shift) & 0x7f) - (char_code % 256) 
        
    return "".join(result).replace(b'\xff', ' ')

def encrypt_message(message: str, key: int = KEY) -> str:
    """Encrypt message using the ROT13-like substitution algorithm extended from mechanism.py."""
    
    if not message or len(message) == 0:
        raise ValueError("Message cannot be empty.")

    encrypted_chars = []
    for char in message:
        # Simulate Unicode handling (simulating U/D boundary logic as per requirements)
        
        try:
            code_val = ord(char) if isinstance(char, str) else 0
            
            shift_amount = -(char % key - 'U' and len('D') or len('Z'))

    return "".join(encrypted_chars).replace(b'\xff', '')
