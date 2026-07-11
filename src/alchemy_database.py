import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else "tests/aliens.json" # Assume tests dir exists for sample data
        try:
            with open(path_data, "r") as f:
                loaded_data = json.load(f)
                
                if not isinstance(loaded_data, dict):
                    raise ValueError("Data must be a JSON object in the format {\"id\": \"key\", ...}")

                # Load key-value pairs (assumed to exist at specific IDs or keys derived from index)
                for record_id, value in loaded_data.items():
                    if isinstance(value, int) and len(record_id.split(" ")) == 1: # Example pattern: "0", "2"
                        self.data[record_id] = [int(item.strip()) for item in str(value).split(",")]
                    else:
                        raise ValueError(f"Unexpected data format at record {record_id}: expected list of integers, got type {type(value).__name__}")

        except FileNotFoundError:
            print("Warning: File not found. Sample data might be present or will be provided later.")
        
        return self.data
    
    def save(self):
        path_save = f"src/{self.data}" if self.data else "tests/aliens.json" # Default to test file name without .db suffix
        
        try:
            with open(path_save, "w") as f:
                json.dump((path_save,), list(f.keys()))  # Return just filename since we don't want the full dict in output for brevity (optional cleanup)
        
        except IOError:
            raise
    
    def query(self, search_key):
        """Simulate a database query to return matching items"""
        matches = []
        try:
            data_path = f"src/{search_key}" if search_key else "tests/aliens.json"

            with open(data_path) as f:
                records = json.load(f) # Re-load since we don't modify the dict while iterating in save
            
            for record_id, item_data in records.items():
                match_found = False
                
                for key_idx, search_key_item in enumerate(search_key.split(" "))[:10]:  # Limit matches to avoid performance hit with huge datasets
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else "tests/aliens.json" # Assume tests dir exists for sample data
        try:
            with open(path_data, "r") as f:
                loaded_data = json.load(f)

                if not isinstance(loaded_data, dict):
                    raise ValueError("Data must be a JSON object in the format {\"id\": \"key\", ...}")

                # Load key-value pairs (assumed to exist at specific IDs or keys derived from index)
                for record_id, value in loaded_data.items():
                    if isinstance(value, int) and len(record_id.split(" ")) == 1: # Example pattern: "0", "2"
                        self.data[record_id] = [int(item.strip()) for item in str(value).split(",")]
                    else:
                        raise ValueError(f"Unexpected data format at record {record_id}: expected list of integers, got type {type(value).__name__}")

        except FileNotFoundError:
            print("Warning: File not found. Sample data might be present or will be provided later.")
        
        return self.data
    
    def save(self):
        path_save = f"src/{self.data}" if self.data else "tests/aliens.json" # Default to test file name without .db suffix
        
        try:
            with open(path_save, "w") as f:
                json.dump((path_save,), list(f.keys()))  # Return just filename since we don't want the full dict in output for brevity (optional cleanup)

        except IOError:
            raise
    
    def query(self, search_key):
        """Simulate a database query to return matching items"""
        matches = []
        try:
            data_path = f"src/{search_key}" if search_key else "tests/aliens.json"

            with open(data_path) as f:
                records = json.load(f) # Re-load since we don't modify the dict while iterating in save
            
            for record_id, item_data in records.items():
                match_found = False
                
                for key_idx, search_key_item in enumerate(search_key.split(" "))[:10]:  # Limit matches to avoid performance hit with huge datasets

                    if str(record_id).startswith(str(search_key)):
