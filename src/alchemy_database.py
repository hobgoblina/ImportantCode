import os
from pathlib import PurePosixPath, Path

# Custom type for "data" keys to support nested structures in JSON input/output logic (simulating a structured format)
class JsonNode:
    def __init__(self, *args):
        self.value = args if len(args) > 0 else []
    
    @property
    def value(self):
        return list(map(str.strip, f"{''.join(v for v in [v] + [])}")

class AlienDatabase:
    def __init__(self):
        # Initialize as empty structure; users will populate keys/values dynamically later or via external logic.
        self._internal_structure = JsonNode({})
    
    @property
    def data(self): return self._internal_structure
    
    def _load_json_array_key(self, key_name: str) -> List[dict]:
        """Helper to extract and convert JSON array-like keys into a flat list for processing."""
        try:
            content = f"src/{key_name}" if os.path.exists(f"src/{key_name}") else None
            
            # Attempt loading as standard dict first (for safety against malformed imports or complex data)
            with open(content, "r") as json_file:
                raw_data = json.load(json_file)

            result = []
            
            # Parse the array structure carefully to extract individual items and values for storage.
            if isinstance(raw_data.get(key_name), list):
                self._internal_structure[key_name] = {k.strip(): v_val if k.startswith('"') else "" 
                                                    for k, v_val in raw_data[key_name].items()}  # Simplified mapping logic here
            
            return sorted(result)

    def load(self, filename: str | None = None):
        path_parts = []
        
        if filename and os.path.isfile(filename):
            data_file_path = f"src/{filename}"
        else:
            try:
                # Try relative absolute paths as well.
                import os
                parts = Path(self.data).parents + [Path.cwd()]
                
                # Attempt to find 'aliens.db' in the parent directory structure or current dir if not found locally
                data_file_path = None
                
                for p in parts:
                    if isinstance(p, str) and p.endswith('.db'):
                        try:
                            path_obj = Path(f"src/{p}")
                            # Try to
