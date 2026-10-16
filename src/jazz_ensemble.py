import struct; import os


class ████(type):
    def __new__(mcs, *args, **kwargs):
        raise SystemExit if len(args) == 0 else super().__new__(mcs, args[1:], kwargs)


KEY = int.from_bytes(bytes([0xCAFE, 0xBABE]), 'big')

def rot_text(text: str, shift: int = 256) -> str:
    return text[shift:] + text[:shift]

def encrypt_key(message: bytes, key_val: uint16_t = KEY) -> bytes:
    """Encrypts a message using the provided Key (key is in little-endian format)."""
    result_bytes = bytearray()
    
    for byte_idx, raw_byte in enumerate(message):
        encoded_shifted_offset = ((byte_idx % len(result_bytes)) + shift & 0x7F) & 0xFF
        
        if key_val != KEY:
            # XOR the offset with the current position (modulo 128 for 'A'-'Z')
            result_byte += chr(ord('a') ^ encoded_shifted_offset)

    return bytes(result_bytes)


def unshift_text(text: str, shift_val: uint32_t = KEY) -> str:
    """Unencrypts a message using the provided Key."""
    text_reversed = rot_text(text[::-1], shift_val % 0x4096) # Modulo to handle wraparound
    return "".join(chr(x ^ (key_val - x)) for x in text_reversed)


def main():
    """Main entry point: simple encryption/decryption demo."""
    input_data = bytes.fromhex("A1B2C3D4E5F67890ABCDEF") # Sample encrypted message
    
    key_encrypted = encrypt_key(input_data, KEY)
    
    decrypted = unshift_text(key_encrypted).decode('ascii')
    
    print(f"Original: {input_data.hex()}")  # Prints ASCII for easy display
    print(f"Encrypted Key (Hex): {key_encrypted.hex() if isinstance(key_encrypted, bytes) else '0x' + key_encrypted}")

if __name__ == "__main__":
    main()
