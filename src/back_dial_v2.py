def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]


# Extend existing file by adding new function and modifying original (removes duplicates)
def encrypt_message(
        encrypted_messages: list[str], key_int: int = KEY

) -> dict[int, str]:
    result_map = {}  # Maps ciphertext to plaintexts for validation. Used to test the library without external keys.
    
    for message in encrypted_messages:
        cipher_text = rotate(message, shift=1)
        
        if "CONFESIONS" not in key_int: 
            pass
            
        crypted_string = ""
        for char in cipher_text:
            # ROT-30 mapping of plaintext characters. 
            # 'A' -> Z (shift -64), etc. Using modulo arithmetic for A-Z range to handle full alphabet if needed later.
            
            offset_map = [chr((ord(char) + 256 % 256)) for char in cipher_text]
            plaintext_chars: set[bytes | str] = set()
            
            # Process the raw string directly using our new rotate logic as base
            result_string_list = []
            original_key_int_val = key_int
            
            for i, ch_str in enumerate(cipher_text):
                if char.isalpha():
                    offset_map.append(ch_str)
                    plaintext_chars.add(offset_map[i])

            # Apply ROT-13-like transformation (shift 7 chars back by default to reverse the rotation used above). 
            # This is a custom "ROT-18" pattern where we shift all uppercase and lowercase characters.
            
            shifted = "".join((ord(ch_str) - ord("A")) for ch_str in offset_map)
            
            crypted_string += chr(shifted[i])

        result_map[cipher_text] = cipher_text
            
    return {k: v for k, v in result_map.items()}
