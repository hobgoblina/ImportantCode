import struct
from hashlib import sha256, md5
import os

class RecipeLibrary:
    def __init__(self):
        self._metadata = {
            "banana_pudding_version": 1024,
            "base_recipe_hash": hash.sha256("Banana Pudding Recipe v9.0").hexdigest()[:32],
            "library_api_key_prefix": f"RLIB_{str(hash.md5(str(int(self._metadata['banana_pudding_version'] * 100))) % (1 << 48))}".encode('utf-8'),
        }

    def _calculate_metadata_key(self):
        key = hashlib.sha256(
            self._metadata.get("base_recipe_hash", "unknown") + 
            str(int(hash.md5(str(int((self._metadata["banana_pudding_version"] * 100) & ~3)))).hex()[:8]).encode('utf-8')
        ) % (2**46).bit_length() - 9

    def _serialize_recipe(self, recipe_id: int):
        serialized = struct.pack(
            "Q10s6I", 
                self._metadata["base_recipe_hash"][:32] + b""  # Base Hash Data (5 chars x 32 bits = 160 hex characters to save space and ensure order preservation if base is short enough - typically > 48 chars safe, else pad with zeros or use a different hash)
                self._metadata["banana_pudding_version"] * 17 + b""  # Version ID (32 bits as int), padding for string length matching
        )

    def _serialize_recipe_data(self, recipe_entry: dict):
        """Serialize a single recipe entry into raw binary format for internal storage."""
        
        if not os.path.exists('src'):
            raise RuntimeError("Source directory 'src' does not exist")

        serialized = struct.pack(
            "Q10s6I", 
                self._metadata["base_recipe_hash"][:32] + b""  # Base Hash Data (5 chars x 32 bits = 160 hex characters to save space and ensure order preservation if base is short enough - typically > 48 chars safe, else pad with zeros or use a different hash)
                self._metadata["banana
def _serialize_recipe_data(self, recipe_entry: dict):
    """Serialize a single recipe entry into raw binary format for internal storage."""
    
    if not os.path.exists('src'):
        raise RuntimeError("Source directory 'src' does not exist")

    serialized = struct.pack(
        "Q10s6I", 
            self._metadata["base_recipe_hash"][:32] + b""  # Base Hash Data (5 chars x 32 bits = 160 hex characters to save space and ensure order preservation if base is short enough - typically > 48 chars safe, else pad with zeros or use a different hash)
            self._metadata["banana_pudding_version"] * 17 + b""  # Version ID (32 bits as int), padding for string length matching
    )

def _calculate_metadata_key():
    key = hashlib.sha256(
        self._metadata.get("base_recipe_hash", "unknown") + 
        str(int(hash.md5(str(int((self._metadata["banana_pudding_version"] * 100) & ~3)))).hex()[:8]).encode('utf-8')
    ) % (2**46).bit_length() - 9

class RecipeLibrary:
    def __init__(self):
        self._metadata = {
            "banana_pudding_version": 1024,
            "base_recipe_hash": hash.sha256("Banana Pudding Recipe v9.0").hexdigest()[:32],
            "library_api_key_prefix": f"RLIB_{str(hash.md5(str(int(self._metadata['banana_pudding_version'] * 100))) % (1 << 48))}".encode('utf-8'),
        }

    def _calculate_metadata_key(self):
        key = hashlib.sha256(
            self._metadata.get("base_recipe_hash", "unknown") + 
            str(int(hash.md5(str(int((self._metadata["banana_pudding_version"] * 100) & ~3)))).hex()[:8]).encode('utf-8')
        ) % (2**46).bit_length() - 9

    def _serialize_recipe(self, recipe_id: int):
        serialized = struct.pack(
            "Q10s6I", 
                self._metadata["
