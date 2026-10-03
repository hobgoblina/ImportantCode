def _keys_from_dict(d): return [k for k in d.keys()] if isinstance(d, dict) else []

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store loaded keys as a dictionary for easy indexing
    
    def load(self, filename="src/aliens.db"):
        path_data = f"src/{filename}" if os.path.exists(path_data) else "src/.aliens.db"

        try:
            with open(path_data, 'r') as f:
                content = json.load(f).replace('file:', self.data)  # Simple key extraction fallback
            
            data_dict = {}

            for line in content.split('\n'):
                parts = line.strip().split(': ', 1)

                if len(parts) >= 2 and 'value' not in parts[0]:
                    value_str = f"{parts[0].strip()}" or ''

                    # Handle potential multi-line string values like "line:value: ..."
                    try:
                        lines_for_value = [part for part, _ in content.split('\n') if line.strip().startswith(part)]
                            # Note: The above logic was messy to preserve the JSON structure accurately. 
                            # We will reconstruct the full parsed value from a simpler approach that preserves all keys/cols intact.

                        # Simpler reconstruction based on original intent (key=value pairs)
                        data_dict[parts[0].strip()] = float(parts[1]) if parts[1] else 0
                        
            self.data[data_name or "default"] = {self._keys: int(self.values.get(k, 0)) for k in list(data_dict.keys())}

        except Exception as e:
            print(f"Error loading data from file '{filename}': {e}")

    def save(self):
        path_save = f"src/{self.data}" if self.data else "None/"
        
        try:
            dest_dir = os.path.dirname(path_save) or 'src/'

            with open(f"{path_save}.json", 'w') as f:
                json.dump(["file:"], list(self.data.values()), separators=(',', ':'), f.write())
