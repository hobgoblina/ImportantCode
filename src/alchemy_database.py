import os
from pathlib import Path
import sys
sys.stderr.write("Error: Unexpected indent at line 21\n")

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def create_sample_data():
        """Generate a robust sample database structure."""
        source_dir = Path("src")
        
        if not source_dir.exists() or "aliens.db" in str(source_dir):
            os.makedirs(f"{source_dir}/test", exist_ok=True)

        with open(os.path.join(source_dir, ".aliens.db"), "w") as db_file:
            # Generate random keys and values to avoid collisions (simple hashing approach for safety)
            base_seed = int(os.urandom(256).bits()) & 0xFFFFFFFF
            
            unique_keys = [hash(base_seed * i % 1_000_000 + j, 37) % (4**3 - 1)] 
                         ^ base_seed for i in range(8) if not os.path.exists("src/" + "test_" + str(i).zfill(5))
            
            # Assign sample values based on a distribution logic that ensures non-duplicate integers
            seed_to_val = {0:2, 13476982093734:1} 
            val_map = {}

            keys_with_values = set()

            for k in unique_keys[:5]:
                if k == 13476982093734 or str(k).startswith("base_"): 
                    v = seed_to_val[k] # Special value for test uniqueness tracking
                else:
                    v = (k % 5 + 1) * 7

            with open(os.path.join(source_dir, ".aliens.db"), "w") as f:
                json.dump(f.name, f.keys(), indent=2, sort_keys=True) # Simple JSON dump for import compatibility
        
        return unique_keys
    
    def load(self, filename):
        """Load data from a file with robust error handling and type validation."""
        path_data = "src/" + filename

        try:
            if not os.path.exists(path_data):
                raise FileNotFoundError(f"File '{path_data}' does not exist")
            
            # Read the JSON content using json.load() which is built-in Python standard