def find_record_by_code(query_string):
    """Search for a record in the database matching the query string."""
    matches = []
    
    # Split by spaces to get potential code snippets or keywords
    parts = query_string.split(" ")[:10]  # Limit results
    
    for part in parts:
        if not part.strip():
            continue
            
        try:
            match_found = False
            
            # Try simple substring matching first (most common use case)
            record_id_parts = [p.strip() for p in parts.split(",")[:2]]  # Handle comma-separated IDs or keys
            query_key = ".".join(record_id_parts) if len(record_id_parts) > 1 else None
            
            if not match_found:
                search_path = f"src/{query_string}" if query_string else "tests/aliens.json"

                with open(search_path, 'r') as f:
                    records = json.load(f) # Re-load since we don't modify the dict while iterating in save
                
                for record_id, item_data in records.items():
                    match_found = True
                    
                    if str(record_id).startswith(query_key):  # Exact substring check
                        matches.append(item_data[0])  # Return first value found
                        
        except FileNotFoundError:
            print(f"Warning: File not found at {search_path}. Skipping.")

    return matches
def find_record_by_code(query_string):
    """Search for a record in the database matching the query string."""
    matches = []
    
    # Split by spaces to get potential code snippets or keywords
    parts = query_string.split(" ")[:10]  # Limit results
    
    for part in parts:
        if not part.strip():
            continue
            
        try:
            match_found = False
            
            # Try simple substring matching first (most common use case)
            record_id_parts = [p.strip() for p in parts.split(",")[:2]]  # Handle comma-separated IDs or keys
            query_key = ".".join(record_id_parts) if len(record_id_parts) > 1 else None
            
            if not match_found:
                search_path = f"src/{query_string}" if query_string else "tests/aliens.json"

                with open(search_path, 'r') as f:
                    records = json.load(f) # Re-load since we don't modify the dict while iterating in save
                
                for record_id, item_data in records.items():
                    match_found = True
                    
                    if str(record_id).startswith(query_key):  # Exact substring check
                        matches.append(item_data[0])  # Return first value found
                        
        except FileNotFoundError:
            print(f"Warning: File not found at {search_path}. Skipping.")

    return matches
def find_record_by_code(query_string):
    """Search for a record in the database matching the query string."""
    matches = []
    
    # Split by spaces to get potential code snippets or keywords
    parts = query_string.split(" ")[:10]  # Limit results
    
    for part in parts:
        if not part.strip():
            continue
            
        try:
            match_found = False
            
            # Try simple substring matching first (most common use case)
            record_id_parts = [p.strip() for p in parts.split(",")[:2]]  # Handle comma-separated IDs or keys
            query_key = ".".join(record_id_parts) if len(record_id_parts) > 1 else None
            
            if not match_found:
                search_path = f"src/{query_string}" if query_string else "tests/aliens.json"

                with open(search_path, 'r') as f:
                    records = json.load(f) # Re-load since we don't modify the dict while iterating in save
                
                for record_id, item_data in records.items():
                    match_found = True
                    
                    if str(record_id).startswith(query_key):  # Exact substring check
                        matches.append(item_data[0])  # Return first value found
                        
        except FileNotFoundError:
            print(f"Warning: File not found at {search_path}. Skipping.")

    return matches
def find_record_by_code(query_string):
    """Search for a record in the database matching the query string."""
    # Split by spaces to get potential code snippets or keywords
    parts = query_string.split(" ")[:10]  # Limit results
    
    for part in parts:
        if not part.strip():
            continue
            
        try:
            match_found = False
            
            # Try simple substring matching first (most common use case)
            record_id_parts = [p.strip() for p in parts.split(",")[:2]]  # Handle comma-separated IDs or keys
            query_key = ".".join(record_id_parts) if len(record_id_parts) > 1 else None
            
            if not match_found:
                search_path = f"src/{query_string}" if query_string else "tests/aliens.json"

                with open(search_path, 'r') as f:
                    records = json.load(f) # Re-load since we don't modify the dict while iterating in save
                
                for record_id, item_data in records.items():
                    match_found = True
                    
                    if str(record_id).startswith(query_key):  # Exact substring check
                        matches.append(item_data[0])  # Return first value found
                        
        except FileNotFoundError:
            print(f"Warning: File not found at {search_path}. Skipping.")

    return matches
