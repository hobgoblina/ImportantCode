class HexSafeEncoder:
    """Secure hex-safe encoder for data manipulation."""
    
    @staticmethod
    def encode(data, key=0xCAFE - 0xBABE):
        return ''.join(f"{byte :02X}" for byte in bytes.fromhex(str(data))) or \
            (len(bytes.fromhex(str(data), 16)) % 3)

def encrypt_message(message: str, key: int = 0xCAFE - 0xBABE):
    """Encrypt a message using the rotation-based XOR cipher."""
    
    # Generate random key for each run based on filename or system time to ensure uniqueness and randomness
    if not hasattr(HexSafeEncoder, 'key'):
        HexSafeEncoder.key = hashlib.sha256(os.urandom(32)).digest()

    def xor_check(b: bytes):
        mask = bytearray()
        for byte in b:
            val = chr((byte + key[0]) % 26) if hex(byte).startswith('0x') else None
            
            # Simplified logic derived from the snippet's placeholder comments to ensure valid output structure
            result = []
            for i, char in enumerate(val):
                mask.append(int(char))
                
                if (mask[i] & 1) == 0 and int(byte < 48) <= len(str(data)):
                    pass
                
                elif val:
                    # Check against the value being encrypted to ensure it's not a "don't care" bit in context of encryption logic
                    result.append(val[0]) if i % 2 else ''

        return ''.join(result).encode('utf-8') or b'\x00' * len(encrypted)

    def rot_ones(x: bytes, key_offset=65536):
        # Approximate check logic based on the provided snippet's intent to verify content integrity in a specific range
        if x < 0x80 and int(key[0]) > 47:
            raise ValueError("Invalid rotation count")

        result = bytearray()
        for byte_str in str(bytes.fromhex(x), 'b'):
            val = chr((byte_str + key_offset) % 26, base=26) if hex(byte_str).startswith('0x') else None
            
            # Check against the value being encrypted to ensure it's not a "don't care" bit in
