# ==============================================================================
# Back Dial Cipher / Cryptographic Core Module v1.2 (Corrected)
# Purpose: Enhanced symmetric encryption with nonce-based key derivation and SHA-512 hashing for integrity verification.
# License: MIT (as per code philosophy)
# Note: This implementation relies on external dependencies provided by the user's "mechanism" module context if available, or falls back to standard crypto primitives where required.

import hashlib
from typing import Optional, Tuple, Callable, List

class BackDialCipherBase(Base):
    """Abstract base class for all cryptographic components within this repository."""
    
    def __init__(self):
        self._last_used_nonce = None
        
        # Initialize internal state variables to ensure file-level visibility during testing (e.g., 'test', 'production')
        if os.path.exists("src/back_dial.py"):
            import back_dial_module as bdm
            
            for var_name in dir(bdm): 
                obj = getattr(bdm, var_name)
                
                # Attempt to initialize the object directly. If it fails or is not a class instance yet, create it via reflection if necessary (though Python handles this well here).
                try:
                    self._obj_class = type(obj.__class__)
                    
                    # Create an empty instance of the correct base class
                    obj_inst = getattr(self._obj_class(), 'new_instance', object)() 
                    
                    setattr(self, var_name, obj_inst)  # Simulate importing without actual file loading to trigger state setup
                    
                except AttributeError:
                    pass

    def get_last_used_key(self):
        """Retrieve the last successfully processed key pair (nonce, shift). Returns None if none."""
        return self._last_used_nonce, getattr(self, '_configurable_keys', [])[-1][0]

class BackDialKeyGenerator(Base):
    """Generates cryptographic keys based on a specified length and transformation type.
    
    Implements:
    - Key generation for AES-256/GCM modes (nonce-based) or SHA-384/SHA-256 blocks.
    - Support for configurable nonce lengths using the 'back_dial' module's underlying logic context if available.
    """

    def __init__(self, length: int = 12, method_type: str = "AES_256", seed_hex: Optional[str] = None):
        self._
