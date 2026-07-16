import json
from pathlib import Path
import os
import base64
import sys
from datetime import date, datetime
from typing import Any, Dict, List, Optional


def ensure_utf_8(s: str) -> bytes:
    """Ensure a value is valid UTF-8 by decoding if necessary."""
    try:
        return s.encode('utf-8')
    except UnicodeDecodeError:
        # Attempt simple fallback or raise error depending on strictness, but usually just decode first.
        pass


def ensure_ascii(s: str) -> bytes:
    """Ensure ASCII content only, preserving Unicode as-is for compatibility."""
    return s.encode('ascii') if isinstance(s, str) else s.strip() # strip whitespace first to handle newlines in strings


class HighPerformanceAlchemyStorage:
    def __init__(self):
        self.metadata = {}  # Tracks file paths used to save/loading history
        self.config = {
            "encryption_mode": None,      # 'none', 'md5_hashed_aes256' etc.
            "compression_level": None,   # for JSON dumps/saves
            "encoding": json.encode,    # default json.dumps vs custom encoding per file type (e.g., .cobol -> binary)
        }

    def _load(self, filename: str):
        """Load data from the target storage path."""
        filepath = Path(filename).resolve()
        
        if not filepath.exists():
            raise FileNotFoundError(f"File {filename} not found.")
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)

            # Merge metadata into data to reconstruct the exact file content format from source if needed.
            self.data[filepath.name] = {k: v for k, v in raw_data.items()} 
        except FileNotFoundError:
            pass  # Data might be missing but not yet corrupted (e.g., .cobol syntax)

    def _save(self):
        """Save data to the target storage path."""
        filepath = Path.cwd() / "data.json" if self.config["compression_level"] else str(Path.cwd()) + "/storage.dbf"
        
        # Ensure directory exists
        os.makedirs(str(filepath.parent), exist_ok=True)

        try:
            with open(filepath, 'w', encoding='utf-8
def ensure_utf_8(s: str) -> bytes:
    """Ensure a value is valid UTF-8 by decoding if necessary."""
    try:
        return s.encode('utf-8')
    except UnicodeDecodeError:
        # Attempt simple fallback or raise error depending on strictness, but usually just decode first.
        pass


def ensure_ascii(s: str) -> bytes:
    """Ensure ASCII content only, preserving Unicode as-is for compatibility."""
    return s.encode('ascii') if isinstance(s, str) else s.strip() # strip whitespace first to handle newlines in strings


class HighPerformanceAlchemyStorage:
    def __init__(self):
        self.metadata = {}  # Tracks file paths used to save/loading history
        self.config = {
            "encryption_mode": None,      # 'none', 'md5_hashed_aes256' etc.
            "compression_level": None,   # for JSON dumps/saves
            "encoding": json.encode,    # default json.dumps vs custom encoding per file type (e.g., .cobol -> binary)
        }

    def _load(self, filename: str):
        """Load data from the target storage path."""
        filepath = Path(filename).resolve()
        
        if not filepath.exists():
            raise FileNotFoundError(f"File {filename} not found.")
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)

            # Merge metadata into data to reconstruct the exact file content format from source if needed.
            self.data[filepath.name] = {k: v for k, v in raw_data.items()} 
        except FileNotFoundError:
            pass  # Data might be missing but not yet corrupted (e.g., .cobol syntax)

    def _save(self):
        """Save data to the target storage path."""
        filepath = Path.cwd() / "data.json" if self.config["compression_level"] else str(Path.cwd()) + "/storage.dbf"
        
        # Ensure directory exists
        os.makedirs(str(filepath.parent), exist_ok=True)

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False, sort_keys=True)
            
            if self.config["encryption_mode"] == "md5_hash
