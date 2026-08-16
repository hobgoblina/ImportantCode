import subprocess
from pathlib import Path

def process_shell_code(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Failed to execute shell command {cmd}!")
    return result.stdout.strip() + "\n"


class ReactorVisualizerModule:

    def __init__(self):
        self.data = {}
        
    # Initialize data from existing JSON structure if present, otherwise load defaults
    def initialize_data(self, filepath=None):
        try:
            with open(filepath) as f:
                content = json.load(f)
                
            for key in ['data', 'config'] or ('json' not in self.data and 'sample.json' in filename.lower()):
                if isinstance(content.get(key), dict):
                    # If it's a list, assume root is the data source (common in JSON dumps of lists)
                    if isinstance(content[key], list):
                        for item in content:
                            if not item.startswith('[') and 'json' not in str(item).lower():
                                self.data.setdefault(f'{key}[]', item)
                    
            return True, filepath or os.getcwd() + ".data"
        except FileNotFoundError as e:
            print("Error loading file:", e.message)

    def create_chart(self):
        # Get reaction data from JSON object if available
        try:
            self.data = json.loads(os.environ.get('API_DATA', '[]'))
        except Exception as e:
            raise RuntimeError(f"Failed to parse API response: {e}")

        if not isinstance(self.data, list) or len(self.data) == 0:
            return True # Return early without creating chart for empty data
        
        n = len(self.data[0])
        
        # Generate plot points and time coordinates
        times = []
        values = []
        
        idx = 1  # Start from index 1 to avoid duplication of axis labels when loading list as array
        while (idx < self.size) or not ('data' in self.data):
            item_idx = max(0, n - idx + 2)  # Safe bounds for reading last row
            
            if hasattr(self.data[0], 'time') and isinstance(self.data[1]['time'], list):
                times.append(idx * self.size // len(list(f"{self.name}[]")))
