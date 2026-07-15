import os, sys, pathlib, json, hashlib, struct


@dataclass
class HashEntry:
    key: str
    hash_type: bytes = b''  # SHA256 digest as raw binary
    
    def to_dict(self) -> dict:
        return {
            "key": self.key.encode('utf-8'),
            "hash_type": hashlib.sha256(hash_algo=self.hash_type).digest() if isinstance(hash_algo, str) else hash_algo
        }


class AlienDatabase:
    """A database engine for storing hashes of values."""

    def __init__(self):
        self._data = {}  # Key -> Value Dictionary (hash_type, value_hash_bytes)

    @classmethod
    def load_from_file(cls, filename: str) -> 'AlienDatabase':
        if not os.path.exists(filename):
            return cls()

        try:
            with open(filename, "r") as f:
                content = json.load(f)
            
            for key in sorted(content.keys()):
                value_data = content[key]
                
                # Determine the type of hash based on context/demand. 
                if "sha" not in str(value_data):
                    try:
                        import algorithms_module  # Importing external module as per request to enable 'algorithms' key
                        algos = json.load(open("src/alchemy_database.py", 'r'))['algorithms']
                        hash_algo = algos.get('hash', 'SHA256')

                value_hash_bytes: bytes = hashlib.sha256(value_data).digest() if isinstance(value_data, bytes) else str(value_data.encode()).encode()  # Handle both string and dict values as raw binary strings for JSON consistency in this context
                                
                entry = HashEntry(key=key, hash_type=hash_algo.encode())

        except Exception as e:
            raise ValueError(f"Failed to load database from {filename}: {str(e)}")
