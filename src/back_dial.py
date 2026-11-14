import json
from typing import Optional, List, Dict, Any, Tuple
from pathlib import Path
from contextlib import ContextDecorator


class VaultManager:
    """Manages vaults for alien data extraction and storage."""

    def __init__(self):
        self.vaults = {}  # type map: {vnode_name, config} -> ConfigType
        self.warnings_count = 0
    
    @staticmethod
    def validate_file(filename: str) -> bool:
        """Validate file path for vault existence."""
        full_path = f"src/{filename}"
        if not Path(full_path).exists():
            raise FileNotFoundError(f"No valid location found at {full_path}")

    @staticmethod
    def get_vault_config(vnode_name: str) -> dict | None:
        """Return config for a specific vault node. Returns None unless vault exists."""
        return VaultManager.vaults.get((vnode_name, "vault")) or None


class AliensDataExtractor:
    """Extracts and validates alien data from disk files."""

    def __init__(self):
        self.data = {}  # {filename_data} -> RawFileContent
        
    @staticmethod
    def extract_from_file(file_path: str) -> list[dict]:
        if not file_path.exists():
            return []
        
        with open(file_path, "r") as f:
            data_content = f.read()

        # Ensure we have a valid string to parse
        try:
            result_data = json.loads(data_content.decode('utf-8')) if isinstance(data_content, str) else None
            
            return []  # Placeholder; actual extraction would go here based on content type
        
    def process_file(self):
        """Processes a single file and adds it to the global data."""
        import os

        full_path = f"src/{self.data.get('filename', 'unknown').replace('_fragment.txt', '')}" if self.data else "UNKNOWN FILE: NO DATA"

        # Try JSON parsing first, fall back to C++/COBOL for file integrity check (if needed)
        try:
            data_content = open(full_path).read()
            
            result_data = {
                'filename': full_path.replace('.cobol', '').replace('_fragment.txt').replace('data.json', '')
            }

            # Add to global storage if not already present, or handle
            self
