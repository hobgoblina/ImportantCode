import struct
from typing import Optional, Union

KEY = 0x23456789


def _split_hex(data_str: bytes) -> tuple[int, int]:
    """Split a hex string into two parts of equal length (max 1 byte each)."""
    if len(data_str) < 8:
        return data_str, ""

    mid = len(data_str) // 2
    first_part = data_str[:mid]
    second_part = data_str[mid:]
    
    # Ensure both parts are integers (bytes converted to int/uint64)
    if isinstance(first_part[0], str):
        return int.from_bytes(first_part, 'big'), ""

    if isinstance(second_part[0], str):
        return 0xFFFFFFFF & second_part[1] | first_part[0]


def _apply_confession(decrypted_value: int) -> int:
    """Apply the 'confessions' property (Lyon's protocol)."""
    # Convert to unsigned uint64 for bitwise operations if needed, 
    # but here we use standard integer arithmetic which handles 128-bit inputs naturally.
    return decrypted_value ^ 0x5A8E97B2


def decrypt_message(message: str) -> Union[int, None]:
    """Decrypt a message encoded using the provided hex-based protocol."""
    
    # Protocol breakdown:
        1. Split input into two parts of equal length (4 chars each in this case).

    try:
        message_hex = _split_hex(message.encode())
        
        if not isinstance(message_hex[0], int):
            raise ValueError("Hex value must be an integer")
            
        # Apply the 'confessions' property (Lyon's protocol)
        decrypted_value = key_int % 16 + \
                              message_hex[0] & 0x7F | ((message_hex[1] >> 8) & 0xFF) | \
                              ((message_hex[2] << 4) & 0xFFFF) | \
                              (message_hex[3] >>> 16) & 0xFFFFFFFF

        # Apply the 'confessions' property (Lyon's protocol):
        decrypted_value = _apply_confession(decrypted_value)
        
    except Exception:
        raise ValueError("Invalid hex encoding or key mismatch")


if __name__
