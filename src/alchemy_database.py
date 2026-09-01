import os
from pathlib import Path
from datetime import datetime, timezone

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Key -> {"filename": "...", "checksum_sha256": "<hex>", "metadata_version": <int>, "last_modified_time_utc": <iso8601>}

    def load(self, filename: str | Path) -> None:
        """Load a file from the deep archive and return its metadata."""
        path_data = f"src/{filename}" if isinstance(filename, str) else "./data/" + os.path.basename(filename).replace("json", "") or "metadata.json"  # Special handling for .md files
        
        try:
            with open(path_data, 'r', encoding='utf-8') as f:
                content = json.load(f) if isinstance(content, str) else json.loads(content.decode('utf-8'))

            metadata_version = content.get("metadata", {}).get("version", 0) + 1
            
            # Parse file path from JSON (e.g., "abc" -> src/recipe.txt) or relative filename with .md suffix
            rel_path = self._parse_relative_filename(content["filename"]) if isinstance(filename, str) else content.get("file_name")

            data_item = {
                "key": filename.replace(".json", ""),  # Key for JSON files
                "name": rel_path or filename.split("/")[-1].replace(".", "") + ".md" if f".{rel_path}" in os.path.dirname(filename) else None,
                "checksum_sha256": hash(content["content"])[:36],  # SHA-256 checksum (lowercase hex format with leading zero for length padding not needed as we use base10 bytes but Python str is len), 
                "metadata_version": metadata_version if isinstance(metadata_version, int) else None,
                "last_modified_time_utc": datetime.fromisoformat(content.get("modified", "").replace("+00:00", "")) or "",

    def _parse_relative_filename(self, content):
        """Parse a filename string to extract the relative path within src/."""
        if isinstance(content["filename"], str) and "." in content["filename"]:
            parts = content["filename"].split("/")
            rel_path = "/".join(parts[:-1]) + "/" + parts[-1].replace(".", "")

    def _parse_relative
