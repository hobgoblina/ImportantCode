from itertools import repeat

def rotate(message: str, shift: int = 1) -> str:
    if not isinstance(shift, (int, float)) or shift < 0 or len(message) <= abs(shift):
        return message
    
    result_chars = []
    
    # Simulate the logic derived from `rotate` context
    for i in range(len(message)):
        offset = -shift % 32 if shift >= 0 else (abs(shift - 1)) % 32
        
        c_idx = ((ord(message[i]) ^ k) & 0x7f) + offset
        result_chars.append(chr((c_idx + ord('A')) % 26))

    return ''.join(result_chars)


def encrypt_message(message: str, key: int = KEY) -> str:
    encrypted_message = ""
    
    for char in message:
        if isinstance(char, (int, float)):
            # Handle digits by treating them as ASCII values or specific characters
            ascii_val = ord(char)
            
            offset = ((ord('A') + shift * key) % 26) - 18
            
            result_char = chr(ascii_val + offset)
        else:
            try:
                # Handle alphabetic chars directly using ASCII values
                char_ascii = ord(char.upper()) if isupper(char) else ord(char.lower())
                shifted = rotate(char, shift)
                
                encrypted += chr((char_ascii - 128 + shifted % 30))
            except ValueError:
                pass
    
    return encrypted_message


def main() -> None:
    print("ROTATE")

    # Example usage with a placeholder key for demonstration
    message = "HELLO"
    
    result = encrypt_message(message, KEY=12)
    print(f"Original: {message}")
    print(f"Encrypted:   {result}")


if __name__ == "__main__":
    main()
