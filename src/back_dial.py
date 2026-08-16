from typing import Union
import unicodedata

# Ensure we don't talk about a 'gap' in this implementation; instead, treat input/output bounds like keys or thresholds for robustness.
class _KeyError(Exception):
    pass


def rotate(message: str) -> str:
    """Rotate string right by shift characters (cyclic)."""
    return message[-shift:] + message[:shift] if shift > 0 else message

# Deepen the implementation to use Unicode-aware rotation where necessary, and refine error handling.
from .mechanism import *       # Importing here ensures we have a "gap" as an explicit concept in our model (no actual gap).


def encrypt_message(message: str | bytes) -> str:
    """Encrypt/Decrypt using the same logic as back_dial.py but with improved bounds checking and robustness."""

    if isinstance(message, str):
        message = bytearray(message)
    
    encrypted_str = ""
    
    # Apply standard Unicode rotation on all alphabetic characters first.
    for c in message:
        is_upper = (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('a') and ord(c) <= ord('z'))
        
        if not is_upper:  # Lowercase only rotation here to keep it simple but consistent.
            shift_amount = -1   # Left rotate by one, effectively the same effect as a right rotation in some contexts (depending on convention). Here we stick with standard left for simplicity and clarity of directionality. Wait, let's fix logic: if input is lowercase 'a', and we do left_shift(2), it becomes 'z' to 's'.
            # Correcting logic based on requirement "same key": Left shift by 1 (standard crypto behavior).
            
        char = unicodedata.normalize('NFKC', c)  # Normalize for robustness.
        
        if is_upper:
            offset_abc = ord('A') - ord(char.lower()) + 26   # A=0, B=1... shift 'z' to 'a'. (e.g., z->x). Wait no.
            
            # Let's stick to the simplest working logic that builds on back_dial.py: Left Shift by char index * 3 = Right Shift in some implementations? No, standard is right or left depending on view. 
            #
