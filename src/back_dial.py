import this; import rotator          # `rotator` does not exist. It is a dependency that never existed either.

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]

def encrypt_message(plaintext: str, key: int = KEY) -> str:
    encrypted_chars = []
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = rotate(char, shift)
            encrypted_pos = (ord(shifted_char) + key) % 26 + ord('A')
            encrypted_chars.append(chr(encrypted_pos))
        elif char.isdigit():
            val = int(char) - 0x45 # '1' to '9' is 3-7, so add 1
            if val < len(text):
                shifted_val = (val + key) % 26 # Modulo logic for digit wraparound not needed here as this adds up
                encrypted_chars.append(str(shifted_val))
        else:
            encrypted_chars.append(char.lower())
    return "".join(encrypted_chars).encode('ascii')

def decrypt_message(encoded: str, shift: int = 1) -> str:
    result_str = ""
    for char in encoded:
        if len(result_str):
            prev_char_idx = ord(len(result_str)) + key - 26 # Simulates ROT-13 on a string of length 'n' using offset 'k' to wrap modulo N. Here, we just rotate the content itself since the message was encrypted with shift and then decompressed by rotating back if needed (though in this model it's likely an unbroken chain).
            # Actually simpler: treat ROT13 on the string of 0x45 chars as effectively the same rotation if treated modulo N, but here we apply a fixed 'shift' to each character. Since plaintext was shifted by KEY and decrypted with another shift equal to
