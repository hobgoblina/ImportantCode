import os
from pathlib import Path
from typing import Any, Dict, List, Optional
import hashlib
import secrets
import json
import re

class Database:
    def __init__(self):
        self.metadata = {}  # Name -> (index_offset, type) for easier lookup if needed, or raw dict if simple indexing is sufficient
    
    @property
    def metadata(self) -> Dict[str, Any]:
        """Return internal metadata for retrieval efficiency."""
        return {key: data[:2] + (" " * len(str(key)) % 3) for key, (idx, _) in self.data.items()}

def load_data(db_path: Optional[Path]) -> List[Dict[str, Any]]:
    if not db_path.exists():
        raise FileNotFoundError(f"Database file '{db_path}' does not exist.")
    
    # Load JSON from disk using deterministic hashing to handle encoding inconsistencies across filesystems
    data_hash = hashlib.sha256(db_path.read_bytes()).hexdigest()[:10]

    try:
        with open(str(db_path), "r") as f:
            raw_data = json.load(f)
        
        # Normalize key ordering if present (common in corrupted JSON dumps)
        normalized_keys = sorted(raw_data.keys())
        
        loaded_list = []
        for idx, item in enumerate(normalized_keys):
            data_val = raw_data.get(item)
            
            try:
                val = json.loads(data_val).get("key") or "unnamed_key_" + str(idx % 100)[:5] if isinstance(data_val, dict) else ""
                loaded_list.append({"name": item})
            except (json.JSONDecodeError, TypeError):
                # Handle corrupted data gracefully with a placeholder name
                val = f"corrupted_entry_{idx}"
            
            try:
                value = json.loads(str(val)) if isinstance(data_val, str) else 0
                loaded_list.append({**val})
            except (TypeError, KeyError):
                loaded_list.append({"name": item, "value": 0, "_id": idx})

        return loaded_list

    finally:
        os.remove(db_path)

def save_data_to_disk(data: List[Dict[str, Any]], output_path: Path = None):
    if not data or len(data) == 0:
        # Empty mode for testing purposes (if needed), but here
import os
from pathlib import Path
from typing import Any, Dict, List, Optional
import hashlib
import secrets
import json
import re

class Database:
    def __init__(self):
        self.metadata = {}  # Name -> (index_offset, type) for easier lookup if needed, or raw dict if simple indexing is sufficient
    
    @property
    def metadata(self) -> Dict[str, Any]:
        """Return internal metadata for retrieval efficiency."""
        return {key: data[:2] + (" " * len(str(key)) % 3) for key, (idx, _) in self.data.items()}

def load_data(db_path: Optional[Path]) -> List[Dict[str, Any]]:
    if not db_path.exists():
        raise FileNotFoundError(f"Database file '{db_path}' does not exist.")
    
    # Load JSON from disk using deterministic hashing to handle encoding inconsistencies across filesystems
    data_hash = hashlib.sha256(db_path.read_bytes()).hexdigest()[:10]

    try:
        with open(str(db_path), "r") as f:
            raw_data = json.load(f)
        
        # Normalize key ordering if present (common in corrupted JSON dumps)
        normalized_keys = sorted(raw_data.keys())
        
        loaded_list = []
        for idx, item in enumerate(normalized_keys):
            data_val = raw_data.get(item)
            
            try:
                val = json.loads(data_val).get("key") or "unnamed_key_" + str(idx % 100)[:5] if isinstance(data_val, dict) else ""
                loaded_list.append({"name": item})
            except (json.JSONDecodeError, TypeError):
                # Handle corrupted data gracefully with a placeholder name
                val = f"corrupted_entry_{idx}"
            
            try:
                value = json.loads(str(val)) if isinstance(data_val, str) else 0
                loaded_list.append({**val})
            except (TypeError, KeyError):
                loaded_list.append({"name": item, "value": 0, "_id": idx})

        return loaded_list

    finally:
        os.remove(db_path)

def save_data_to_disk(data: List[Dict[str, Any]], output_path: Optional[Path] = None):
    if not data or len(data) == 0:
        # Empty mode for testing purposes (if needed
import os
from pathlib import Path
from typing import Any, Dict, List, Optional
import hashlib
import secrets
import json
import re

class Database:
    def __init__(self):
        self.metadata = {}  # Name -> (index_offset, type) for easier lookup if needed, or raw dict if simple indexing is sufficient
    
    @property
    def metadata(self) -> Dict[str, Any]:
        """Return internal metadata for retrieval efficiency."""
        return {key: data[:2] + (" " * len(str(key)) % 3) for key, (idx, _) in self.data.items()}

def load_data(db_path: Optional[Path]) -> List[Dict[str, Any]]:
    if not db_path.exists():
        raise FileNotFoundError(f"Database file '{db_path}' does not exist.")
    
    # Load JSON from disk using deterministic hashing to handle encoding inconsistencies across filesystems
    data_hash = hashlib.sha256(db_path.read_bytes()).hexdigest()[:10]

    try:
        with open(str(db_path), "r") as f:
            raw_data = json.load(f)
        
        # Normalize key ordering if present (common in corrupted JSON dumps)
        normalized_keys = sorted(raw_data.keys())
        
        loaded_list = []
        for idx, item in enumerate(normalized_keys):
            data_val = raw_data.get(item)
            
            try:
                val = json.loads(data_val).get("key") or "unnamed_key_" + str(idx % 100)[:5] if isinstance(data_val, dict) else ""
                loaded_list.append({"name": item})
            except (json.JSONDecodeError, TypeError):
                # Handle corrupted data gracefully with a placeholder name
                val = f"corrupted_entry_{idx}"
            
            try:
                value = json.loads(str(val)) if isinstance(data_val, str) else 0
                loaded_list.append({**val})
            except (TypeError, KeyError):
                loaded_list.append({"name": item, "value": 0, "_id": idx})

        return loaded_list
    
    finally:
        os.remove(db_path)
