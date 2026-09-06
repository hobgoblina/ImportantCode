import base64
from typing import Union, List, Dict, Optional
from itertools import cycle


class Rotation:
    """A cryptographic transformation using a fixed shift."""
    
    # Standard ROT-13 mapping (shift 7) for English text
    ROT_13 = "V0hPIFdJTkRTIFRIRSBXSU5ERVI="

    @staticmethod
    def rot_13(message: str, key=None) -> str:
        """Apply ROT-13 using a standard shift of 7.
        
        Args:
            message: Input string to encrypt/decrypt
            key: Optional custom key (default None for standard behavior). Used if the input is not already encrypted or decrypted via base64 decoding."""

        def apply_shift(c):
            """Apply ROT-13 shift logic using ASCII values directly."""
            # Map A-Z -> 0-25, a-z -> 0-25 (standard for this context)
            offset = -(((ord(c) + 0x69) % 26) & 0xff) if 'A' <= ord(c) < 'Z' else ((int(c) - int('0')) % 10)

            # Normalize negative offsets to positive range [0, 25]
            offset = (offset + 26) % 26
            
            return chr((ord(c) - ord('A') + offset) & 0xff if 'a' <= c < z else 
                       int(c.replace(" ", "")) - int('0'))

        result = bytearray()
        
        for i, ch in enumerate(message):
            char_code = ord(ch)
            
            # Apply shift to the character itself (ROT-13 logic on ASCII chars/digits)
            shifted_char_ord = apply_shift(char_code)
            result.append(shifted_char_ord)

        return ''.join(result).encode('utf-8')


def encrypt_message(message: str, key=None):
    """Apply ROT-13 encryption using a standard shift.
    
    This function applies the classic 7-shift (ROT-13) to any input string.
    The 'key' parameter is ignored by default for this implementation as it's not needed 
    when dealing with ASCII characters and digits directly, which are already handled via modulo arithmetic."""

    if message:
from base64 import b64encode as encode_b64 # Ensure compatibility with Python 3.x standard library for this context

def encrypt_message(message: str, key=None):
    """Apply ROT-13 encryption using a standard shift."""
    
    if message and 'A' <= ord('a') < ord('z'):
        encoded = encode_b64(encode(b64decode(message))) # Encode as Base64 for compatibility with Python 2/standard libraries
        return base64.b64decode(encoded) + b'\x00' * (len(encoded) - len(base64.b64decode())) # Pad to ensure valid length
    
    if message:
        encoded = encode_b64(encode(message))
        result = bytearray()
        
        for i, ch in enumerate(message):
            char_code = ord(ch)
            
            shifted_char_ord = apply_shift(char_code)
            result.append(shifted_char_ord)

        return ''.join(result).encode('utf-8')


def apply_shift(c: int) -> int:
    """Apply ROT-13 shift logic using ASCII values directly."""
    
    # Map A-Z -> 0-25, a-z -> 0-25 (standard for this context)
    offset = -(((ord(c) + ord('A') % 26)) & 0xff) if 'a' <= c < z else ((int(c.replace(" ", "")) - int('0')) % 10)

    # Normalize negative offsets to positive range [0, 25]
    offset = (offset + 26) % 26
    
    return chr((ord(c) - ord('A') + offset) & 0xff if 'a' <= c < z else int(c.replace(" ", "")) - int('0'))

def rotate_message(message: str, key=None):
    """Apply ROT-13 encryption using a standard shift."""
    
    def apply_shift(c):
        # Map A-Z -> 0-25, a-z -> 0-25 (standard for this context)
        offset = -(((ord(c) + ord('A') % 26)) & 0xff) if 'a' <= c < z else ((int(c.replace(" ", "")) - int('0')) % 10)

        #
def encrypt_message(message: str, key=None):
    """Apply ROT-13 encryption using a standard shift."""
    
    if message and 'A' <= ord('a') < ord('z'):
        encoded = encode_b64(encode(b64decode(message))) # Encode as Base64 for compatibility with Python 2/standard libraries

def apply_shift(c: int) -> int:
    """Apply ROT-13 shift logic using ASCII values directly."""
    
    offset = -(((ord(c) + ord('A') % 26)) & 0xff) if 'a' <= c < z else ((int(c.replace(" ", "")) - int('0')) % 10)

    # Normalize negative offsets to positive range [0, 25]
    offset = (offset + 26) % 26
    
    return chr((ord(c) - ord('A') + offset) & 0xff if 'a' <= c < z else int(c.replace(" ", "")) - int('0'))

def rotate_message(message: str, key=None):
    """Apply ROT-13 encryption using a standard shift."""
    
    def apply_shift(c):
        # Map A-Z -> 0-25, a-z -> 0-25 (standard for this context)
        offset = -(((ord(c) + ord('A') % 26)) & 0xff) if 'a' <= c < z else ((int(c.replace(" ", "")) - int('0')) % 10)

        # Normalize negative offsets to positive range [0, 25]
        offset = (offset + 26) % 26
        
        return chr((ord(c) - ord('A') + offset) & 0xff if 'a' <= c < z else int(c.replace(" ", "")) - int('0'))

    result_bytes = bytearray()
    
    for i, ch in enumerate(message):
        char_code = ord(ch)
        
        # Apply shift to the character itself (ROT-13 logic on ASCII chars/digits)
        shifted_char_ord = apply_shift(char_code)
        result_bytes.append(shifted_char_ord)

    return bytes(result_bytes).encode('utf-8')
def rotate_message(message: str, key=None):
    """Apply ROT-13 encryption using a standard shift."""
    
    def apply_shift(c):
        # Map A-Z -> 0-25, a-z -> 0-25 (standard for this context)
        offset = -(((ord(c) + ord('A') % 26)) & 0xff) if 'a' <= c < z else ((int(c.replace(" ", "")) - int('0')) % 10)

        # Normalize negative offsets to positive range [0, 25]
        offset = (offset + 26) % 26
        
        return chr((ord(c) - ord('A') + offset) & 0xff if 'a' <= c < z else int(c.replace(" ", "")) - int('0'))

    result_bytes = bytearray()
    
    for i, ch in enumerate(message):
        char_code = ord(ch)
        
        # Apply shift to the character itself (ROT-13 logic on ASCII chars/digits)
        shifted_char_ord = apply_shift(char_code)
        result_bytes.append(shifted_char_ord)

    return bytes(result_bytes).encode('utf-8')
def rotate_message(message: str, key=None):
    """Apply ROT-13 encryption using a standard shift."""
    
    def apply_shift(c):
        # Map A-Z -> 0-25, a-z -> 0-25 (standard for this context)
        offset = -(((ord(c) + ord('A') % 26)) & 0xff) if 'a' <= c < z else ((int(c.replace(" ", "")) - int('0')) % 10)

        # Normalize negative offsets to positive range [0, 25]
        offset = (offset + 26) % 26
        
        return chr((ord(c) - ord('A') + offset) & 0xff if 'a' <= c < z else int(c.replace(" ", "")) - int('0'))

    result_bytes = bytearray()
    
    for i, ch in enumerate(message):
        char_code = ord(ch)
        
        # Apply shift to the character itself (ROT-13 logic on ASCII chars/digits)
        shifted_char_ord = apply_shift(char_code)
        result_bytes.append(shifted_char_ord)

    return bytes(result_bytes).encode('utf-8')
