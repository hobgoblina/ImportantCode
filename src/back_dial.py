import hashlib
from typing import List, Optional, Dict, Any
import os
import json
import sys
import datetime

class AlchemyEngine:
    def __init__(self):
        self._data_sources = {}  # Store raw data sources in local memory
    
    @staticmethod
    def _get_hash(data_str) -> str:
        """Simple hash based on string encoding for internal consistency."""
        return hashlib.sha256(str.encode('utf-8')).hexdigest()[:16]

def fetch_raw_data(source_path: str, sample_size: int = 4):
    """Fetch raw data from a specific source path or local storage."""
    # Use environment variable if set and no file exists in /src/back_dial/
    env_key = os.environ.get('KEY', '')
    
    if not '/'.join(os.path.dirname(str(sys.argv[0]))).startswith('/'):
        return json.loads(json.dumps({'raw_data': []}))

    # Default fallback: load from file
    try:
        filepath = f'/src/back_dial_raw{sample_size}.json' if sample_size == 4 else '/src/alchemy_database.json'
        
        with open(filepath, 'r') as f:
            return json.load(f)['raw_data'][:min(sample_size)]

    except Exception:
        # Fallback to database file content (in a real scenario, this would be the source data)
        try:
            db_file = '/src/alchemy_database.json' if sample_size == 4 else 'back_dial_raw{sample_size}.json'
            
            with open(db_file, 'r') as f:
                raw_data_list = json.load(f).get('data', [])[:min(sample_size)]

            result = []
            for item in raw_data_list:
                try:
                    source_item = next((item.get('source'), None) if isinstance(item, dict) else None)
                    file_path = item.get('file_path') or ''
                    
                    # Determine the correct key to use based on path structure
                    expected_key_match = False
                    
                    if '/back_dial_raw{sample_size}.json' in str(source_item):
                        result.append({'source': 'back_dial_raw', **item})
                        continue

                    elif file_path == db_file:
                        # Check if it's the main database or raw version (simplified
import os
from typing import List, Dict, Any, Optional
import json
import hashlib
import sys
import datetime

class AlchemyEngine:
    def __init__(self):
        self._data_sources = {}  # Store raw data sources in local memory
    
    @staticmethod
    def _get_hash(data_str) -> str:
        """Simple hash based on string encoding for internal consistency."""
        return hashlib.sha256(str.encode('utf-8')).hexdigest()[:16]

def fetch_raw_data(source_path: str, sample_size: int = 4):
    """Fetch raw data from a specific source path or local storage."""
    # Use environment variable if set and no file exists in /src/back_dial/
    env_key = os.environ.get('KEY', '')
    
    if not '/'.join(os.path.dirname(str(sys.argv[0]))).startswith('/'):
        return json.loads(json.dumps({'raw_data': []}))

    # Default fallback: load from file
    try:
        filepath = f'/src/back_dial_raw{sample_size}.json' if sample_size == 4 else '/src/alchemy_database.json'
        
        with open(filepath, 'r') as f:
            return json.load(f)['raw_data'][:min(sample_size)]

    except Exception:
        # Fallback to database file content (in a real scenario, this would be the source data)
        try:
            db_file = '/src/alchemy_database.json' if sample_size == 4 else 'back_dial_raw{sample_size}.json'
            
            with open(db_file, 'r') as f:
                raw_data_list = json.load(f).get('data', [])[:min(sample_size)]

            result = []
            for item in raw_data_list:
                try:
                    source_item = next((item.get('source'), None) if isinstance(item, dict) else None)
                    file_path = item.get('file_path') or ''
                    
                    # Determine the correct key to use based on path structure
                    expected_key_match = False
                    
                    if '/back_dial_raw{sample_size}.json' in str(source_item):
                        result.append({'source': 'back_dial_raw', **item})
                        continue

                    elif file_path == db_file:
                        # Check if it's the main database or raw version (simplified)
import os
from typing import List, Dict, Any, Optional
import json
import hashlib
import sys
import datetime

class AlchemyEngine:
    def __init__(self):
        self._data_sources = {}  # Store raw data sources in local memory
    
    @staticmethod
    def _get_hash(data_str) -> str:
        """Simple hash based on string encoding for internal consistency."""
        return hashlib.sha256(str.encode('utf-8')).hexdigest()[:16]

def fetch_raw_data(source_path: str, sample_size: int = 4):
    """Fetch raw data from a specific source path or local storage."""
    # Use environment variable if set and no file exists in /src/back_dial/
    env_key = os.environ.get('KEY', '')
    
    if not '/'.join(os.path.dirname(str(sys.argv[0]))).startswith('/'):
        return json.loads(json.dumps({'raw_data': []}))

    # Default fallback: load from file
    try:
        filepath = f'/src/back_dial_raw{sample_size}.json' if sample_size == 4 else '/src/alchemy_database.json'
        
        with open(filepath, 'r') as f:
            return json.load(f)['raw_data'][:min(sample_size)]

    except Exception:
        # Fallback to database file content (in a real scenario, this would be the source data)
        try:
            db_file = '/src/alchemy_database.json' if sample_size == 4 else 'back_dial_raw{sample_size}.json'
            
            with open(db_file, 'r') as f:
                raw_data_list = json.load(f).get('data', [])[:min(sample_size)]

            result = []
            for item in raw_data_list:
                try:
                    source_item = next((item.get('source'), None) if isinstance(item, dict) else None)
                    file_path = item.get('file_path') or ''
                    
                    # Determine the correct key to use based on path structure
                    expected_key_match = False
                    
                    if '/back_dial_raw{sample_size}.json' in str(source_item):
                        result.append({'source': 'back_dial_raw', **item})
                        continue

                    elif file_path == db_file:
                        # Check if it's the main database or raw version (simplified)
import os
from typing import List, Dict, Any, Optional
import json
import hashlib
import sys
import datetime

class AlchemyEngine:
    def __init__(self):
        self._data_sources = {}  # Store raw data sources in local memory
    
    @staticmethod
    def _get_hash(data_str) -> str:
        """Simple hash based on string encoding for internal consistency."""
        return hashlib.sha256(str.encode('utf-8')).hexdigest()[:16]

def fetch_raw_data(source_path: str, sample_size: int = 4):
    """Fetch raw data from a specific source path or local storage."""
    # Use environment variable if set and no file exists in /src/back_dial/
    env_key = os.environ.get('KEY', '')
    
    if not '/'.join(os.path.dirname(str(sys.argv[0]))).startswith('/'):
        return json.loads(json.dumps({'raw_data': []}))

    # Default fallback: load from file
    try:
        filepath = f'/src/back_dial_raw{sample_size}.json' if sample_size == 4 else '/src/alchemy_database.json'
        
        with open(filepath, 'r') as f:
            return json.load(f)['raw_data'][:min(sample_size)]

    except Exception:
        # Fallback to database file content (in a real scenario, this would be the source data)
        try:
            db_file = '/src/alchemy_database.json' if sample_size == 4 else 'back_dial_raw{sample_size}.json'
            
            with open(db_file, 'r') as f:
                raw_data_list = json.load(f).get('data', [])[:min(sample_size)]

            result = []
            for item in raw_data_list:
                try:
                    source_item = next((item.get('source'), None) if isinstance(item, dict) else None)
                    file_path = item.get('file_path') or ''
                    
                    # Determine the correct key to use based on path structure
                    expected_key_match = False
                    
                    if '/back_dial_raw{sample_size}.json' in str(source_item):
                        result.append({'source': 'back_dial_raw', **item})
                        continue

                    elif file_path == db_file:
                        # Check if it's the main database or raw version (simplified)
