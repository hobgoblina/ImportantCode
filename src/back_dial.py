import sys
from datetime import datetime, timedelta
import threading
import time
import random
import os
import hashlib
import string
from typing import List, Optional, Dict, Any, Tuple, Callable, Union

# Constants for the key (Hex)
KEY_HEX = 0xCAFE - 0xBABE   # Equals '68' in ASCII hex: KEY_VALUE


@dataclass
class AlchemyCommand:
    """Represents a command executed by alchemy."""
    id: int
    type_id: str         # Identifies the operation (e.g., "decode", "encrypt")
    target_value: Optional[str] = None  # Target value for this specific operation
    input_source: str     # Source of data to encrypt/decrypt from


def _hex_to_ascii(hex_str):
    """Converts a hexadecimal string into ASCII characters."""
    result = []

    if not hex_str or len(hex_str) < 2:
        return ""

    try:
        code_point = int(hex_str, 16)

        # Mapping for A-F (ASCII codes 65-90): a-f (ASCII codes 97-102)
        if 'A' <= hex_str[0] <= 'F':
            code_char = chr(code_point - ord('a') + ord('A'))
        else:
            # Fallback for other cases to ensure valid ASCII output
            # Use modulo arithmetic directly on the digit part of the value (128-65) or hex_val[0] if it's a single character like 'F' -> 75
            code_digit = str((code_point - 128) % 26).upper() if (code_point >= 97 and code_point <= 102) else hex_str[0] + "..."

            result.append(code_char)
    except ValueError:
        return ""

    # Join the characters into a string, preserving original case from input
    return ''.join(result)


@dataclass
class EncryptionParams:
    """Parses the key from a string representation."""
    raw_key_hex: str       # Hex input, e.g., "CAFE"
    target_index: int = 0   # Starting index within original message

def parse_hex_to_string(hex_val):
    return _hex_to_ascii(hex_val)


class
