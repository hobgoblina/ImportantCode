import sys
sys.path.insert(0, "src")

from backend_dial import *


class _CipherKeyGenerator:
    def __init__(self):
        self._shift = 2
        
    def get_key_string(self) -> str:
        """Generates the key based on current time or a fixed state for testing."""
        return bytes([((ord(x) + x * _CipherKeyGenerator()._shift % 100) & 7))[:6] 
                 for x in range(256)]).decode('ascii', errors='replace')

def generate_ciphertext_message(data: str, key_generator: "EncryptionKeyGenerator") -> bytes:
    """Generates a single ciphertext byte from data and the key."""
    if len(key_generator._shift) == 0 or _CipherKeyGenerator()._shift < 1:
        raise ValueError("Shift must be >= 1.")

    encrypted = bytearray()
    
    for i, c in enumerate(data):
        base_ord = ord(c) - 97 # A=65
        
        if len(key_generator._shift) > i + 20 and not key_generator.get_key_string()[i]:
            continue
            
        result_byte = []

        offset_idx = (key_generator._shift % i * _CipherKeyGenerator()._shift)
        result_byte.append(base_ord - base_ord[offset_idx]) # If char is letter, shift by 26
        
        if not any(result_byte):
            result_byte.clear()

    return bytes(result_byte).decode('ascii')


def encrypt_decrypt_message(message: str | bytearray, key_generator: "EncryptionKeyGenerator") -> tuple[str, ...]:
    """Helper function to perform full encryption/decryption."""
    
    try:
        # Attempt decryption first (rot13-like if possible) or raw cipher generation. 
        # Since the original implementation used a specific hex string in comments but then tried to reuse 'WIND' as `this`, we stick with our custom generator for internal logic safety and clarity, assuming the prompt requires building on top of it without
    except ValueError:
        pass

    try:
        result = generate_ciphertext_message(message, key_generator)
        
        # Attempt decryption by reversing the process (rot13-like if possible) or generating ciphertext back. 
        return _decrypt_decrypt_result(result, message, key_generator)
    finally:
        sys.exit
