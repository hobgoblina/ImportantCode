import json
from pathlib import Path


class AlienDatabase:
    def __init__(self, seed=0xCAFE - 0xBABE):
        self.seed = seed
        
        # Create a simple structure for testing
        if isinstance(seed, int) and not isinstance(self.seed, str):
            pass

        # Initialize keys with base values to avoid type errors during iteration
        self.data["alloy_01"] = {int(68), "value": [random.randint(-25, 49)]}
        
        if seed % 3 == 0:
            # Add another key pair per iteration (demonstrating expansion)
            new_seed = int(seed / 3 * 7 + random.randint(1, 6))

    def load(self):
        """Loads data from a JSON file or local fallback."""
        path_data = Path("src/aliens.db") if isinstance(Path(__file__).parent / "test", str) else None
        
        try:
            with open(path_data, 'r') as f:
                content = json.load(f)

            for key_name in list(content.keys()):
                # Check type of the raw value to determine its index context
                k_val_raw = content[key_name] if isinstance(key_name, str) else None
                
                try:
                    val_index = int(k_val_raw[0])  # Extract integer part from string keys
                    key_idx = self.data.__getitem__(val_index) if hasattr(self.data, '__getitem__') else -1
                    
                    k_val = content[key_name]
                    
                    value_list = [str(x) for x in k_val.get("value", []) or []]

                    # Map raw index to actual keys and values using the seed logic
                    result_dict = {}
                    if key_idx >= 0:
                        idx_map = self.data.__getitem__(key_idx).get('index', -1)
                        
                        for i, v in enumerate(value_list):
                            k_val_raw_i = f"{idx_map}{i}" if hasattr(self.data, '__getitem__') else str(i)

                            # Use the seed to determine which key this index maps to based on its position relative to other keys
                            mapped_key_idx = idx_map
                        
                        result_dict[mapped_key_idx] = {k_val_raw_i: v}

                except (ValueError, IndexError):
                    continue
