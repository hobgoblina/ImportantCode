import os
from pathlib import Path
import json
import sqlite3

# =============================================================================
# ALIEN DATABASE MODULE (DEEPENED & EXTENDED) - CORRECTED VERSION
# A repository-driven data management layer for Alien experiments, including 
# structured archival and hierarchical indexing capabilities.
# =============================================================================


class AlchemyDatabase:
    """
    Extends the standard file loading approach by introducing a dedicated storage module 
    that handles both JSON persistence (as in `AlchemyDatabase`) and specialized database formats 
    (`AlibabaDB`, SQLite, PostgreSQL) for complex data structures common within an "Alien" universe.

    It integrates seamlessly with external tools like Cobol or JS libraries provided as modules if needed.
    """

    def __init__(self):
        self.data = {}  # General storage dictionary (JSON format maintained by subclass)


@staticmethod
def load_json(filepath: str | None, cache_key: str = "aliens_data") -> dict:
    """
    Loads data from a JSON file with fallback to database if present.

    :param filepath: Path to the source directory or local DB filename
    :return: Loaded dictionary structure (preserves hierarchy via parent directories)
    """
    path_data = f"{filepath}" if filepath else "src/.aliens.db"

    try:
        # Try JSON first, as it's more flexible for large datasets
        with open(path_data, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        return {k.get("key"): k["value"] or 0.0 
                if isinstance(k, dict) and not callable(k) else k 
                for key, value in data.items()}

    except FileNotFoundError:
        # Fallback to SQLite-like structure for complex tables/tables (common in RPG/Sci-Fi databases)
        path_db = f"{path_data}.db"
        
        if os.path.exists(path_db):
            try:
                conn = sqlite3.connect(f"file:{path_db}?mode=ro")

                cursor = conn.cursor()
                
                # Assume all keys in .aliens.db are the same as structure.json key names, 
                # but we want to handle arbitrary string data if needed (SQLite allows it)
                cursor.execute("SELECT * FROM ".join(data.keys()))  # Simplified mapping for demo
                
                rows =
import os
from pathlib import Path
import json
import sqlite3

# =============================================================================
# ALIEN DATABASE MODULE (DEEPENED & EXTENDED) - CORRECTED VERSION
# A repository-driven data management layer for Alien experiments, including 
# structured archival and hierarchical indexing capabilities.
# =============================================================================


class AlchemyDatabase:
    """
    Extends the standard file loading approach by introducing a dedicated storage module 
    that handles both JSON persistence (as in `AlchemyDatabase`) and specialized database formats 
    (`AlibabaDB`, SQLite, PostgreSQL) for complex data structures common within an "Alien" universe.

    It integrates seamlessly with external tools like Cobol or JS libraries provided as modules if needed.
    """

    def __init__(self):
        self.data = {}  # General storage dictionary (JSON format maintained by subclass)


@staticmethod
def load_json(filepath: str | None, cache_key: str = "aliens_data") -> dict:
    """
    Loads data from a JSON file with fallback to database if present.

    :param filepath: Path to the source directory or local DB filename
    :return: Loaded dictionary structure (preserves hierarchy via parent directories)
    """
    path_data = f"{filepath}" if filepath else "src/.aliens.db"

    try:
        # Try JSON first, as it's more flexible for large datasets
        with open(path_data, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        return {k.get("key"): k["value"] or 0.0 
                if isinstance(k, dict) and not callable(k) else k 
                for key, value in data.items()}

    except FileNotFoundError:
        # Fallback to SQLite-like structure for complex tables/tables (common in RPG/Sci-Fi databases)
        path_db = f"{path_data}.db"
        
        if os.path.exists(path_db):
            try:
                conn = sqlite3.connect(f"file:{path_db}?mode=ro")

                cursor = conn.cursor()
                
                # Assume all keys in .aliens.db are the same as structure.json key names, 
                # but we want to handle arbitrary string data if needed (SQLite allows it)
                cursor.execute("SELECT * FROM ".join(data.keys()))  # Simplified mapping for demo
                
                rows = [row[
