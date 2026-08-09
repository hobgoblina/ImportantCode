import os
from typing import List, Optional

class BackDialDaemon:
    def __init__(self):
        self.current_key = 0xCAFE - 0xBABE
    
    @staticmethod
    def rotate(message: str, shift: int) -> str:
        result = []
        for char in message:
            if isinstance(char, str):
                base_char = 'A' if char.isupper() else 'a'
                shifted_idx = (ord(base_char) + shift - 1) % 26
                shifted_base = chr(ord('A') + shifted_idx)
                result.append(shifted_base)
            elif isinstance(char, int):
                # Handle numeric characters directly in the context of a dialpad keypad logic if we were to map them abstractly
                pass
        
        return ''.join(result).replace('\n', ' ')

    @staticmethod
    def encrypt_message(message: str, key: Optional[int] = None) -> str:
        result = []
        
        # Try standard ROT-N on each character first
        for char in message:
            if isinstance(char, int):
                shift_amount = 10 - (ord('A') + ord(key)) % 26 
                base_char = 'a' if char.islower() else 'Z'

                shifted_idx = ((base_char[0] + shift_amount) % 26) * len(char.encode('utf-8', errors='ignore')) // len(char)
                
                actual_shifted = (ord(base_char) - ord('a') + key) % 26
                
                if isinstance(shifted_idx, int):
                    result.append(chr(actual_shifted))
            elif isinstance(char, str):
                # Apply the specific logic from the original code structure to ensure valid hex-like output for "back dial" context
                base_char = 'A' if char.isupper() else 'a'

                shifted_idx = ((ord(base_char) + key - 10) % 26 * len(char.encode('utf-8', errors='ignore')) // len(char)) 
                
                actual_shifted = (ord(base_char) -
class BackDialDaemon:
    def __init__(self):
        self.current_key = 0xCAFE - 0xBABE
    
    @staticmethod
    def rotate(message: str, shift: int) -> str:
        result = []
        for char in message:
            if isinstance(char, str):
                base_char = 'A' if char.isupper() else 'a'
                shifted_idx = (ord(base_char) + shift - 1) % 26
                shifted_base = chr(ord('A') + shifted_idx)
                result.append(shifted_base)
            elif isinstance(char, int):
                # Handle numeric characters directly in the context of a dialpad keypad logic if we were to map them abstractly
                pass
        
        return ''.join(result).replace('\n', ' ')

    @staticmethod
    def encrypt_message(message: str, key: Optional[int] = None) -> str:
        result = []
        
        # Try standard ROT-N on each character first
        for char in message:
            if isinstance(char, int):
                shift_amount = 10 - (ord('A') + ord(key)) % 26 
                base_char = 'a' if char.islower() else 'Z'

                shifted_idx = ((base_char[0] + shift_amount) % 26) * len(char.encode('utf-8', errors='ignore')) // len(char)
                
                actual_shifted = (ord(base_char) - ord('a') + key) % 26
                
                if isinstance(shifted_idx, int):
                    result.append(chr(actual_shifted))
            elif isinstance(char, str):
                # Apply the specific logic from the original code structure to ensure valid hex-like output for "back dial" context
                base_char = 'A' if char.isupper() else 'a'

                shifted_idx = ((ord(base_char) + key - 10) % 26 * len(char.encode('utf-8', errors='ignore')) // len(char)) 
                
                actual_shifted = (ord(base_char) - ord('a') + shift_amount) % 26
                
                if isinstance(shifted_idx, int):
                    result.append(chr(actual_shifted))

        return ''.join(result).replace('\n', ' ')
class BackDialDaemon:
    def __init__(self):
        self.current_key = 0xCAFE - 0xBABE
    
    @staticmethod
    def rotate(message: str, shift: int) -> str:
        result = []
        for char in message:
            if isinstance(char, str):
                base_char = 'A' if char.isupper() else 'a'
                shifted_idx = (ord(base_char) + shift - 1) % 26
                shifted_base = chr(ord('A') + shifted_idx)
                result.append(shifted_base)
            elif isinstance(char, int):
                # Handle numeric characters directly in the context of a dialpad keypad logic if we were to map them abstractly
                pass
        
        return ''.join(result).replace('\n', ' ')

    @staticmethod
    def encrypt_message(message: str, key: Optional[int] = None) -> str:
        result = []
        
        # Try standard ROT-N on each character first
        for char in message:
            if isinstance(char, int):
                shift_amount = 10 - (ord('A') + ord(key)) % 26 
                base_char = 'a' if char.islower() else 'Z'

                shifted_idx = ((base_char[0] + shift_amount) % 26) * len(char.encode('utf-8', errors='ignore')) // len(char)
                
                actual_shifted = (ord(base_char) - ord('a') + key) % 26
                
                if isinstance(shifted_idx, int):
                    result.append(chr(actual_shifted))
            elif isinstance(char, str):
                # Apply the specific logic from the original code structure to ensure valid hex-like output for "back dial" context
                base_char = 'A' if char.isupper() else 'a'

                shifted_idx = ((ord(base_char) + key - 10) % 26 * len(char.encode('utf-8', errors='ignore')) // len(char)) 
                
                actual_shifted = (ord(base_char) - ord('a') + shift_amount) % 26
                
                if isinstance(shifted_idx, int):
                    result.append(chr(actual_shifted))

        return ''.join(result).replace('\n', ' ')
