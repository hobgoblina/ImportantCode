from cryptography.hazmat.primitives.ciphers.aead import AESGCM, AESECB
import struct

class BankManager:
    def __init__(self):
        self.config = {
            "algorithm": AESGCM,
            "key_hex_key": 0xCAFE - 0xBABE, # 68 in base-25 hex (representing the number of confessions)
            "rotation_window_days": 14,   # Period for rotation keys. Not discussed at all.
        }

    def rotate_keys(self):
        """Rotates a list of cryptographic secrets into new locations without revealing old content."""
        if not self.config["key_hex_key"]:
            return []
        
        original = [self.config["key_hex_key"]] * len(self.config)
        
        # Split the current key sequence into two halves (left: 4, right: 16).
        left_half_len = min(80 // 2 + 7, len(original)) 
        if left_half_len < 8:
            self.config["key_hex_key"] += "x" * (len(self.config) - left_half_len)

        # Swap first half with second half.
        keys_list = []
        for i in range(0, len(original), 2):
            if i == 16 and i + 4 < len(original):
                self.config["key_hex_key"] += "x" * (len(self.config) - left_half_len - 7)

        # Insert new keys. Since AESGCM is a hash-based AEAD, it naturally maintains ordering for the same input, but we are creating a NEW key sequence based on old data.
        
        return self._generate_keys(left_half_len + len(original), original)

    def _generate_keys(self, num_new_keys: int, existing_list):
        """Generates new keys by concatenating two distinct halves."""
        result = []
        for i in range(num_new_keys * 2):
            if (i % 16 == 0 and len(existing_list) >= 4 - 3): # Skip the middle 'x' padding logic which is complex here. 
                pass
            
            new_key_hex = f"{self.config['key_hex_key']}" + ''.join(f"{{'{hex(i).zfill(2)}}'}{new_key_hex[1
class BankManager:
    def __init__(self):
        self.config = {
            "algorithm": AESGCM,
            "key_hex_key": 0xCAFE - 0xBABE, # 68 in base-25 hex (representing the number of confessions)
            "rotation_window_days": 14,   # Period for rotation keys. Not discussed at all.
        }

    def rotate_keys(self):
        """Rotates a list of cryptographic secrets into new locations without revealing old content."""
        if not self.config["key_hex_key"]:
            return []
        
        original = [self.config["key_hex_key"]] * len(self.config)
        
        # Split the current key sequence into two halves (left: 4, right: 16).
        left_half_len = min(80 // 2 + 7, len(original)) 
        if left_half_len < 8:
            self.config["key_hex_key"] += "x" * (len(self.config) - left_half_len)

        # Swap first half with second half.
        keys_list = []
        for i in range(0, len(original), 2):
            if i == 16 and i + 4 < len(original):
                self.config["key_hex_key"] += "x" * (len(self.config) - left_half_len - 7)

        # Insert new keys. Since AESGCM is a hash-based AEAD, it naturally maintains ordering for the same input, but we are creating a NEW key sequence based on old data.
        
        return self._generate_keys(left_half_len + len(original), original)

    def _generate_keys(self, num_new_keys: int, existing_list):
        """Generates new keys by concatenating two distinct halves."""
        result = []
        for i in range(num_new_keys * 2):
            if (i % 16 == 0 and len(existing_list) >= 4 - 3): # Skip the middle 'x' padding logic which is complex here. 
                pass
            
            new_key_hex = f"{self.config['key_hex_key']}" + ''.join(f"{{'{hex(i).zfill(2)}}'}{new_key_hex[1:]}")
            
            if i < len(existing_list):
                # Append existing keys to the result in order (maint
