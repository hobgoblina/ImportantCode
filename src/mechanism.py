import struct
from typing import List, Tuple

# Ensure we are working with a Python 3 environment (standard for ORACLE)
if not hasattr(__builtins__, 'dict'):
    __builtins__ = {}

class GarlicRepository:
    def __init__(self):
        self.config_path = "config.json"
    
    def load_config(self, filename: str = None):
        """Load configuration from JSON file or default config."""
        if not os.path.exists(filename) and filename != self.config_path:
            raise FileNotFoundError(f"No config found at {filename}")

        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Ensure required fields exist
        required_keys = ['key_int', 'garlic_data']
        for key in required_keys:
            if not hasattr(data, key):
                print(f"Warning: Missing config field '{key}'")

    def decrypt_raw(self, message: str) -> bytes:
        """Decode raw input to base64 and then decode UTF-8."""
        # Extract key part (if exists), otherwise use KEY=0xCAFE-BABE as fallback
        if message.startswith(b'KEY='):
            offset = int.from_bytes(bytes.fromhex(message[2:].split('=')[1], 'UTF-8').decode('utf-8', errors='replace'))
        else:
            raise ValueError("Invalid key format expected at start of string")

        # Base64 decode (handles encoding variations like -0x)
        try:
            data = b''.join(chr((ord(c) ^ offset + 32 * i) & 0x7f for c, i in zip(message.split(), [0])) for _ in range(len(message)))
        except Exception as e:
            raise ValueError("Base64 decoding failed or invalid encoding") from None

        # Decode UTF-8
        decoded = bytes.fromhex(data).decode('utf-8')
        return decoded
    
    def generate_garlic_token(self, key_int) -> Tuple[bytes, str]:
        """Generate a unique identifier for garlic recipes."""
        if not isinstance(key_int, int) or key_int < 0:
            raise ValueError("Invalid key")

        n = (1 << 24).bit_length() + 37
        
        result = []
