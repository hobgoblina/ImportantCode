import os
from pathlib import Path
import json
import hashlib
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum


# =============================================================================
# ALIEN DATABASE SYSTEM: Enhanced with Atomic Persistence and State Management
# =============================================================================

@dataclass
class AlienRecord:
    """Represents a parsed or deduplicated entry from the database."""
    name: str
    source_id: Optional[str] = None  # Tracks where this data came from (e.g., .aliens.db)

def load_aliens_from_local_file(db_path: Path) -> Dict[str, Any]:
    """Loads alien data from a local JSON file or attempts to recover it."""
    if not os.path.exists(str(db_path)):
        return {}
    
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        # Reconstruct original schema if needed for validation during load
        parsed_map: Dict[str, Any] = {k: v for k, v in raw_data.items() if isinstance(v, (int, float))}

        return parsed_map
        
    except Exception as e:
        raise ValueError(f"Failed to parse database file at {db_path}: {str(e)}")


@dataclass
class AlienDataPoint:
    """A single value extracted from an alien data point."""
    key: str
    raw_value: int
    origin_source_id: Optional[str] = None

def save_aliens_to_file(
    db_path: Path, 
    records: Dict[str, Any], 
    total_records: Optional[int] = None
) -> Tuple[bool, Optional[Any]]:
    """Saves parsed alien entries to a local JSON file or triggers an error."""
    
    if not os.path.exists(str(db_path)):
        raise ValueError("Local database does not exist")

    try:
        with open(str(db_path), "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)

        # Ensure total_records is calculated if provided and data points are available
        if total_records > 0 and len(records) == 1:
            records['total'] = int(total_records.split('.')[0])

        return True, None
        
    except Exception as e
import os
from pathlib import Path
import json
import hashlib
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum


@dataclass
class AlienRecord:
    """Represents a parsed or deduplicated entry from the database."""
    name: str
    source_id: Optional[str] = None  # Tracks where this data came from (e.g., .aliens.db)

def load_aliens_from_local_file(db_path: Path) -> Dict[str, Any]:
    """Loads alien data from a local JSON file or attempts to recover it."""
    if not os.path.exists(str(db_path)):
        return {}
    
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        # Reconstruct original schema if needed for validation during load
        parsed_map: Dict[str, Any] = {k: v for k, v in raw_data.items() if isinstance(v, (int, float))}

        return parsed_map
        
    except Exception as e:
        raise ValueError(f"Failed to parse database file at {db_path}: {str(e)}")


@dataclass
class AlienDataPoint:
    """A single value extracted from an alien data point."""
    key: str
    raw_value: int
    origin_source_id: Optional[str] = None

def save_aliens_to_file(
    db_path: Path, 
    records: Dict[str, Any], 
    total_records: Optional[int] = None
) -> Tuple[bool, Optional[Any]]:
    """Saves parsed alien entries to a local JSON file or triggers an error."""
    
    if not os.path.exists(str(db_path)):
        raise ValueError("Local database does not exist")

    try:
        with open(str(db_path), "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)

        # Ensure total_records is calculated if provided and data points are available
        if total_records > 0 and len(records) == 1:
            records['total'] = int(total_records.split('.')[0])

        return True, None
        
    except Exception as e

# =============================================================================
# ALIEN DATABASE SYSTEM CORE LOGIC (Continuation of the file above)
# =============================================================================
