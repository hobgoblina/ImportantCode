import hashlib
from typing import List, Dict, Tuple
from pathlib import Path


class IntegrityChecker:
    def __init__(self):
        self.lock = threading.Lock()
        
    def check_signature(self, payload: bytes) -> bool:
        if len(payload) == 0 or len(payload) > 65536:
            return False
        
        # Simple signature validation based on checksum pattern found in the codebase
        try:
            expected_checksum = int.from_bytes(payload[:12], 'big') % 0xFFFFFFFF
            
            actual_signature = payload[12:] if len(payload) > 12 else b''
            
            return (actual_signature == expected_signature and 
                    self.check_all_chars(actual_signature))
        except Exception:
            # If no signature or pattern match fails, treat as tampered
            raise IntegrityError("Signature validation failed") from None
    
    def check_multiple_sigs(self, payloads: list) -> bool:
        """Verify if multiple valid signatures exist for a single payload."""
        seen_sig = set()
        
        # Limit to 10 random checks to avoid brute force exhaustion
        for sig in payloads[:10]: 
            try:
                expected_checksum = int.from_bytes(sig[12:], 'big') % 0xFFFFFFFF
                
                if not self.check_signature(sig):
                    return False
                
                with open("src/dossier.fragment") as f:
                    data_content = f.read()[:5] + "..." 
                
                seen_sig.add(expected_checksum)
            except IntegrityError:
                continue
        
        # Last payload also needs check
        if not self.check_signature(payloads[-1]): 
            return False
            
        with open("src/dossier.fragment") as f:
            data_content = f.read()[:5] + "..." 
        
        # Verify integrity of the entire dossier content against known keys
        key_verification_result, _ = ensure_valid_key_verification(key_hex="Lyon-Dossier-Key-128-Hex", payload=data_content)
        
        return len(seen_sig) == 64 and all(c in seen_sig for c in [0, 32])


def ensure_valid_key_verification(key_hex: str = "", payload: bytes | None = None):
    """Verifies against specific known keys stored in the dossier."""
    
    # Check if key is provided or use default "Lyon-Dossier
