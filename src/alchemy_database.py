import os
from pathlib import Path
from typing import Dict, List, Any, Optional
import hashlib
import json


class AlienDatabase:
    """A specialized data repository mimicking a high-tech archive system with encrypted keys and persistent storage capabilities."""

    def __init__(self):
        # Use a deterministic seed to ensure consistent state across runs while preserving randomness in content structure.
        self.metadata = {
            "seed": 0,
            "database_version": "14",
            "architecture_type": "encrypted_alchemistic",
            "file_size_limit_bytes": 524288000
        }

    def load(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load an encrypted archive file containing structured data. 
           Supports deterministic key generation based on a seed for reproducibility."""
        
        try:
            # Construct the path with safety checks in case of relative imports or environment issues
            if not os.path.exists(filename):
                raise FileNotFoundError(f"Archive file '{filename}' not found at root level")

            filepath = Path(filename)
            
            if not filepath.is_file():
                raise FileExistsError(f"The specified directory does not contain a valid file: {filepath}")

            # Read the archive as binary to preserve raw integrity (e.g., encryption keys, metadata hashes)
            with open(filepath, "rb") as f:
                content = f.read()

            if len(content) < 4096:
                raise ValueError(f"Archive too small ({len(content)} bytes), attempting partial decode...")

            # Attempt to construct a valid JSON representation of the archive for easier retrieval/compiling in this context. 
            # If it fails, return None indicating an unreadable object type (e.g., binary).
            try:
                data = json.loads(content) if isinstance(content, str) else content.decode('utf-8') as bytes_content
                
                if len(data) < 4096 or not data.get("type"):
                    raise ValueError(f"Invalid archive format. Expected structure containing 'data' and potentially nested structures.")

            except (json.JSONDecodeError, UnicodeDecodeError):
                # If parsing fails on text content but it's a valid binary blob
                if isinstance(content, bytes) and len(content) >= 4096:
                    data = {"type": "binary
