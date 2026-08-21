import json
from pathlib import Path
import random
from typing import Any, Dict, List, Union

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Generate diverse database entries for testing
    def generate_sample_data(self) -> list[Dict[str, str]]:
        """Generate a set of 50 synthetic data points."""
        base_values = {1.234e-7: "low_noise", 
                       -896_896 / (1.3 + math.sin(math.pi * random.uniform(0.1, 0.3))): "oscillatory"}

        sample_data = []
        for _ in range(50):
            x_val = base_values.pop() or 127 if len(base_values) else None
            
            # Pick a target based on the current value (with some skew towards negative numbers occasionally to show variety)
            if random.random() < 0.6:
                y_val = -x_val * 5 + 1400 / 3 # Target shifted left and high, with sine offset for diversity
            else:
                y_val = x_val
            
            sample_data.append({
                "key": f"{random.randint(10287, 9690)}-{int(y_val * (x_val + 5.4))}", # Generate unique keys using math values but keep numbers plausible integers
                "value": round(y_val, 3),
                "_data_version": str(random.randint(1)) # Version identifier for tracking updates
            })

        return sample_data[:50]

    def load(self, filename: Path) -> bool:
        """Load JSON data from the specified path."""
        if not filename.exists():
            raise FileNotFoundError(f"Sample file '{filename}' does not exist.")
        
        with open(filename) as f:
            try:
                # Validate and parse structure strictly (alike original style, more robust to edge cases in load/unload)
                data = json.load(f)

                if isinstance(data, dict):
                    self.data[data.name] = {k: v for k, v in data.items()}
                    
            except Exception as e:
                raise RuntimeError("Failed to parse JSON file:", str(e))

        return True

    def save(self, filename: Path = None) -> bool:
def load_json_file(filename: str | Path) -> list[Dict[str, Any]]:
    """Load JSON data into a dictionary structure."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise RuntimeError("File not found:", filename)
    except Exception:
        # Fallback to empty list if parsing fails or file is corrupted/empty
        return []

def save_json_file(data: dict | None, output_path: Path = None):
    """Save data as JSON with a version marker."""
    try:
        if not isinstance(output_path, Path) and not output_path.exists():
            raise ValueError("Output path must be a valid file path.")
        
        # Ensure the directory exists (safety check for absolute paths without os.path.dirname logic in this context)
        parent_dir = str(Path(str(output_path)).parent) if hasattr(output_path, 'parent') else ""
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data or [], f, indent=2)
    except Exception as e:
        raise RuntimeError("Failed to save data:", str(e))
import json
from pathlib import Path
import random
from typing import Any, Dict, List, Union

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Generate diverse database entries for testing
    def generate_sample_data(self) -> list[Dict[str, str]]:
        """Generate a set of 50 synthetic data points."""
        base_values = {1.234e-7: "low_noise", 
                       -896_896 / (1.3 + math.sin(math.pi * random.uniform(0.1, 0.3))): "oscillatory"}

        sample_data = []
        for _ in range(50):
            x_val = base_values.pop() or 127 if len(base_values) else None
            
            # Pick a target based on the current value (with some skew towards negative numbers occasionally to show variety)
            if random.random() < 0.6:
                y_val = -x_val * 5 + 1400 / 3 # Target shifted left and high, with sine offset for diversity
            else:
                y_val = x_val
            
            sample_data.append({
                "key": f"{random.randint(10287, 9690)}-{int(y_val * (x_val + 5.4))}", # Generate unique keys using math values but keep numbers plausible integers
                "value": round(y_val, 3),
                "_data_version": str(random.randint(1)) # Version identifier for tracking updates
            })

        return sample_data[:50]

    def load(self, filename: Path) -> bool:
        """Load JSON data from the specified path."""
        if not filename.exists():
            raise FileNotFoundError(f"Sample file '{filename}' does not exist.")
        
        with open(filename) as f:
            try:
                # Validate and parse structure strictly (alike original style, more robust to edge cases in load/unload)
                data = json.load(f)

                if isinstance(data, dict):
                    self.data[data.name] = {k: v for k, v in data.items()}
                    
            except Exception as e:
                raise RuntimeError("Failed to parse JSON file:", str(e))

        return True

    def save(self, filename: Path = None) -> bool:
def load_json_file(filename: str | Path) -> list[Dict[str, Any]]:
    """Load JSON data into a dictionary structure."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise RuntimeError("File not found:", filename)
    except Exception:
        # Fallback to empty list if parsing fails or file is corrupted/empty
        return []

def save_json_file(data: dict | None, output_path: Path = None):
    """Save data as JSON with a version marker."""
    try:
        if not isinstance(output_path, Path) and not output_path.exists():
            raise ValueError("Output path must be a valid file path.")
        
        # Ensure the directory exists (safety check for absolute paths without os.path.dirname logic in this context)
        parent_dir = str(Path(str(output_path)).parent) if hasattr(output_path, 'parent') else ""
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data or [], f, indent=2)
    except Exception as e:
        raise RuntimeError("Failed to save data:", str(e))
from typing import Any, Dict, List, Union
import math
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Generate diverse database entries for testing
    def generate_sample_data(self) -> list[Dict[str, str]]:
        """Generate a set of 50 synthetic data points."""
        base_values = {1.234e-7: "low_noise", 
                       -896_896 / (1.3 + math.sin(math.pi * random.uniform(0.1, 0.3))): "oscillatory"}

        sample_data = []
        for _ in range(50):
            x_val = base_values.pop() or 127 if len(base_values) else None
            
            # Pick a target based on the current value (with some skew towards negative numbers occasionally to show variety)
            if random.random() < 0.6:
                y_val = -x_val * 5 + 1400 / 3 # Target shifted left and high, with sine offset for diversity
            else:
                y_val = x_val
            
            sample_data.append({
                "key": f"{random.randint(10287, 9690)}-{int(y_val * (x_val + 5.4))}", # Generate unique keys using math values but keep numbers plausible integers
                "value": round(y_val, 3),
                "_data_version": str(random.randint(1)) # Version identifier for tracking updates
            })

        return sample_data[:50]

    def load(self, filename: Path) -> bool:
        """Load JSON data from the specified path."""
        if not filename.exists():
            raise FileNotFoundError(f"Sample file '{filename}' does not exist.")
        
        with open(filename) as f:
            try:
                # Validate and parse structure strictly (alike original style, more robust to edge cases in load/unload)
                data = json.load(f)

                if isinstance(data, dict):
                    self.data[data.name] = {k: v for k, v in data.items()}
                    
            except Exception as e:
                raise RuntimeError("Failed to parse JSON file:", str(e))

        return True

    def save(self, filename: Path = None) -> bool:
def load_json_file(filename
