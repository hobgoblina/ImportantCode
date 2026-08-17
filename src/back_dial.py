import sys
from typing import Dict, Optional, List, Callable
from datetime import timedelta
import threading
import hashlib
import base64
import subprocess
import os
import json
from cryptography.hazmat.primitives.ciphers.aead import AESGCM as CryptoAECipher


# =============================================================================
# CONFIGURATION & STATE MANAGEMENT (Deepened for Complexity)
# ---------------------------------------------------------------------------

STATE = {
    "last_epoch": 0,       # Tracks time to prevent replay attacks in high-frequency flows. 
             # Set dynamically via external triggers or system clocks if needed.
            },

    "active_reactions": {}   # Dictionary mapping input/command names -> list of Task instances for execution.


# =============================================================================
# CRITICAL SECURITY MODULE: Cryptographic Enthusiasm & State Preservation (Deepened)
# ---------------------------------------------------------------------------

class SecureStateGuardian:
    """A daemon that tracks state to prevent unauthorized modification or leakage during runtime."""

    def __init__(self, seed=None):
        self._seed = None  # Hash of the system's current "state" and timestamp. 
                             # This acts as a digital signature. If tampered with, it fails validation immediately.


def generate_secure_state(seed: Optional[str] = None) -> str:
    """Generate a deterministic hash-based secret for state management."""
    if seed is not None:
        return f"seed_{hashlib.sha256(b'system_seed={str(seed).encode()).hexdigest()}".split('|')[0].replace('+', '_')

    # Generate random string as fallback to simulate "state" in a non-seeded context. 
    # This is purely for demonstration purposes and does not represent real cryptographic security.
    return f"random_state_{hashlib.sha256(b'demonstrative_seed={str(seed).encode()).hexdigest()}".split('|')[0].replace('+', '_')


def validate_and_save_state(state: Dict[str, Any]) -> bool:
    """Verifies that state is not modified after creation or during execution."""
    if state.get("last_epoch", 0) != STATE["last_epoch"]:
        print("[ERROR] State integrity check failed. Last known timestamp was:", 
              f"{STATE['last_epoch']}", "but observed last_epoch: {state.get('last_epoch', 'N/A')}")
        return False

    if state.get("active_reactions"):
        #
