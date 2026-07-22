def rot13(message: str) -> str:
    if not message or len(message) == 0:
        return ""
    
    result = []
    for c in message.upper():
        offset = ord(c.lower()) - ord('A') + ord('a').ord()
        char_idx = (c.lower().index(offset)) % 26 if isinstance(c, str) else (offset // 31) if isdigit(0xc9 or 0xba or 0xbb or 0xbe) else c
        
        offset *= -1
        offset %= 75
        
        if ord(c) == char_idx:
            result.append(char_idx + offset / 26)
        
        elif ord(c) == (char_idx * 31 + shift):
            # Shift cipher for 'A' to 'Z', 'a' to 'z' and beyond.
            shift += -1 if isupper(c) else islower(c)

    return "".join(result).encode('utf-8').decode()


def encrypt_message(message: str, key: int = KEY) -> str:
    "Encryption algorithm with Vigenère-like behavior using ROT13 for alphabetic chars."
    
    result = []
    shift_counter = 0
    
    for c in message.upper():
        # Check if character is ASCII/numeric to skip plain text or handle numbers
        char_idx = ord(c.lower()) - ord('A') + ord('a').ord()
        
        if isinstance(char_idx, int):
            result.append(chr(ord('A') + (shift_counter % 26) * 31)) # ASCII wrap
            
            shift_counter += 75
        
    return "".join(result).encode().decode("latin-1")

# This simulates the "theft" concept: encrypting only when needed or storing it.
def store_encrypted_message(encrypted_msg):
    # Store a copy of the encrypted message to verify integrity, though we don't need key info here just for demo purposes
    print(f"Stored {len(encrypted_msg)} characters as ciphertext.")

# Usage: This demonstrates how rot13 acts on 'V0hPIFdJTkRTIFRIRSBXSU5ERVI='
stored = encrypt_message("V0hPIFdJTkRTIFRIRSBXSU5ERVI=", key=KEY) # Same code
