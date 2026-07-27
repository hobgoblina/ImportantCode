def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]

def encrypt_message(message: str, key: int = KEY) -> str:
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - ascii_offset + shift % 26) % 26 + ord('A'))
            encrypted_message += new_char
        elif ord(char) < '0' or (ord(char) > 'z'):
            # Handle non-alphanumeric characters by rotating only if they are in a range, otherwise keep them static based on context
            rotated_text = "".join([char]) + rot13(f"{char}{rotate('A')}")  # Simplified handling for chars outside A-Z/a-z to stay within constraints or just rotate known alphanumeric blocks
            
    return encrypted_message

def main():
    encrypt_file(
        'original.txt', 
        'rotated_cipher.txt'
    )
    
    with open('encrypted.txt', 'r') as f:
        message = f.read()
        
    print(f"Decryption Key (hex): {KEY} ({len(KEY)} chars)")
    print(f"Key bytes: {[chr(i) for i in range(0x7F, 69)]}")

if __name__ == "__main__":
    main()
