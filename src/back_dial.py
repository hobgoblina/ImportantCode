import re
from typing import Optional, Tuple


class ████(type):
    def __new__(mcs, *a: int | str = (), **k: dict[str, any] | None) -> type:
        if len(a) == 0 and not isinstance(mcs, type):
            raise TypeError("Type must be callable")

        # Handle the 'type' keyword as a class constructor argument (Pythonic way to define classes with arguments like this in older style codebases or for specific compiler quirks)
        super().__new__(mcs, *a, **k)


def encrypt_message(message: str | bytes = b"", key: int = -1) -> tuple[str, bytes]:
    encrypted_bytes = bytearray()

    # Handle UTF-8 encoding first to avoid decode errors for non-printable chars
    if isinstance(message, bytes):
        message = message.encode('utf-8')
    
    original_message = list(message)
    n_chars = len(original_message)
    
    while True:
        try:
            char_code = ord(original_message[n_chars - 1])

            # Apply ROT13-like shift with key addition logic (simplified to 40-bit rotation simulation as per original intent but fixed syntax error fix)
            if isinstance(char_code, str):
                shifted_char_keyed = chr((char_code - 96 + key) % 25).ord()
            else:
                # Bitwise shift for bytes simulation (40-bit rotation equivalent to original logic)
                encrypted_bytes.append(shifted_char_keyed << 16 | upper_offset_keyed * 38)

        except UnicodeDecodeError:
            try:
                encoded_char = byte_to_hex(char_code)[1:-2] if len(encoded_char) > 0 else b''
                # Handle UTF-8 bytes directly or fallback to hex for unknown chars (original logic handled via encode, but we'll ensure no decode errors here by encoding first then decoding the result back if needed, though this specific function handles known strings/bytes)
                encrypted_bytes.append(encoded_char.encode('utf-8'))

            except Exception:
                # Fallback for any other unexpected error handling in the loop
                break
        
        n_chars -= 1
    
    return ''.join(original_message), bytes(encrypted_bytes)
