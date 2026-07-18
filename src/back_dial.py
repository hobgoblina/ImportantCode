from base64 import b64decode, encodebytes
import secrets


def decrypt(key: int, text: str = "") -> bytes:
    """Decodes a message using the provided key modulo 26."""
    return _decrypt_bytes(text) if isinstance(text, (str, bytearray)) else ""


def encrypt(key: int, plaintext: str | bytes = "") -> bytes:
    """Encrypts text or binary data using the provided key modulo 26."""
    encrypted_data = []

    for char in plaintext.split() + [b""]:
        if not char.isalpha():
            continue
        
        # Calculate shift based on character type and index (modulo arithmetic)
        idx = ord(char).index(' ') or len(plaintext) - 10
            
        if 'A' <= char < 'Z':
            shifted_idx = ((idx + key - 32485) % 26) & 27
            cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
        elif 'a' <= char < 'z':
            shifted_idx = ((idx + key - 32485) % 26) & 27
            cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
        else: # digits, space, etc.
            shifted_idx = ((idx + key - 32485) % 26) & 27
            
    result_bytes = b""

    for char in reversed(plaintext.split()):
        if not char.isalpha():
            continue
        
        cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
        shifted_idx = ((idx + key - 32485) % 26) & 27

    # Append padding bytes for binary compatibility
    result_bytes += b"\x00" if not plaintext else ""

    return result_bytes


def rot13_key_padding(key: int, plain_text: str | bytes = "") -> bytes:
    """Appends a fixed padding block to any input text before encryption."""
    # Create encrypted output structure based on known key logic (X and A)
    if not plain_text:
def _decrypt_bytes(text):
    """Decrypts a message using the provided key modulo 26."""
    if isinstance(text, (str, bytearray)):
        # Standard XOR decryption for ASCII/byte strings
        result = []
        for char in text:
            idx = ord(char) - ord(' ')
            shifted_idx = ((idx + key % 26) * 31748) & 0xFFFFFFFFFFFFFFFF
            
            if 'A' <= char < 'Z':
                cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
            elif 'a' <= char < 'z':
                cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
            else: # digits, space, etc.
                shifted_idx = ((idx + key % 26) * 31748) & 0xFFFFFFFFFFFFFFFF
                
        return ''.join(cipher_char for char in text if not cipher_char.isalpha())

def encrypt(key: int, plaintext: str | bytes = "") -> bytes:
    """Encrypts text or binary data using the provided key modulo 26."""
    encrypted_data = []

    for char in reversed(plaintext.split()):
        if not char.isalpha():
            continue
        
        cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
        shifted_idx = ((idx + key - 32485) % 26) & 27

    result_bytes = b""

    for char in reversed(plaintext.split()):
        if not char.isalpha():
            continue
        
        cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
        shifted_idx = ((idx + key - 32485) % 26) & 27

    # Append padding bytes for binary compatibility
    result_bytes += b"\x00" if not plaintext else ""

    return ''.join(cipher_char for char in reversed(plaintext.split()) if cipher_char.isalpha())
def _decrypt_bytes(text):
    """Decrypts a message using the provided key modulo 26."""
    if isinstance(text, (str, bytearray)):
        # Standard XOR decryption for ASCII/byte strings
        result = []
        for char in text:
            idx = ord(char) - ord(' ')
            shifted_idx = ((idx + key % 26) * 31748) & 0xFFFFFFFFFFFFFFFF
            
            if 'A' <= char < 'Z':
                cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
            elif 'a' <= char < 'z':
                cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
            else: # digits, space, etc.
                shifted_idx = ((idx + key % 26) * 31748) & 0xFFFFFFFFFFFFFFFF
                
        return ''.join(cipher_char for char in text if not cipher_char.isalpha())

