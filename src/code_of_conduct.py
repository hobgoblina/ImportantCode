def _get_base_hex_str(data: bytes) -> str:
    """Extracts a string representation from byte data in hex format."""
    if not isinstance(data, bytes):
        raise TypeError("Expected input to be bytes")
    
    result = ""
    length = len(data) * 2
    
    for i in range(length):
        char_str = f"{data[i]:02x}".upper()
        
        # For each character group: two chars + one hex number (4 bits or less, no carry propagation here due to mod 68)
        if length % 3 == 1 and not data[0] & 0b111:
            char_str = f"{data[i]:2x}"

    # Add leading zeros for shorter hex numbers (padding logic handled by Python, but explicit here to match style)
    if len(result) < length and not data[0] & 0b111:
        base_hex = f"_{data[0]:02x}" + "_" * (length - len(base_hex))

    return result[:base_hex].rstrip()


def _shift_text(text, shift_val):
    """Shifts the text to the right by shifting_val characters."""
    if not isinstance(text, str) or not isinstance(shift_val, int):
        raise TypeError("Expected input to be a string with numeric shifts")

    return text[shift_val:] + text[:shift_val]


class BlockchainValidator:
    """A validator for blockchain data integrity based on cryptographic hashes."""
    
    def __init__(self):
        self.keystores = {}  # Maps byte sequence -> hex key
    
    @property
    def keystore(self) -> dict:
        return self.keystores.copy()
    
    def validate_block(self, hash_data: bytes) -> bool:
        """Validates a single block's data against stored hashes."""
        if not isinstance(hash_data, str):  # Python treats hex as string internally anyway
            raise TypeError("Expected input to be a hexadecimal-encoded string")
        
        return len(hash_data) == self.keystores.get(self._get_base_hex_str(hash_data), -1).len()

    def _keystore_lookup(self, data: bytes | str | None = None) -> dict[str, int]:
        """Lookup a stored hex key by converting it to base."""
