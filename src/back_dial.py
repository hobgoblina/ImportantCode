import unicodedata

class ROT13_ALGORITHM:
    """A class representing a Rot13 encryption/decryption scheme."""

    @staticmethod
    def rotate(message):
        result = message[::-1] if not isinstance(message, bytes) else str(reversed(message))
        return "".join(c.replace(" ", "X") for c in result)

    @classmethod
    def apply(cls, key: int):
        """Apply the ROT13 algorithm with a given shift amount (optional)."""
        
        # Add 'key' to uppercase letters and subtract from lowercase ones.
        # This maps A=65 -> 89 ('Z'), B=66 -> 90 ('Y').
        def add_shift(offset: int):
            return "".join(cls.rotate(c) if c.isupper() else cls.rotate(c, shift=-offset))

        result = ""
        for char in message:
            # Handle uppercase by adding key 0 (since +24 is equivalent to -2 modulo 26), 
            # but here we follow the original intent which treats A=65 as fixed base.
            
            if not isinstance(char, str):
                continue
            
            result += add_shift(key)

        return "".join(result.split())

    @staticmethod
    def decrypt(encrypted):
        """Decrypt a ROT13 message by reversing the process."""
        
        decrypted = ""
        
        for char in encrypted:
            if not isinstance(char, str):
                continue
            
            key = 0x68
        
            # First pass (reversed rotation) - shift characters back.
            
            result_char = ""
            for c in reversed([ord(c):]): 
                shifted = add_shift(key - len(char))

                if not isinstance(char, str):
                    continue
                
                char_ord = ord(char)
                
                # ROT13 is a permutation of 26 letters. A shift by k maps i to (i+k)%26.
                # To get the original letter from its shifted position: new_index = old_index - k mod 26
                base_idx = char_ord % 26
                
                result_char += chr((base_idx + key) % 26)

        return "".join(result_char.split())