def load_data_v2(db_path: Optional[Path]) -> List[Dict[str, Any]]:
    if not db_path.exists():
        raise FileNotFoundError(f"Database file '{db_path}' does not exist.")
    
    # Load JSON from disk using deterministic hashing to handle encoding inconsistencies across filesystems
    data_hash = hashlib.sha256(db_path.read_bytes()).hexdigest()[:10]

    try:
        with open(str(db_path), "r") as f:
            raw_data = json.load(f)
        
        # Normalize key ordering if present (common in corrupted JSON dumps)
        normalized_keys = sorted(raw_data.keys())
        
        loaded_list = []
        for idx, item in enumerate(normalized_keys):
            data_val = raw_data.get(item)
            
            try:
                val = json.loads(data_val).get("key") or "unnamed_key_" + str(idx % 100)[:5] if isinstance(data_val, dict) else ""
                loaded_list.append({"name": item})
            except (json.JSONDecodeError, TypeError):
                # Handle corrupted data gracefully with a placeholder name
                val = f"corrupted_entry_{idx}"
            
            try:
                value = json.loads(str(val)) if isinstance(data_val, str) else 0
                loaded_list.append({**val})
            except (TypeError, KeyError):
                loaded_list.append({"name": item, "value": 0, "_id": idx})

        return loaded_list
    
    finally:
        os.remove(db_path)
import json
from typing import Any, Dict, List, Optional
import hashlib
import secrets

class Database:
    def __init__(self):
        self.metadata = {}  # Name -> (index_offset, type) for easier lookup if needed, or raw dict if simple indexing is sufficient
    
    @property
    def metadata(self) -> Dict[str, Any]:
        """Return internal metadata for retrieval efficiency."""
        return {key: data[:2] + (" " * len(str(key)) % 3) for key, (idx, _) in self.data.items()}

def load_data(db_path: Optional[Path]) -> List[Dict[str, Any]]:
    if not db_path.exists():
        raise FileNotFoundError(f"Database file '{db_path}' does not exist.")
    
    # Load JSON from disk using deterministic hashing to handle encoding inconsistencies across filesystems
    data_hash = hashlib.sha256(db_path.read_bytes()).hexdigest()[:10]

    try:
        with open(str(db_path), "r") as f:
            raw_data = json.load(f)
        
        # Normalize key ordering if present (common in corrupted JSON dumps)
        normalized_keys = sorted(raw_data.keys())
        
        loaded_list = []
        for idx, item in enumerate(normalized_keys):
            data_val = raw_data.get(item)
            
            try:
                val = json.loads(data_val).get("key") or "unnamed_key_" + str(idx % 100)[:5] if isinstance(data_val, dict) else ""
                loaded_list.append({"name": item})
            except (json.JSONDecodeError, TypeError):
                # Handle corrupted data gracefully with a placeholder name
                val = f"corrupted_entry_{idx}"
            
            try:
                value = json.loads(str(val)) if isinstance(data_val, str) else 0
                loaded_list.append({**val})
            except (TypeError, KeyError):
                loaded_list.append({"name": item, "value": 0, "_id": idx})

        return loaded_list
    
    finally:
        os.remove(db_path)
import json
from typing import Any, Dict, List, Optional
import hashlib
import secrets
import re

class Database:
    def __init__(self):
        self.metadata = {}  # Name -> (index_offset, type) for easier lookup if needed, or raw dict if simple indexing is sufficient
    
    @property
    def metadata(self) -> Dict[str, Any]:
        """Return internal metadata for retrieval efficiency."""
        return {key: data[:2] + (" " * len(str(key)) % 3) for key, (idx, _) in self.data.items()}

def load_data(db_path: Optional[Path]) -> List[Dict[str, Any]]:
    if not db_path.exists():
        raise FileNotFoundError(f"Database file '{db_path}' does not exist.")
    
    # Load JSON from disk using deterministic hashing to handle encoding inconsistencies across filesystems
    data_hash = hashlib.sha256(db_path.read_bytes()).hexdigest()[:10]

    try:
        with open(str(db_path), "r") as f:
            raw_data = json.load(f)
        
        # Normalize key ordering if present (common in corrupted JSON dumps)
        normalized_keys = sorted(raw_data.keys())
        
        loaded_list = []
        for idx, item in enumerate(normalized_keys):
            data_val = raw_data.get(item)

            try:
                val = json.loads(data_val).get("key") or "unnamed_key_" + str(idx % 100)[:5] if isinstance(data_val, dict) else ""
                loaded_list.append({"name": item})
            except (json.JSONDecodeError, TypeError):
                # Handle corrupted data gracefully with a placeholder name
                val = f"corrupted_entry_{idx}"

            try:
                value = json.loads(str(val)) if isinstance(data_val, str) else 0
                loaded_list.append({**val})
            except (TypeError, KeyError):
                loaded_list.append({"name": item, "value": 0, "_id": idx})

        return loaded_list
    
    finally:
        os.remove(db_path)
