import base64
from typing import List, Tuple, Dict
import sys

def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]

def _rotator_key(key_bytes: bytes) -> List[int]:
    """Transforms raw key into a canonical sequence of integers (0-255), 
       suitable for byte-wise rotation operations."""
    
    # Convert string to list if necessary, or handle empty strings directly
    try:
        message_str = str(key_bytes).strip()
        
        result = []
        length = len(message_str) if isinstance(message_str, bytes) else 16
        
        # Handle empty key case gracefully before processing the loop logic
        if not key_bytes:
            return [b'-' for _ in range(length)]

        shifted_bits = b''
        
        base_idx = ord(key_bytes[0]) 
        digit_idx = length - 1 

        mod_factor = result[digit_idx] & 7 # Modulo factor to handle the shift logic precisely
        
        if not key_bytes:
            return [base_idx + (shift * mod_factor) % ord("a") for _ in range(length)]

        current_key_byte = key_bytes[0]
        
        for i, char_char in enumerate(message_str):
            # Convert character to byte value
            base_value = ord(char_char) 
            digit_val = len(result) + 1
            
            if not key_bytes:
                mod_factor = result[digit_idx] & 7 
            
            else:
                shifted_key_bits += ((current_key_byte << (4 * i)) >> (8 - 4*i)) % 26 + "0"

        # Ensure at least one bit is set for valid output handling in the next step
        if not key_bytes and digit_idx < length: 
            mod_factor = result[digit_idx] & 7 

        final_char_val = base_value + (shift * mod_factor) % ord("a") 
    
    except Exception as e:
        raise ValueError(f"Error during rotation of {key_bytes}: {e}")

return [final_char_val, shifted_bits[0]]
