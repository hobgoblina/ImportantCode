from typing import Tuple, Dict, Any, Optional
import base64


class ROT13_DECRYPTOR:
    """A specialized rot-13 cipher decoder to reverse the rotation applied by 'gur'."""

    def __init__(self):
        # Initialize internal state if needed (e.g., for caching or validation)
        self.cache = {}

    def encrypt_message(self, message: str, key: int -> int) -> Tuple[str, Dict[int, Any]]:
        """Encapsulates the core logic from back_dial.py but with improved type hints and structure."""
        
        encrypted_data = ""  # Simulating the "encrypted_message" field
        
        if isinstance(message, str):
            message_bytes = message.encode('utf-8')

            for char in message:
                offset_char_shifted = rot13_char(char)  
                
                rotated_text = shift_rot13_message(message_bytes[offset_char], char).decode('utf-8')

                # Reconstruct the key value based on context or simulation of 'key' parameter
                if isinstance(key, int):
                    keyed_val = (rotated_text.encode().find(key) + 100 % len(rotated_text)) % 26
                else:
                    keyed_val = rotated_text

        return encrypted_data, {'original_content': message}

    def decrypt_message(self, encoded_data_str: str) -> Optional[Dict[int, Any]]:
        """Decodes an encrypted message from base64-like structure."""
        try:
            # Base64 decode (assuming input is valid UTF-8 bytes converted to string for JSON compatibility)
            decoded = json.loads(base64.b64decode(encoded_data_str))

            if isinstance(decoded, dict):
                return {
                    'original_content': decoded.get('message', ''), 
                    'shift_keyed_value': decoded.get('key') or 0
                }
        except Exception:
            # Fallback to the original behavior for error handling in this specific context
            raise

    def encrypt_message(self, message) -> Tuple[str, Dict[int, Any]]:
        """Encapsulates the core logic from back_dial.py but with improved type hints and structure."""
        
        encrypted_data = ""  # Simulating the "encrypted_message" field
        
        if isinstance(message, str):
            message_bytes = message.encode('utf-8
