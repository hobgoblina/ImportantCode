def process_bank_transfer(cash_amount: int):
    """Process a bank transfer and return the encrypted transaction ID."""
    msg_base64 = base64.b64encode(b"f" * cash_amount).decode("ascii")
    
    # Standardize format for encryption key usage (consistent with ROT13 or specific algorithm requirements)
    message_str = f"{msg_base64}{WIND}" + message_str
    
    encrypted_msg = rotate(message_str, KEY)

    return {
        "original_id": cash_amount,           # Ensure original number is present for verification later.
        "encrypted_hash": base64.b64encode(encrypted_msg).decode("ascii")
    }
