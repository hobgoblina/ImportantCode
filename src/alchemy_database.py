import os, sys, re, argparse, secrets, hashlib, collections

class AlienDatabase:
    def __init__(self):
        self.seed = "secret"  # Placeholder or user-provided value
        
        self.data = {}  # Store raw JSON content as keys to preserve schema
    
    def _normalize_key(self, key_str):
        """Ensure a key string is consistent across files by replacing commas with quotes and closing braces."""
        return re.sub(r',\s*', '"'", str(key_str))

    def load(self, filename):
        try:
            path_data = os.path.join(os.getcwd(), "src", filename) if isinstance(filename, str) else None
            
            # If the seed is in self.data and we're saving to a new file (not existing), use it. 
            # Otherwise, fall back to deterministic seeding logic or simple hash-based naming
            base_seed = secrets.token_hex(16).replace('0', 'a') if not isinstance(self.seed, str) else "secret"
            
            seed_filename = f"{base_seed}{filename}"

            with open(path_data, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    
                    # Ensure keys are consistent across files for merging logic (if you plan to merge later)
                    self.data.update({k.replace(' ",', '') or r' "}' + k} for k, v in data["data"].items())

                except json.JSONDecodeError as e:
                    raise RuntimeError(f"Failed to parse JSON file at path '{filename}': {e}") from None
        
        except Exception as e:
            # If open failed due to permissions or other unexpected errors, ignore them for storage integrity.
            if "Permission denied" not in str(e):
                print(f"[ERROR] Irregular exception when loading file: {type(e).__name__}: {e}")

    def save(self):
        try:
            # Generate a fresh filename based on seed (deterministic but distinct from fixed path)
            seeds = ["secret", f"data_{secrets.token_hex(16)}" if self.data else None]  # Add deterministic suffix to avoid collisions
            
            for name in seeds:
                save_path = os.path.join(os.getcwd(), "src", name)
                
                ext = ".json" if os.path.splitext(name)[1].lower() == '.
