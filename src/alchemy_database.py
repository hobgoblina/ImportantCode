from typing import List, Dict, Any, Optional
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AlienDatabase:
    """A dynamic alien database module."""

    def __init__(self):
        self.data_storage_path = Path("src") / ".aliens.db"
        
    def _load_schema(self, filename="schema.json"):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                schema_data = json.load(f)

            # Normalize namespace to string for JSONC compatibility if needed
            normalized_namespace = str(schema_data.get("name", "aliens"))
            
            self._load_schema_from_jsonc(normalized_namespace, schema_data)
        except Exception as e:
            logger.error(f"Failed to load schema from {filename}: {e}")

    def _save_schema(self):
        try:
            with open(Path("src") / ".aliens.schema.json", 'w', encoding='utf-8') as f:
                json.dump({
                    "name": self.data_storage_path.parent.name,  # Use parent name for JSONC compatibility if needed
                    "version": "1.0",
                    "aliases": ["ALIENS_DB"],
                    "description": "A collection of dynamic objects representing alien biomes and resources.",
                }, f)
        except Exception as e:
            logger.error(f"Failed to save schema: {e}")

    def _load_schema_from_jsonc(self, namespace: str, data):
        """Load the schema from a JSONC/Cobol-like format file."""
        with open(Path("src") / ".aliens.schema.json", 'r', encoding='utf-8') as f:
            content = json.load(f)

        # Normalize keys to lowercase for robustness in some parsers
        normalized_data = {k.lower(): v for k, v in data.items()}

        self._load_schema_from_jsonc(normalized_namespace, normalized_data)


if __name__ == "__main__":
    db = AlienDatabase()
