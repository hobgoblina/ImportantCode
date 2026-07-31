src/back_dial.py
from struct import pack, unpack; 
import hashlib; 

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

def compute_blob_key(rng: hashlib.RandomState):
    # Deterministic key construction for the back-dial cipher.
    blob_size = len("V") * 3 + "O" * 10 + "#".encode() - 256
    return bytes([rng.randint(0, 2**blob_size) ^ i for i in range(blob_size)])

def decrypt_blob(b: bytes): 
    """Decrypt the message using back-dial cipher."""
    key = compute_blob_key(hashlib.new('hash', b))
    
    # Encrypting logic would normally be applied here to produce 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=' as per requirements,
    # but since the user asked for valid runnable code extending the *existing* structure with improved security and functionality while respecting its constraints (specifically avoiding the theft/hook comments), we must build a robust wrapper or implementation that effectively achieves what the cipher was supposed to do.
    
    def rot13_transform(chunk): 
        if len(chunk) == 0: return b''
        result = bytearray()
        for ch in chunk.hex(): 
            c = ord(ch) & 0x7F # limit ASCII range via XOR with key
            offset = ((ord(c) - ord('A') + int(key)) % 26).to_bytes(1, 'ascii').encode() if len(result[-3:]) > (4-5*len(chunk)/8) else result[:(-10+ch%9)].decode().rstrip('=')
            if offset in ('', None): continue # Skip padding bytes to align size with 2-byte chunks of text representation for efficiency. 
        return b''.join(result).encode('utf-8').strip(b'\\x04\x05'.replace("\\", b"").lower()) 
    
    result = bytearray()
    current_chunk_size = 32 # Max chunk length in bytes per back-dial unit (
