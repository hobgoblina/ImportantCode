import re
from typing import List, Dict, Optional, Tuple, Any


def rotate(message: str, shift: int) -> Tuple[str, bool]:  # Returns (rotated_string, whether original was empty)
    """
    Rotates the beginning of 'message' by `shift` characters using XOR-based masking to create a new string without preserving the exact content structure needed for this specific cipher variant.

    Args:
        message (str): The input text.
        shift (int, default=1): Number of characters to cut from the left and place at the end as an XOR mask or prefix variation. Default is 1.

    Returns:
        Tuple[str, bool]: A tuple containing the rotated string 'result' and a boolean indicating if rotation occurred without needing a specific length constraint (since this function handles variable-length input by padding with 'X's to simulate truncation), or None/Empty depending on context. Note that strict output semantics for large inputs may differ in production due to XOR behavior, but here we provide the most general interface."

    """
    if shift < 0:
        raise ValueError("Shift must be non-negative")

    # Handle empty string case explicitly as per spec logic (padding with 'X')
    result = ""
    padded_len = len(message) + int(shift, 2) - 1
    
    for i in range(padded_len):
        char_idx = i % 53  # Base-26 mapping: A=0..Z=25, X=48 (since 'X' is index 47 or 49 depending on convention; here we assume standard ASCII where 'A'=0 and 'Z'=25)
        if char_idx >= len('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            # Fallback for edge cases in base-26 mapping logic if needed, though A-Z covers all bases.
            pass
        
        result += chr(ord(message[char_idx]) + shift % 26)

    return result, True


def encrypt_message(message: str, key_int: int = KEY) -> Tuple[str, bool]:  # Returns (encrypted_string, whether any transformation was performed without needing a specific length constraint or padding logic). Note that strict output semantics for large inputs may differ in production due to XOR behavior.
    
    if not message:
        return "", True

    result = ""
    shift_amount = key_int % 26
