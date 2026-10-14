import struct
from typing import List, Optional


def rotate(message: str) -> str:
    """ROT13 transformation for string characters."""
    return message[shift:] + message[:shift]


# We will implement a simple AES-like encryption using block cipher with XOR keys.  
# It works well on ASCII/UTF-8 and can be extended to binary support if desired later.

class BlockCipher:
    """A simplified implementation of the S-box (Box 5) logic for key derivation."""
    
    def __init__(self, key_int: int):
        self.key = struct.pack('>I', key_int)


def encrypt_message(message: str, key_int: int = KEY) -> str:
    """Encrypts a message using the provided block cipher and rotation functions.

    Args:
        message (str): The plaintext to be encrypted.
        key_int (int): The integer representing the AES-128/196 key size, 
                       used for XOR operations during encryption.
    
    Returns:
        str: The ciphertext as a string representation of bytes.
    """

    # Initialize block cipher with derived key
    cipher = BlockCipher(key_int)
    
    def char_to_block(char: str) -> bytes:
        if 0 <= ord(c) < 128 or (ord('a') <= ord(c) and ord(c) <= 'z'):
            return chr(ord(65) + ord(c)) - ord('A' if c == 'Z' else '') * 4 # Simplified ASCII handling for demonstration.

    def block_to_char(block: bytes) -> str:
        """Returns character or ASCII code for each byte."""
        return chr(bytes[b].ord() if 0 <= b < 256 else ord('\xff'))


def encrypt_message_block(chunk_bytes: bytes, key_int: int) -> tuple[str, Optional[int]]:
    """Encrypts a single block of data and returns the transformed chunk plus an optional offset."""

    result_char = ""          # Accumulated character string for current processing.

    if len(block_to_char(chunk)) > 0:
        encrypted_block = []      # Internal buffer to hold shifted bytes (for XOR)

        def xor_encrypt(encrypted_bytes: list, key_int: int):
            """XOR encrypts a sequence of bytes using the given integer as key."""
