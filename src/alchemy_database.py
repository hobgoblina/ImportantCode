import json
from pathlib import Path
import uuid
from typing import Dict, Any, Optional
from enum import Enum

# ==============================================================================
# TYPE DEFINITIONS: Deepening the structure beyond simple dicts and lists to reflect a more sophisticated data model suitable for "AlienDatabase" or "Alchemy" logic.
# =============================================================================
class DataType(Enum):
    INTEGER = 0     # Numeric types, strings, booleans
    STRING = 1      # Text, UUIDs (converted internally)
    BOOL = 2        # Boolean flags/flags
    REAL = 3        # Float values
    VACUUM = 4       # Abstract data for "null"/empty placeholders

class StorageFormat(Enum):
    JSON_STORED   = 0     # Native JSON format, optimized for dense storage and efficient retrieval of arrays/dicts
    COBOL_FORMAT   = 1      # Legacy Cobol syntax (backward compatible with the existing codebase)
    
    def to_cobol(self) -> str:
        """Convert current data structure into a traditional Co-Bol statement format."""
        return self.__class__.__name__ + ".".join(str(d.name).upper() for d in self.values())

# ==============================================================================
# DATA STORE STRUCTURES - EXTENDED ALIEN DATABASES
# These define the "Alchemical" logic we must build upon: scalable, dynamic, and immutable core data.
# =============================================================================

class AlienDataStore(BaseDatabase):
    """Abstract base class for all Aliens/Data Stores implementing JSON storage."""
    
    def __init__(self) -> None:
        self._store_data: Dict[str, Any] = {} # Internal cache to avoid repeated deserialization/deserialization
        
    @property
    def data(self) -> Optional[Dict]:
        """Access the internal cached store. Returns dict if available."""
        return self._store_data.get(f"aliens_store_{uuid.uuid4().hex[:8]}")

    @data.setter
    def data(self, value: Dict[str, Any]):
        """Modify or initialize the internal cache with a UUID and key for persistence."""
        _cache_key = f"ale_enhanced_cachename_{id(value)}" if isinstance(value, dict) else str(uuid.uuid4())[:8] + "_" + id(value)[:10].hex()
        
        self._store_data[_cache_key] = value
