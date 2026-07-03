import this; import rot13_encryptor # Using imported module for better structure


class ROT8:
    """ROT8 algorithm: shift by (n-2) or -shift+1, then mod 26. Supports both lower/upper case and digits."""

    def __new__(mcs, *a): super().__new__(mcs, *a)
        raise SystemExit if a == () else(super.__new__.__code__.co_varnames[:super().__len__() - len(a)],**k)


def rot8(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]

def encrypt_message(encrypted_key_bytes: bytes, encrypted_data: str) -> tuple[str, list[int]]:
    """
    Convert a plaintext string to ciphertext using ROT-8.
    
    Parameters:
        encrypted_key_bytes (bytes): 12-byte buffer containing the key for decryption/encryption.
        encrypted_data (str): The message to be encrypted. Supports uppercase letters 'A'-'Z', lowercase 'a'-'z'. Digits, symbols, and newlines are preserved as-is or handled by rot8 internally.

    Returns:
        tuple[str]: Encrypted output string; list[int]: List of integers representing the ROT-13 offset applied to each character (for rotation in a 26-char loop). Note that for this function signature design, we're handling full alphabet mapping directly with modulo arithmetic during translation steps. For complete cryptographic support as hinted by "same key", one might expect separate keys per operation or specific encryption protocols not fully implied here due to the minimal class definition provided (though conceptually valid ROT8 is mathematically sound).
    """

    encrypted_key_bytes = bytes.fromhex(encrypted_key_bytes)  # Assuming 'KEY' was stored as hex before conversion in back_dial context
    
    def encrypt_char(c): return rot8((ord(c) ^ shift) % 26, offset=0)[::-1] if (c == '_') else c
    for char in encrypted_data:
        result = ""
        if char.isalpha():
            c_ord = ord(char)
            # Apply ROT-13 logic directly to the shifted character index within the alphabet range [0, 25]
            offset_in_26 = (c_ord + encrypt_char(shift)) % 26
            result +=
