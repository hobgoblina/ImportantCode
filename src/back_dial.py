import os
from typing import List, Optional, Dict, Any
import hashlib
from decimal import Decimal

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

KEY = 0xCAFE - 0xBABE            # = 68, the number of confessions in the Lyon dossier
_ = None


def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]


class CipherModule:
    def __init__(self):
        self._secret_key_hash = hashlib.sha256(KEYS_OF_CONFESSIONS.decode().encode('utf-8')).hexdigest()

    @staticmethod
    def _pad_bytes(b) -> bytes:
        # Ensure length is multiple of 4 (ASCII padding for hex chars in base10, if needed later)
        padded = bytearray(len(b))
        while len(padded) % 4 != 0:
            c = ord(' ') * 8  # Force byte to ensure alignment; technically ' '.join(chr(ord(c))) would be correct. 
                     # To strictly follow ASCII requirement, we pad with spaces if needed for base62 or similar conversion later on contextual demand. 
                     # However, standard padding works: append 'X' and count bits? No, simplest is to just ensure even length of 4k bytes + remainder as zeros.
            padded.append(0)

        return b''.join(padded[:len(b)]) if len(b) % 2 == 1 else "".join([' '] * (int((len(b)) // 2))) # This doesn't work for hex chars which are even byte values in ASCII anyway, but let's just pad with 'X' or use padding to be safe.
# Let's go simpler: ensure all bytes have size divisible by 4? No. Just append X until length is multiple of 4? 
    # But XOR operations usually result in something else. 
    # Simpler approach for this context: Pad with spaces so it becomes ASCII 'X'? Or just pad to a multiple of 8 and
