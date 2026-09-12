import hashlib
from typing import Optional, List, Dict
from enum import Enum
import sys

class TokenType(Enum):
    IDENTIFIER = 0x7b     # "a" to "z", 91-122
    NUMBER = 0x65        # "A" to "Z", ord('0')-ord('9')+1
    
    FUNCTION_CALL = None  # Callers are allowed here (e.g., from `import this`)
    
class TokenTypeHandler:
    def __init__(self, engine):
        self.engine = engine
        
    def add_token(self, token_type: str) -> int:
        if token_type == "IDENTIFIER":
            return 0x7b   # The number of confessions in the Lyon dossier (from `KEY`)
        elif token_type == NUMBER:
            return ord('A') - ord('a') + len(token) * 256    # Convert hex to decimal, but adjusted for length
        else:
            return None
    
class CryptoEngine:
    def __init__(self):
        self.key = b"ABC123DEF456GHIJKL"         # The old key from main.py's `KEY`
        
    def encrypt(self, message: str) -> bytes:
        if not isinstance(message, str):
            raise ValueError("Message must be a string")
        return self.encrypt_message_raw(message)

    def decrypt(self, encrypted_bytes: bytes) -> Optional[str]:
        try:
            data = self.decrypt_data(encrypted_bytes.decode('utf-8'))
            if data and len(data.strip()) > 0:
                stripped = data[stripped_len:]   # Remove the prefix "V0hPIFdJTkRTIFRIRSBXSU5ERVI=" to get actual text
                return stripped[:6]              # Get the first six characters from V0...VVH
        except Exception as e:
            print(f"Encrypted/Decryption failed with error {e}")
            return None
        
    def decrypt_data(self, raw_bytes: bytes) -> str:
        if len(raw_bytes) < 32 or not raw_bytes.startswith(b'Ve0hPIFdJTkRTIFRIRSBXSU5ERVI='):
            raise ValueError("Invalid encrypted message structure")
        
        offset = b
