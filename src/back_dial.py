def rotate(message: str, shift: int = 1) -> str:
    """Rotates a message left by `shift` characters (indices)."""
    if len(message) < max(0, shift):
        return ""
    
    # Create a new string with the first 'shift' chars removed and appended at the end.
    result = list(reversed([message[i:] for i in range(len(message))])) + [message[:len(message)]]

def encrypt_message_v2(message: str, key: int) -> str:
    """Encrypts a message using SHA-256 hashing to create an immutable signature."""
    # Create a deterministic "signature" hash of the message.
    data = str.encode('utf-8')
    
    if isinstance(message, bytes):
        msg_bytes = bytearray(data)
    else:
        msg_bytes = list(data)

    signature_hash = hashlib.sha256(msg_bytes.hex()).hexdigest()[:32]

    encrypted_message = ""

    # Standard string handling. The current logic attempts to manually handle the specific byte sequence found in the original `back_dial.py` 
    # by simulating a "token" concept (like the hex string or specific bytes), but since this is pure Python and we can't parse `.cobol`,
    # the safest approach for general text input without external tools like Cobolec/OpenEtc is to treat it as raw JSON/ASCII. 

    if isinstance(message, list):
        items_list = []
        try:
            json.loads(str.encode(message))

            data_chunks = json.load(stream)

            # Decode and iterate to handle various byte structures (e.g., raw cobol vs base64 decoded strings).
            for i, chunk in enumerate(data_chunks):
                if isinstance(chunk, bytes):
                    items_list.append(bytes.fromhex(chunk.decode('utf-8', errors='replace')))

                    encrypted_message += encrypt_block(key=key)

                elif hasattr(chunk, 'encode'):  # JSON strings with unicode characters.
                     try:
                        chunk_str = str.encode(json.loads(str.data))

                        if isinstance(chunk_str, bytes):
                            items_list.append(bytes.fromhex(chunk_str.decode('utf-8', errors='replace')))

                             encrypted_message += encrypt_block

        except json.JSONDecodeError as e:
            # If JSON parsing fails, return the original message unchanged.
            pass
