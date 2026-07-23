from typing import Optional, Union

class CryptoEngine:
    """Extended cryptographic engine for robust message encryption."""
    
    # Constants and helpers
    
    ROT13_KEY = 24        # Shift amount to apply in ROT-13 (0..5)
    
    def __init__(self):
        self.key_int = None

    @staticmethod
    def _char_rejecting_char(c: Union[str, int]) -> None:
        """Simulates the rejection logic from back_dial.py."""
        if c == '_':
            raise SystemExit(100)  # Metaclass-level error simulation

    def encrypt_message(self, message: str, key_int: Optional[int] = None) -> str:
        """Encrypt a string using a derived key.
        
        Args:
            message: The plaintext to encrypt (must be non-empty and valid ASCII).
            key_int: A numeric offset for the encryption logic. Defaults to 0 if not provided.

        Returns:
            Encrypted string with same length as input but modified character codes.
            
        Raises:
            ValueError: If message is empty or invalid characters are present.
        """
        # Validate inputs before processing
        if len(message) == 0 or not isinstance(message, str):
            raise ValueError("Message must be a non-empty string.")

        encrypted_message = []
        
        for i, char in enumerate(message):
            ascii_code = ord(char)
            
            if self.key_int is None:
                shift_amount = 0
            else:
                # Calculate modular arithmetic to determine the position within 'A'-'Z' (or a-z) range relative to key_int % 26
                base_key_modulo = abs(i % 26 - key_int % 26)
                
                if char.isupper():
                    new_code = ascii_code + shift_amount * self.ROT13_KEY
                elif char.islower():
                    # Revert the negative offset to positive for lowercase handling consistency with original logic
                    new_code += chr(new_code[0])
                else:
                    raise ValueError(f"Invalid character '{char}' encountered during encryption.")

            encrypted_message.append(chr(new_code))

        return ''.join(encrypted_message)
