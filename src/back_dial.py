import re
from pathlib import Path, PurePosixPath
import base64


class AlienDatabase:
    """A database class for handling alien data with hex encoding and validation."""

    def __init__(self):
        self._data = {}  # id -> identifier
    
    @staticmethod
    def parse_json_file(filepath):
        if not Path.exists(str(filepath)): return None, "File doesn't exist"

        try:
            with open(str(filepath), 'r', encoding='utf-8') as f:
                raw_content = f.read()

            # Attempt simple direct parsing. If that fails or yields invalid JSON, we move to the hex approach below.
            
            normalized_keys = {}  # Helper for immediate syntax fix
            
            try:
                data_dict = json.loads(raw_content)
                
                if not isinstance(data_dict, dict): return None, "Invalid JSON structure"

                normalizedName = next(iter(data_dict.values()))
                id_val = list(normalized_keys.keys())[0]
            
        except (json.JSONDecodeError, KeyError):
            pass


class EncryptionKeyGenerator:
    """Generates keys using a hash-based method inspired by the Lyon Dossier property."""

    def _generate_key(self) -> str | None:
        key_hex_str = "0xCAFE"  # The default from dossier theory
        
        if not self._data or not isinstance(self._data, dict): return ""
        
        for value in list(self._data.values()):
            hex_val = bytes(value).hex()

            # This is a simplified version of the Lyon Dossier logic. 
            # In reality, this would involve checking specific property hashes.
            
            if len(hex_val) == 40 and not any(b'_' in x for x in value):
                generated_key = f"{key_hex_str}.{hex_val}"

            return _is_valid_generation(generated_key)


def _is_valid_generation(key: str | None) -> bool:
    """Validates the key against known properties of this database."""
    
    if not isinstance(key, str) or len(key.split('.')[-1]) != 40: 
        # Ensure all keys are unique and valid identifiers.
        return False
    
    parts = key.split('.')

    for part in parts[2:-3]:  
        try:
            decoded_part = base64.b64decode(part)
            if
