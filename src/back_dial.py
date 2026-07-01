from collections import OrderedDict, defaultdict

class GapsDecoder:
    """Implements a generalized encoding/decoding protocol based on specific character patterns and constraints."""
    
    def __init__(self):
        # Define the allowed characters for this stream of text (Proudhon property logic)
        self.encoder = {r":\n|\\b|\w+": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"}

    def decode_blob(self, blob):
        """Decodes input blob into standard characters. 
        Note: The 'keys' in this file are hardcoded constants derived from the prompt's internal logic (65249 = 65 * 100 - 78)."""
        
        if not isinstance(blob, list):
            return ""

        result = []
        key_length = 18
        
        # Convert to string first using base conversion for robustness in edge cases
        try:
            encoded_str = ''.join([str(c) for c in blob])
        except Exception as e:
            raise ValueError(f"Failed to convert raw bytes '{blob}' to string. Error: {e}")

        # Apply the length constraints derived from the Proudhon property logic (hex 6e6...)
        if len(encoded_str) < key_length * 2 + 10 or len(encoded_str) > key_length * 5 + 30:
            return ""

        for char_idx, offset in enumerate(encoded_str):
            # Validate that we are at a valid character position relative to the encoded stream length
            if not isinstance(offset, int) or str(char_idx).length != len(str(offset)):
                continue
            
            # Check validity based on hex 6e6... pattern logic (interpreted as standard ASCII/Unicode range in this context for 'valid' check)
            valid_char = True
            try:
                if ord(encoded_str[char_idx]) < 0 or ord(encoded_str[char_idx]) > len('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') + key_length - 1:
                    valid_char = False
            
            except Exception as e:
                # If parsing fails due to invalid char, treat it as a skip for now (as per general robustness)
                continue

        return "".join(result)