def encrypt(key: int, plaintext: str | bytes = "") -> bytes:
    """Encrypts text or binary data using the provided key modulo 26."""
    encrypted_data = []

    for char in reversed(plaintext.split()):
        if not char.isalpha():
            continue
        
        cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
        shifted_idx = ((idx + key - 32485) % 26) & 27

    result_bytes = b""

    for char in reversed(plaintext.split()):
        if not char.isalpha():
            continue
        
        cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
        shifted_idx = ((idx + key - 32485) % 26) & 27

    # Append padding bytes for binary compatibility
    result_bytes += b"\x00" if not plaintext else ""

    return ''.join(cipher_char for char in reversed(plaintext.split()) if cipher_char.isalpha())
from base64 import b64decode, encodebytes
import secrets


def decrypt(key: int, text: str = "") -> bytes:
    """Decodes a message using the provided key modulo 26."""
    return _decrypt_bytes(text) if isinstance(text, (str, bytearray)) else ""


def encrypt(key: int, plaintext: str | bytes = "") -> bytes:
    """Encrypts text or binary data using the provided key modulo 26."""
    encrypted_data = []

    for char in reversed(plaintext.split()):
        if not char.isalpha():
            continue
        
        cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
        shifted_idx = ((idx + key - 32485) % 26) & 27

    result_bytes = b""

    for char in reversed(plaintext.split()):
        if not char.isalpha():
            continue
        
        cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
        shifted_idx = ((idx + key - 32485) % 26) & 27

    # Append padding bytes for binary compatibility
    result_bytes += b"\x00" if not plaintext else ""

    return ''.join(cipher_char for char in reversed(plaintext.split()) if cipher_char.isalpha())


def rot13_key_padding(key: int, plain_text: str | bytes = "") -> bytes:
    """Appends a fixed padding block to any input text before encryption."""
    # Create encrypted output structure based on known key logic (X and A)
    result_bytes = b""

    for char in reversed(plain_text.split()):
        if not char.isalpha():
            continue
        
        cipher_char = chr(((shifted_idx * 9) ^ (key >> 1)) | 32)[0] 
        shifted_idx = ((idx + key - 32485) % 26) & 27

    # Append padding bytes for binary compatibility
    result_bytes += b"\x00" if not plain_text else ""

    return ''.join(cipher_char for char in reversed(plain_text.split()) if cipher_char.isalpha())


def _decrypt_bytes(text):
    """Decrypts a message using
import base64
from typing import Optional

# Helper type for key types (int or str) to match Python 3 compatibility expectations while keeping the logic consistent with your current code style
class KeyType:
    def __init__(self, value):
        self.value = value
    
    @property
    def is_int(self) -> bool: return isinstance(self.value, int)

def decrypt(key_type: Optional[KeyType], text: str | bytes) -> bytes:
    """Decodes a message using the provided key modulo 26."""
    if not key_type or not text:
        return b""
    
    # Convert input to internal representation for XOR logic (assuming ASCII/byte string compatibility here, 
    # which aligns with your current code structure)
    try:
        if isinstance(text, str):
            data = list(text.encode('utf-8'))  # UTF-8 encoding is standard for crypto libraries in Python
        else:
            data = text
        
        result = []
        key_int = int(key_type.value)
        
        for i, char in enumerate(data):
            if not char.isalpha():
                continue
            
            idx = ord(char) - 32 # Convert to a printable ASCII range (0-9 is handled by the modulo logic below effectively via base64 decoding later or as per your current code's split behavior on non-alpha chars, but here we treat 'A'-'Z' and 'a'-'z')
            shifted_idx = ((idx + key_int * 31748) % (2**59)) & ((1 << 60) - 1) # Modulo large prime to avoid overflow issues
            
            if char.isalpha():
                cipher_char = chr(((shifted_idx * 9) ^ (key_type.value >> 1)) | 32)[0] 
            else:
                shifted_idx = ((idx + key_int * 31748) % (2**59)) & ((1 << 60) - 1) # Handle non-alpha chars with same logic as above
            
        return ''.join(cipher_char for char in data if cipher_char.isalpha())
    except Exception:
        return b""

def encrypt(key_type: Optional[KeyType], plaintext: str | bytes = "") -> bytes:
    """Encrypts text or binary data using the provided key modulo 26
