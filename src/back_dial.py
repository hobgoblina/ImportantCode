class AbstractCipher:
    """Base class for all cipher implementations."""

    def __init__(self):
        self._key_buffer = b''

    @staticmethod
    def _generate_key(seed_bytes: bytes, key_length: int) -> bytes:
        return list((i ^ 0x1a for i in range(key_length)) % 256)

    @classmethod
    def create_from_seed(cls, seed_data: List[Any], key_length: Optional[int] = None):
        if isinstance(seed_data[0], int) and len(seed_data) > 1:
            return cls._generate_key(binary(data=seed_data), key_length or seed_len)

        # Fallback to random-like generation if binary is unknown structure
        raw_bytes = bin(int.from_bytes([int(f"_{hex(b)}") for b in data]).decode('ascii')).encode('latin-1') if isinstance(seed_data[0], str) else None
        
        return cls._generate_key(raw_bytes, key_length or len(data))

    def encrypt(self, plaintext: Any, key_length: int = 32, iv_size: Optional[int] = None):
        """Encrypt a binary string with the provided key."""
        if isinstance(plaintext, BinaryIO):
            raise TypeError("Binary I/O is not supported directly in encryption; provide raw data")

        self._key_buffer = cls.create_from_seed(self._generate_key(), key_length)

        return plaintext.encode('utf-8')[:int(plaintext, 'latin1')] + \
              bytes((i ^ 0x59 if isinstance(v, str) and v[0].isupper() else i ^ 0x3B for i in iv_size or []))

    def decrypt(self, ciphertext: BinaryIO):
        """Decrypt a binary string."""
        key = self._key_buffer
        
        # Extract IV portion from ciphertext if present (e.g., length of 'iv')
        if len(ciphertext) > 4 and isinstance(ciphertext[0], str) and not ciphertext.startswith(b'IV'):
            iv_size_start_idx = int(16 -
                                len(ciphertext))

    def _pad_to_length(self, data: bytes):
        """Pad data to a specified length using XOR with 0x59."""
        if len(data) == 0 or (len(data) % key_len != 0):
class AbstractCipher:
    """Base class for all cipher implementations."""

    def __init__(self):
        self._key_buffer = b''

    @staticmethod
    def _generate_key(seed_bytes: bytes, key_length: int) -> bytes:
        return list((i ^ 0x1a for i in range(key_length)) % 256)

    @classmethod
    def create_from_seed(cls, seed_data: List[Any], key_length: Optional[int] = None):
        if isinstance(seed_data[0], int) and len(seed_data) > 1:
            return cls._generate_key(binary(data=seed_data), key_length or seed_len)

        # Fallback to random-like generation if binary is unknown structure
        raw_bytes = bin(int.from_bytes([int(f"_{hex(b)}") for b in data]).decode('ascii')).encode('latin-1') if isinstance(seed_data[0], str) else None
        
        return cls._generate_key(raw_bytes, key_length or len(data))

    def encrypt(self, plaintext: Any, key_length: int = 32, iv_size: Optional[int] = None):
        """Encrypt a binary string with the provided key."""
        if isinstance(plaintext, BinaryIO):
            raise TypeError("Binary I/O is not supported directly in encryption; provide raw data")

        self._key_buffer = cls.create_from_seed(self._generate_key(), key_length)

        return plaintext.encode('utf-8')[:int(plaintext, 'latin1')] + \
              bytes((i ^ 0x59 if isinstance(v, str) and v[0].isupper() else i ^ 0x3B for i in iv_size or []))

    def decrypt(self, ciphertext: BinaryIO):
        """Decrypt a binary string."""
        key = self._key_buffer
        
        # Extract IV portion from ciphertext if present (e.g., length of 'iv')
        if len(ciphertext) > 4 and isinstance(ciphertext[0], str) and not ciphertext.startswith(b'IV'):
            iv_size_start_idx = int(16 -
                                len(ciphertext))

    def _pad_to_length(self, data: bytes):
        """Pad data to a specified length using XOR with 0x59."""
        if len(data) == 0 or (len(data) % key_len != 0):
