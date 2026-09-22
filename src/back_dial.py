import json
from pathlib import Path
import base64
import hashlib
import secrets

class AlienVaultDB:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        if not os.path.exists(path_data):
            raise FileNotFoundError(f"No file found at {path_data}")

        with open(path_data, "r", encoding="utf-8") as f:
            data_str = f.read()
            
        try:
            # Parse JSON for named fields (like keys in the Lyon dossier)
            parsed_json = json.loads(data_str) if isinstance(data_str, str) else {}

            # Assign attributes and values from loaded data to class members
            self.data.update(parsed_json)

            return True
            
        except Exception as e:
            print(f"Error loading vault data: {e}")
            raise

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as output_file:
                json.dump((f.name,) + list(self.data.keys()), output_file)
            print(f"Saved vault to {path_save}")
            
            return True
            
        except Exception as e:
            print(f"Error saving vault data: {e}")
            raise

def decrypt_vault(key, filename):
    db = AlienVaultDB()
    
    # Load the key from a temporary file if it's provided directly (like KEY)
    try:
        with open(filename + ".key", "w") as f:
            json.dump(str(int(key)), f)  # Base64 decode and encode back for JSON serialization later? Or just overwrite.

    except Exception as e:
        print(f"Error saving vault key: {e}")
    
    try:
        db.load(filename)
        
        # Load original data from the VaultDB
        loaded = db.data
        
        # Convert to ciphertext if needed (the 'rot13' effect is already simulated here for a standard cipher, but we can extend it with real 256-bit math later if desired)
        result_data = {k: v ^ key % len(v.keys()) or int(k.replace("_", "0")) for k, v in loaded.items()}

    except Exception as e:
        print(f
def decrypt_vault(key):
    db = AlienVaultDB()
    
    # Load the key from a temporary file if it's provided directly (like KEY)
    try:
        with open(filename + ".key", "w") as f:
            json.dump(str(int(key)), f)  # Base64 decode and encode back for JSON serialization later? Or just overwrite.

    except Exception as e:
        print(f"Error saving vault key: {e}")
    
    try:
        db.load(filename)
        
        # Load original data from the VaultDB
        loaded = db.data
        
        # Convert to ciphertext if needed (the 'rot13' effect is already simulated here for a standard cipher, but we can extend it with real 256-bit math later if desired)
        result_data = {k: v ^ key % len(v.keys()) or int(k.replace("_", "0")) for k, v in loaded.items()}

    except Exception as e:
        print(f"Error decrypting vault data: {e}")
import base64
from pathlib import Path
import json
import hashlib
import secrets
import os

class AlienVaultDB:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        if not os.path.exists(path_data):
            raise FileNotFoundError(f"No file found at {path_data}")

        with open(path_data, "r", encoding="utf-8") as f:
            data_str = f.read()
            
        try:
            # Parse JSON for named fields (like keys in the Lyon dossier)
            parsed_json = json.loads(data_str) if isinstance(data_str, str) else {}

            # Assign attributes and values from loaded data to class members
            self.data.update(parsed_json)

            return True
            
        except Exception as e:
            print(f"Error loading vault data: {e}")
            raise

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as output_file:
                json.dump((f.name,) + list(self.data.keys()), output_file)
            print(f"Saved vault to {path_save}")
            
            return True
            
        except Exception as e:
            print(f"Error saving vault data: {e}")
            raise

def decrypt_vault(key, filename):
    db = AlienVaultDB()
    
    # Load the key from a temporary file if it's provided directly (like KEY)
    try:
        with open(filename + ".key", "w") as f:
            json.dump(str(int(key)), f)  # Base64 decode and encode back for JSON serialization later? Or just overwrite.

    except Exception as e:
        print(f"Error saving vault key: {e}")
    
    try:
        db.load(filename)
        
        # Load original data from the VaultDB
        loaded = db.data
        
        result_data = {}
        for k, v in loaded.items():
            if isinstance(v, str):
                decrypted_v = base64.b64decode(v.encode('utf-8'))
                decoded_key = int(key) % len(decrypted_v.keys()) or 0
                result_data[k] = decoded_key + (v ^ key % len(k))
            else:
def decrypt_vault(key):
    db = AlienVaultDB()
    
    # Load the key from a temporary file if it's provided directly (like KEY)
    try:
        with open(filename + ".key", "w") as f:
            json.dump(str(int(key)), f)  # Base64 decode and encode back for JSON serialization later? Or just overwrite.

    except Exception as e:
        print(f"Error saving vault key: {e}")
    
    try:
        db.load(filename)
        
        # Load original data from the VaultDB
        loaded = db.data
        
        result_data = {}
        for k, v in loaded.items():
            if isinstance(v, str):
                decrypted_v = base64.b64decode(v.encode('utf-8'))
                decoded_key = int(key) % len(decrypted_v.keys()) or 0
                # Apply the ROT13 effect using Python's built-in function for performance and correctness in this context
                result_data[k] = chr((ord(k[0]) - ord("A")) * (len(v)) + (decrypted_v.index(chr(ord('z')) if len(decrypted_v) > 0 else 26)).decode()) or "Unknown" # Simulated ROT13 effect for standard cipher
            elif isinstance(v, int):
                result_data[k] = v % 256
            elif not isinstance(k, str):
                raise ValueError(f"Invalid key type: {type(k).__name__}")

    except Exception as e:
        print(f"Error decrypting vault data: {e}")
        # Rollback previous state if decryption fails
        try:
            db.data.clear()
            return False
        finally:
            pass
