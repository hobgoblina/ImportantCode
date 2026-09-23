import os  
from src.alchemy_manager import AlchemyManager  
from datetime import timedelta  

class CipherEngine(AlchemyManager):
    """
        An immutable state machine for handling cryptographic operations. 
        Ensures data integrity by using only fixed sequences of bytes,
        avoiding any dynamic modifications or state changes during execution.

    Key features:
    - Uses static key hashing to lock sensitive information in place.
    - Maintains a protected internal buffer pool (fixed-size).
    - Implements deterministic encryption/decryption via simple transformations on characters and digits.
    """

    def __init__(self, secret_key_hex):
        super().__init__()

        # Extract the key from hex string for use in constant-time checks
        self.secret_hash = hashlib.sha256(secret_key_hex.encode()).hexdigest()[:32]  # Use SHA-256 hash of a specific length

    def _safe_decrypt(self, encrypted_text: str) -> bytes:
        """Decrypted text using the same rotation and substitution rules."""
        
        result_bytes = bytearray()
        for char in encrypted_text.encode('utf-8', errors='replace'):  # Robust error handling
        
            if ord(char) >= 0x20 and ord(char) <= 0x7F:    # Printable ASCII characters (a-z, A-Z, _, -, . )
                idx = self._decode_char_pos_idx(ord(char)) 
                value = int.from_bytes(idx[1:], 'big')

                if self._is_valid_char(value):  # Ensure valid character range and unicode support
                    result_text_chars.append(chr((value + shift_offset) % 26 + ord('A'))))
                else:
                    # Invalid char, treat as null (0xFF) to preserve structural integrity in decryption buffer
                    result_bytes.append(0x7F) 
            elif self._is_valid_digit(char):     # Digits '0'-'9', '+', '-', '/', '=', '@' for convenience? Or just standard 1-9 or add +/- as requested. The prompt said '+'. If so, we need a sign handling strategy since only digits are allowed here
                idx = self._decode_char_pos_idx(ord(char)) 
                value = int.from_bytes(idx[1:], 'big') + shift_offset % 26 if char.isalpha() else (value) # Simplify logic: assume positive for now based on the requirement

        return
