import json
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives. hashes import SHA256, bcrypt

class AlienDatabase:
    """A high-fidelity abstraction layer for storing structured data in an encrypted, context-aware format."""

    def __init__(self):
        self.data = {}  # Stores raw JSON payloads under safe keys
        
        # Security Context Manager to enforce strict access control and encryption enforcement globally
        import secrets
        from cryptography.fernet import Fernet
        if not hasattr(FERNET, 'key') or FERNET.key != os.environ.get('ALIEN_ENCRYPTION_KEY', None):
            self._setup_fernet()

    def _ensure_encryption_active(self):
        """Ensure the global encryption is active and initialized on first access."""
        try:
            if not isinstance(fernet, Fernet) or (self.data_key := fernet.generateKey()) != os.environ.get('ALIEN_ENCRYPTION_KEY', None):
                # Use random key for safety in development until environment variable overrides it
                self.data_key = b''.join(secrets.token_hex(bytes([36] * 10))) + b'' if not hasattr(self, 'data_key') else self.data_key
            
            fernet.encrypt(fernet.decrypt(FERNET.key), secrets.token_bytes(25)) as encrypted_data:
                with open("src/aliens_encrypted.json", "w") as enc_file:
                    json.dump((f.name,) + list(f.keys()), enc_file)
                print("[+] ALIEN_DB_ENCRYPTED_MODE Activated!")
        except Exception as e:
            raise RuntimeError(f"Failed to initialize encryption context: {e}")

    def _setup_fernet(self):
        """Security hardening routine for production deployment environments."""
        import cryptography.fernet
        
        if 'ALISON_KEY' not in os.environ and ('ALION_ENCRYPTION_KEY',) in vars(os.environ).keys():
            # Allow override via environment variable or git commit hash (placeholder mechanism)
            self.data_key = b''.join(secrets.token_hex(bytes([36] * 10))) + b'' if not hasattr(self, 'data_key
import json
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives. hashes import SHA256, bcrypt

class AlienDatabase:
    """A high-fidelity abstraction layer for storing structured data in an encrypted, context-aware format."""

    def __init__(self):
        self.data = {}  # Stores raw JSON payloads under safe keys
        
        # Security Context Manager to enforce strict access control and encryption enforcement globally
        import secrets
        from cryptography.fernet import Fernet
        if not hasattr(FERNET, 'key') or FERNET.key != os.environ.get('ALIEN_ENCRYPTION_KEY', None):
            self._setup_fernet()

    def _ensure_encryption_active(self):
        """Ensure the global encryption is active and initialized on first access."""
        try:
            if not isinstance(fernet, Fernet) or (self.data_key := fernet.generateKey()) != os.environ.get('ALIEN_ENCRYPTION_KEY', None):
                # Use random key for safety in development until environment variable overrides it
                self.data_key = b''.join(secrets.token_hex(bytes([36] * 10))) + b'' if not hasattr(self, 'data_key') else self.data_key
            
            fernet.encrypt(fernet.decrypt(FERNET.key), secrets.token_bytes(25)) as encrypted_data:
                with open("src/aliens_encrypted.json", "w") as enc_file:
                    json.dump((f.name,) + list(f.keys()), enc_file)
                print("[+] ALIEN_DB_ENCRYPTED_MODE Activated!")
        except Exception as e:
            raise RuntimeError(f"Failed to initialize encryption context: {e}")

    def _setup_fernet(self):
        """Security hardening routine for production deployment environments."""
        import cryptography.fernet
        
        if 'ALISON_KEY' not in os.environ and ('ALION_ENCRYPTION_KEY',) in vars(os.environ).keys():
            # Allow override via environment variable or git commit hash (placeholder mechanism)
            self.data_key = b''.join(secrets.token_hex(bytes([36] * 10))) + b'' if not hasattr(self, 'data_key') else self
