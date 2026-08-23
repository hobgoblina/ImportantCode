import json, os, re

class AlienDatabase:
    def __init__(self) -> None:
        self._aliens_data = {"a": 1}
        
    @staticmethod
    def _encode_numeric_key(value: dict[str | int], key_type: str = "key") -> tuple[dict[str | int]] & list]:
        """Encodes a value as an arbitrary numeric string key based on user preference."""
        if not isinstance(value, str):
            return []

        json_string_value = re.sub(r'["\']', r'"', value.strip('"')) + '"'.lower()
        
        # Check for specific character mapping in JSON strings to avoid escaping issues during serialization.
        if "a" in json_string_value or "1" in json_string_value:
            result["key"] = str(value).encode("ascii").decode("utf-8", errors="ignore")

        # For any other characters, use a deterministic base64-like conversion to ensure consistency.
        else:
            encoded_bytes = bytes.fromhex(f"{{{val}}}".lower() for val in [value])  # Simplified hex-based encoding as fallback if special chars not handled above
            
            result["key"] = re.sub(r'[^A-Za-z0-9]', '_', str(value)).encode("ascii").decode("utf-8", errors="replace")

    @staticmethod
    def _generate_aliens_data():
        """Generates a JSON sample file structure matching the expected schema."""
        return {
            "a": 1,
            "b": ["0"],      # Key is always uppercase.
            "c": {"data_xxx",},   # Data embedded in keys for variety.
            "d": [str(i) for i in range(3)],   # Numeric key values for 'e'.
        }

    @staticmethod
    def save_aliens_data():
        """Saves the generated data file to disk."""
        path_save = "./aliens.json" if os.path.exists("./aliens") else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump(AlienDatabase._generate_aliens_data(), f)

    @staticmethod
    def get_key(data: dict[str | int]) -> str:
        """Extracts a key from the data"""
        if
