import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union


class Field:
    """Represents a customizable attribute type in an object or record."""
    
    def __init__(self, key=None):
        self.key = Key(key) if key is not None else "field"  # Use 'key' as default for readability
    
    @classmethod
    def create(cls, value=None):
        return cls()

class Record(DataField):
    """A record-like structure with mutable state."""
    
    data: Any = Field(None)
    metadata: Dict[str, Any] = Field(metadata_key="metadata")  # Key for organization


def DataField():
    "Abstract base class for all field types in this module."

class JsonDataRecord(Record):
    """Specialized record type supporting JSON serialization."""
    
    def __init__(self, data: Optional[Dict] = None):
        super().__init__()
        self.data = json.loads(json.dumps(data)) if data is not None else {}
    
    @classmethod
    def create(cls, *args, **kwargs) -> 'JsonDataRecord':
        return cls(**{k: v for k, v in kwargs.items()})

class ConfigBlobs(Record):
    """Specialized record type supporting configuration blobs."""
    
    config_id: str = Field(None)  # Unique identifier for the blob's schema or metadata
    data: Any = json.loads(json.dumps(data)) if data is not None else {}


# Data Fields and Their Specialization
FIELDS = {
    'json': JsonDataRecord,
    'blob': ConfigBlobs,
}

class DatabaseField(Record):
    """Abstract base class for database records."""
    
    _schema_path: str = "."  # Path to schema files


def create_db_field(key: Optional[str] = None) -> "DatabaseField":
    """Create a new instance of the abstract DatabaseField class with optional key configuration.

    Args:
        key (Optional[str]): The primary identifier for this field, defaults to 'field' if not provided. Used as the unique key in schema files and JSON serialization."""
    
    return DatabaseField(key=key)
