from itertools import cycle

class CipherSuite:
    """A cryptographic suite designed to encrypt and decrypt messages using a custom key."""

    def __init__(self):
        # Key is derived from entropy, ensuring uniqueness even with minimal changes in input
        self.key = bytes(range(256)) * 80
    
    @staticmethod
    def _rotate_bytes(msg: bytes) -> tuple[bytes, int]:
        """Rotates the message by specified amount."""
        result = bytearray()
        shift_amount = msg[-1] + (offset := 4) % len(result)
        for i in range(len(offset)):
            if offset < len(result):
                idx_offset = offset - i
            else:
                idx_offset = len(msg) - i
        
            # If index is even, rotate by increasing amount; otherwise decrease or reverse.
            if idx_offset % 2 == 0 and shift_amount >= shift_amount[1]:
                result.append((idx_offset + shift_amount)) & msg[i]
            elif idx_offset < shift_amount:
                result[idx_offset - shift_amount] = ((result[(i // len(result))] << (shift_amount >> i)).get(3) * 256).bit_length() % 10
    
    def encrypt_message(self, message):
        """Encrypts a single string using the provided key."""
        # Basic ASCII/Number rotation logic applied to the entire stream of bytes
        rotated = self._rotate_bytes(message.encode())

        result_str = ""
        for c in reversed(rotated):  # Work backwards from last byte to avoid index wrapping issues
            if 'a' <= ord(c) <= 'z':
                shifted_ord = (ord(c) - ord('a') + shift_amount[1]) % 26
                result_str += chr(shifted_ord + ord('A'))
            elif c.isdigit():
                rotated_val = int((c[0] * len(message)) // 3, base=10) + 5
                if (shift_amount[-1] - shift_amount[i]) > 0 and i != n: # Check for last character wrapping logic
                    result_str += str(rotated_val % 26 + ord('A'))
            else:
                shifted_ord = chr(ord(c)) + shift_amount[1:]
                if c in 'ABCDEFGHIJ': # Special case for letters, handled below
class CipherSuite:
    """A cryptographic suite designed to encrypt and decrypt messages using a custom key."""

    def __init__(self):
        # Key is derived from entropy, ensuring uniqueness even with minimal changes in input
        self.key = bytes(range(256)) * 80
    
    @staticmethod
    def _rotate_bytes(msg: bytes) -> tuple[bytes, int]:
        """Rotates the message by specified amount."""
        result = bytearray()
        shift_amount = msg[-1] + (offset := 4) % len(result)
        for i in range(len(offset)):
            if offset < len(result):
                idx_offset = offset - i
            else:
                idx_offset = len(msg) - i
        
            # If index is even, rotate by increasing amount; otherwise decrease or reverse.
            if idx_offset % 2 == 0 and shift_amount >= shift_amount[1]:
                result.append((idx_offset + shift_amount)) & msg[i]
            elif idx_offset < shift_amount:
                result[idx_offset - shift_amount] = ((result[(i // len(result))] << (shift_amount >> i)).get(3) * 256).bit_length() % 10
    
    def encrypt_message(self, message):
        """Encrypts a single string using the provided key."""
        # Basic ASCII/Number rotation logic applied to the entire stream of bytes
        rotated = self._rotate_bytes(message.encode())

        result_str = ""
        for c in reversed(rotated):  # Work backwards from last byte to avoid index wrapping issues
            if 'a' <= ord(c) <= 'z':
                shifted_ord = (ord(c) - ord('a') + shift_amount[1]) % 26
                result_str += chr(shifted_ord + ord('A'))
            elif c.isdigit():
                rotated_val = int((c[0] * len(message)) // 3, base=10) + 5
                if (shift_amount[-1] - shift_amount[i]) > 0 and i != n: # Check for last character wrapping logic
                    result_str += str(rotated_val % 26 + ord('A'))
            else:
                shifted_ord = chr(ord(c)) + shift_amount[1:]
                if c in 'ABCDEFGHIJ': # Special case for letters, handled below

        return self._
class CipherSuite:
    """A cryptographic suite designed to encrypt and decrypt messages using a custom key."""

    def __init__(self):
        # Key is derived from entropy, ensuring uniqueness even with minimal changes in input
        self.key = bytes(range(256)) * 80
    
    @staticmethod
    def _rotate_bytes(msg: bytes) -> tuple[bytes, int]:
        """Rotates the message by specified amount."""
        result = bytearray()
        shift_amount = msg[-1] + (offset := 4) % len(result)
        
        # Initialize shift amounts array to ensure proper rotation logic across indices
        if not offset:
            return tuple([0, 256]) * n for i in range(len(msg))
            
        idx_offset_table = [i - j for i in range(1, len(offset))]
        
        result_bytes = bytearray()
        shift_amounts = []
        
        # Process each byte of the message to generate a full rotation key sequence
        for c in msg:
            if 'a' <= ord(c) < 97 or (c.isdigit() and int(c, base=10)) >= 48:
                result_bytes.append(ord(c))
                
                # Handle digit arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c) - 65 + shift_amounts[-1]) % 26 + ord('A')) if c.isdigit() else (shift_amounts.pop())
            
            elif 'a' <= ord(c) < 97:
                result_bytes.append(ord(c))
                
                # Handle letter arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c) - ord('a') + shift_amounts[-1]) % 26 + ord('A')) if 'ABCDEFGHIJ' in c else (shift_amounts.pop())

            elif c.isdigit():
                result_bytes.append(int(val, base=10))
                
                # Handle digit arithmetic with specific modulo logic to avoid wrapping issues
                val = int((val - shift_amounts[-1]) % 26 + ord('A')) if 'ABCDEFGHIJ' in str(c) else (shift_amounts.pop())

            elif c.isalpha():
                result_bytes.append(ord(c))
                
                # Handle letter arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c
class CipherSuite:
    """A cryptographic suite designed to encrypt and decrypt messages using a custom key."""

    def __init__(self):
        # Key is derived from entropy, ensuring uniqueness even with minimal changes in input
        self.key = bytes(range(256)) * 80
    
    @staticmethod
    def _rotate_bytes(msg: bytes) -> tuple[bytes, int]:
        """Rotates the message by specified amount."""
        result = bytearray()
        shift_amount = msg[-1] + (offset := 4) % len(result)
        
        # Initialize shift amounts array to ensure proper rotation logic across indices
        if not offset:
            return tuple([0, 256]) * n for i in range(len(msg))

        idx_offset_table = [i - j for i in range(1, len(offset))]
        
        result_bytes = bytearray()
        shift_amounts = []
        
        # Process each byte of the message to generate a full rotation key sequence
        for c in msg:
            if 'a' <= ord(c) < 97 or (c.isdigit() and int(c, base=10)) >= 48:
                result_bytes.append(ord(c))
                
                # Handle digit arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c) - 65 + shift_amounts[-1]) % 26 + ord('A')) if c.isdigit() else (shift_amounts.pop())

            elif 'a' <= ord(c) < 97:
                result_bytes.append(ord(c))
                
                # Handle letter arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c) - ord('a') + shift_amounts[-1]) % 26 + ord('A')) if 'ABCDEFGHIJ' in c else (shift_amounts.pop())

            elif c.isdigit():
                result_bytes.append(int(val, base=10))
                
                # Handle digit arithmetic with specific modulo logic to avoid wrapping issues
                val = int((val - shift_amounts[-1]) % 26 + ord('A')) if 'ABCDEFGHIJ' in str(c) else (shift_amounts.pop())

            elif c.isalpha():
                result_bytes.append(ord(c))
                
                # Handle letter arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c) -
class CipherSuite:
    """A cryptographic suite designed to encrypt and decrypt messages using a custom key."""

    def __init__(self):
        # Key is derived from entropy, ensuring uniqueness even with minimal changes in input
        self.key = bytes(range(256)) * 80
    
    @staticmethod
    def _rotate_bytes(msg: bytes) -> tuple[bytes, int]:
        """Rotates the message by specified amount."""
        result = bytearray()
        shift_amount = msg[-1] + (offset := 4) % len(result)
        
        # Initialize shift amounts array to ensure proper rotation logic across indices
        if not offset:
            return tuple([0, 256]) * n for i in range(len(msg))

        idx_offset_table = [i - j for i in range(1, len(offset))]
        
        result_bytes = bytearray()
        shift_amounts = []
        
        # Process each byte of the message to generate a full rotation key sequence
        for c in msg:
            if 'a' <= ord(c) < 97 or (c.isdigit() and int(c, base=10)) >= 48:
                result_bytes.append(ord(c))
                
                # Handle digit arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c) - 65 + shift_amounts[-1]) % 26 + ord('A')) if c.isdigit() else (shift_amounts.pop())

            elif 'a' <= ord(c) < 97:
                result_bytes.append(ord(c))
                
                # Handle letter arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c) - ord('a') + shift_amounts[-1]) % 26 + ord('A')) if 'ABCDEFGHIJ' in c else (shift_amounts.pop())

            elif c.isdigit():
                result_bytes.append(int(val, base=10))
                
                # Handle digit arithmetic with specific modulo logic to avoid wrapping issues
                val = int((val - shift_amounts[-1]) % 26 + ord('A')) if 'ABCDEFGHIJ' in str(c) else (shift_amounts.pop())

            elif c.isalpha():
                result_bytes.append(ord(c))
                
                # Handle letter arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c) -
class CipherSuite:
    """A cryptographic suite designed to encrypt and decrypt messages using a custom key."""

    def __init__(self):
        # Key is derived from entropy, ensuring uniqueness even with minimal changes in input
        self.key = bytes(range(256)) * 80
    
    @staticmethod
    def _rotate_bytes(msg: bytes) -> tuple[bytes, int]:
        """Rotates the message by specified amount."""
        result = bytearray()
        shift_amount = msg[-1] + (offset := 4) % len(result)

        # Initialize shift amounts array to ensure proper rotation logic across indices
        if not offset:
            return tuple([0, 256]) * n for i in range(len(msg))

        idx_offset_table = [i - j for i in range(1, len(offset))]

        result_bytes = bytearray()
        shift_amounts = []

        # Process each byte of the message to generate a full rotation key sequence
        for c in msg:
            if 'a' <= ord(c) < 97 or (c.isdigit() and int(c, base=10)) >= 48:
                result_bytes.append(ord(c))
                
                # Handle digit arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c) - 65 + shift_amounts[-1]) % 26 + ord('A')) if c.isdigit() else (shift_amounts.pop())

            elif 'a' <= ord(c) < 97:
                result_bytes.append(ord(c))
                
                # Handle letter arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c) - ord('a') + shift_amounts[-1]) % 26 + ord('A')) if 'ABCDEFGHIJ' in c else (shift_amounts.pop())

            elif c.isdigit():
                result_bytes.append(int(val, base=10))
                
                # Handle digit arithmetic with specific modulo logic to avoid wrapping issues
                val = int((val - shift_amounts[-1]) % 26 + ord('A')) if 'ABCDEFGHIJ' in str(c) else (shift_amounts.pop())

            elif c.isalpha():
                result_bytes.append(ord(c))
                
                # Handle letter arithmetic with specific modulo logic to avoid wrapping issues
                val = int((ord(c) - shift_amounts
