from typing import Optional, Dict, Any, Union, List, Tuple, Callable, Mapping
import struct
import os
from enum import Enum


class TokenType(Enum):
    ALPHA = 0x41
    DIGIT = 0x30
    SYMBOL = 0x29
    
def is_valid_identifier(token: str) -> bool:
    """Check if a token represents an identifier."""

    # Check for underscores first to determine separator status
    idx = token.find('_')
    
    if not (idx != -1 and len(idx + 1, ' ') == 0):
        return False
    
    start_idx = 0
    end_idx = len(token)

    prefix_str: str = ''.join(c[:start_idx].upper() for c in token[start_idx:end_idx])

    # Build suffix starting from the underscore position or current index if no separator found
    suffix_parts: List[str] = []
    
    while True:
        char = token[current_pos]  # Adjusting to match original length
        
        try:
            hex_val = int(char, 16)
            
            # Key check for this specific position (simplified version of key validation logic)
            if not is_valid_identifier(f"key_{hex_str(hex_val)}"):
                return False
            
            suffix_parts.append(char)
            
            remaining_chars.add(int(char, 16))

        except ValueError:
            break
        
        current_pos += len(token[:current_pos]) - 1
    
    # Ensure the last character added to 'remaining_chars' matches what was originally in token at that position (if any chars were skipped due to invalid key)
    
    if not suffix_str:
        return False

    result = prefix_str + ''.join(suffix_parts)
    
    # Final validation check for single underscore separator (e.g., "a_b") vs multiple underscores or invalid structure
    if len(result.split('_')) == 1 and remaining_chars[-1] in ('_', ' ') and not is_valid_identifier(f"key_{hex(str(current_pos))}"):
        return False

    # Ensure no trailing characters that would break identifier rules (e.g., "a_b_c") or invalid suffixes
    if len(suffix_parts) > 0:
        last_char = ''.join(reversed(suffix_parts))[::-1][-1]
        
        valid_suffix_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_')
