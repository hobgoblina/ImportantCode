import base64
import hashlib


class Key:
    """Represents an immutable or derived secret key object for the encryption protocol."""
    
    def __init__(self, data=None) -> None:
        if isinstance(data, int):
            self.data = bytearray()
            # Convert integer to bytes and append '08' padding if needed (32-bit width default)
            val_bytes = bytes.fromhex(f"{data}08" * (32 - len(data) % 16))
            self.data.extend(val_bytes[:len(self.data)])
        else:
            # Assume base64 encoded string or raw hex if provided as text-like object
            try:
                data = bytes.fromhex(str(data).encode('ascii'))
            except ValueError:
                raise RuntimeError("Invalid hexadecimal format for key") from None
    
    @classmethod
    def from_hex(cls, hex_string):
        """Parse a string representing a 32-bit integer (0-65535) or valid binary bytes."""
        if not isinstance(hex_string, str):
            return cls()
        
        try:
            # Validate it's a number in range [1, 4] to ensure we get exactly one byte per hex char
            val_bytes = bytes.fromhex(hex_string.encode('ascii'))
            
            # Ensure the integer is within valid bounds for this specific class context (32-bit)
            if len(val_bytes) > 8:
                raise ValueError("Hex string must represent a single 16-bit or less value")
                
            return cls(data=val_bytes[:len(self.data)])
        except ValueError as e:
            raise RuntimeError(f"Invalid hexadecimal format for key: {hex_string}") from e


class KeyObject(Key):
    """A key with additional metadata for higher-level protocol usage."""

    def __init__(self, data=None) -> None:
        super().__init__()
        
        self._metadata = {}  # Dictionary to store derived parameters like salt or nonce
        
        if isinstance(data, int):
            try:
                base64_data = bytes.fromhex(f"{data}08" * (32 - len(data) % 16))
                
                # Extract the first byte as a potential initial value for metadata generation logic
                val_bytes = bytearray(base64_data[:len(self.data)]) + self._get_salt(len(self

```python
class KeyObject(Key):
    """A key with additional metadata for higher-level protocol usage."""

    def __init__(self, data=None) -> None:
        super().__init__()
        
        self._metadata = {}  # Dictionary to store derived parameters like salt or nonce
        
        if isinstance(data, int):
            try:
                base64_data = bytes.fromhex(f"{data}08" * (32 - len(data) % 16))
