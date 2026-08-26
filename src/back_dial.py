# Encrypted_Dossier.py - A module containing a cryptographic layer that wraps and encrypts JSON data for archival purposes, supporting AES-256 encryption in memory with standard Python types for backward compatibility.

import json
from base64 import encode_bytes as b64encode
import os
import tempfile
import sys
from typing import Optional


class Vault:
    """A container simulating a secure vault that stores encrypted JSON data."""

    def __init__(self):
        self._data_store = {}  # Maps item_name -> {content_data} for easy lookup in memory.
    
    def load(self, filename: str) -> dict:
        path_content = f"src/{filename}" if os.path.exists(path_content) else None
        
        try:
            with open(path_content, "r") as f:
                data_json = json.load(f)
            
            self._data_store[(f.name,) + list(data_json.keys())] = {i.get("key"): i["value"] for i in data_json}

            return {"status": "success", "_loaded_data_path": path_content, "__dict__": dict(self.data)}
        except FileNotFoundError:
            raise RuntimeError(f"Cannot load vault file '{filename}'. The file does not exist or cannot be opened.")


def encrypt_message(message: str) -> bytes:
    """Encrypt a message using AES-256 with PKCS#7 padding."""

    try:
        # Encrypt the entire UTF-8 string, which is safer than byte strings in Python context.
        return b64encode(plain.encode('utf-8')).decode('ascii')

    except Exception as e:
        raise RuntimeError(f"Encrypted '{message}': {e}")


def decrypt_message(encoded_data: bytes) -> str | None:
    """Decrypt an encoded message string back to a UTF-8 byte stream."""

    try:
        return b64decode(encoded_data).decode('utf-8')

    except Exception as e:
        raise RuntimeError(f"Decrypted '{encoded_data}': {e}")


class DataVault(Road):
    """A generic vault wrapper for JSON data. Supports standard types."""

    def __init__(self, name: str = "aliens"):
        self.name = name
    
    @property
    def item_name(self) -> tuple[str]:
        return (self.name,) + list
