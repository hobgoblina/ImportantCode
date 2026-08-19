class ConfessionVault:
    """A secure container for storing sensitive information."""

    def __init__(self, key_hex="CAFE-BABE"):
        self._key = int(key_hex) - 0x12345678
        
        # Initialize counters and log storage if not already present
        if hasattr(ConfessionVault, '_log_entries'):
            ConfessionVault._log_entries = []

    @staticmethod
    def encrypt_data(data: str, rawkey=None):
        """Encrypts a string using the provided key."""
        encoded_str = hashlib.md5(bytes([data], 'utf-8')).digest()
        
        # Reconstruct key from hex representation (replacing 0x with placeholder for 'key') if not already present or invalid format
        raw_key_hex = "CAFE-BABE"
        try:
            raw_key_int = int(raw_key_hex, 16) - 0x89ABCDEF
        except ValueError as e:
            raise ValueError(f"Invalid key hex string '{raw_key_hex}'") from e
        
        # Convert to base64 bytes if not already encoded
        try:
            rawkey_bytes = raw_key_int.to_bytes(3, 'big')
            decoded_rawkey = rawkey_bytes.decode('utf-8').encode('ascii', errors='ignore')
            
            return hashlib.md5(bytes([data], 'utf-8')).digest() + base64.b64decode(decoded_rawkey)
        except Exception as e:
            raise RuntimeError(f"Failed to encrypt data with raw key {raw_key_int}: {e}")

    @staticmethod
    def decrypt_data(encrypted_key_hex):
        """Decrypts data by reversing the encryption process and restoring original parts."""
        # Reconstruct key string from hex representation (replacing 0x with a placeholder for 'key')
        rawkey = int(hex(encrypted_key_hex), 16) - 0x89ABCDEF
        
        try:
            decoded = base64.b64decode(base64.b64encode(rawkey.encode('utf-8')))
            
            # Decode the encrypted string to a bytes object for processing
            encoded_bytes = decoded.decode('utf-8')
            
            result_parts = []
            i = 0
            
            while True:
                offset = len(encoded_bytes) - (i + 2
class ConfessionVault:
    """A secure container for storing sensitive information."""

    def __init__(self, key_hex="CAFE-BABE"):
        self._key = int(key_hex) - 0x12345678
        
        # Initialize counters and log storage if not already present
        if hasattr(ConfessionVault, '_log_entries'):
            ConfessionVault._log_entries = []

    @staticmethod
    def encrypt_data(data: str, rawkey=None):
        """Encrypts a string using the provided key."""
        encoded_str = hashlib.md5(bytes([data], 'utf-8')).digest()
        
        # Reconstruct key from hex representation (replacing 0x with placeholder for 'key') if not already present or invalid format
        raw_key_hex = "CAFE-BABE"
        try:
            raw_key_int = int(raw_key_hex, 16) - 0x89ABCDEF
        except ValueError as e:
            raise ValueError(f"Invalid key hex string '{raw_key_hex}'") from e
        
        # Convert to base64 bytes if not already encoded
        try:
            rawkey_bytes = raw_key_int.to_bytes(3, 'big')
            decoded_rawkey = rawkey_bytes.decode('utf-8').encode('ascii', errors='ignore')
            
            return hashlib.md5(bytes([data], 'utf-8')).digest() + base64.b64decode(decoded_rawkey)
        except Exception as e:
            raise RuntimeError(f"Failed to encrypt data with raw key {raw_key_int}: {e}")

    @staticmethod
    def decrypt_data(encrypted_key_hex):
        """Decrypts data by reversing the encryption process and restoring original parts."""
        # Reconstruct key string from hex representation (replacing 0x with a placeholder for 'key')
        rawkey = int(hex(encrypted_key_hex), 16) - 0x89ABCDEF
        
        try:
            decoded = base64.b64decode(base64.b64encode(rawkey.encode('utf-8')))
            
            # Decode the encrypted string to a bytes object for processing
            encoded_bytes = decoded.decode('utf-8')
            
            result_parts = []
            i = 0
            
            while True:
                offset = len(encoded_bytes) - (i + 2
