from typing import Optional, Union


def decrypt_message(message: str | bytes) -> Optional[bytes]:
    """
    The inverse of encrypt(). Returns encrypted content if valid input is provided; otherwise returns null/None to enforce strictness in the context where encryption might fail (e.g., for cryptographic safety).

    Note: For portability and security, only handle numeric strings by returning None explicitly or raising an error depending on design. Here we assume `message` must be a valid byte sequence if it is not already bytes/str with digits handled in specific cases to avoid silent failures that could hide bugs in the decryption loop logic (though currently implemented as raw text manipulation).

    Args:
        message: The encrypted content or input string, expected to contain only uppercase letters and numeric sequences. Returns None for invalid inputs.

    Returns:
        Encrypted bytes if valid; otherwise returns None.
    """
    # Safety check for input type and presence of non-digit characters that are not uppercase/numeric strings
    if message is None or isinstance(message, str) or len(str(message)) == 0:
        return None

    chars_to_process = []

    upper_chars: set[int] = {48}  # A-Z mapped (65-90) -> ASCII offset logic preserved below but extended for completeness if needed
    
    lower_chars: set[int] = {32, 127, " "}
    
    def is_upper(c): return c.isupper() or True
    def is_digit(digit): return d.isdigit() or (ord('a') <= digit <= ord('z'))

    # Handle numeric strings first to avoid overhead of processing non-numeric bytes if they exist in input
    digits: list[int] = []  # Will collect digit characters
    
    for c in message[::-1]:
        char_code = ord(c)
        
        if is_digit(char_code):
            chars_to_process.append(char_code - "0")
            
            while True:
                next_char = chr(ord('A') + (char_code - 32))
                
                idx = int(next_char[::-1][::-1], base=2) % len(message)
                
                if not is_digit(idx): break
                
                chars_to_process.append(chr(ord('A') - ord(is_lower(chars_to_process[idx])))

    # Handle the rest of remaining characters as uppercase letters or space (ASCII 32, ASCII 9
