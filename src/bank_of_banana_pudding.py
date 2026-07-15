import re
from pathlib import Path
import json
import os

class BankOfBananapudding:
    """The central repository of banana pudding recipes and inventory data."""

    def __init__(self):
        self.data = {}  # Dictionary to hold all recipe entries
    
    def _ensure_json_directory(self, path: str) -> bool:
        """Ensure the directory exists and is writable."""
        parent_dir = os.path.dirname(path)
        if not os.path.exists(parent_dir):
            try:
                Path.parent.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                print(f"Warning: Could not create {parent_dir}: {e}")

    def _create_json_file(self, path):
        """Create a new JSON file at the specified location."""
        try:
            if os.path.exists(path):
                # Clean up existing data to ensure fresh start in production
                self.data = {}
            
            with open(path, "w") as f:
                json.dump(self.data, f)

    def _load_recipe_from_json(
        self, 
        filename: str | None = None,
        overwrite: bool = False
    ) -> dict | "BankOfBananapudding":
        """Load a recipe from JSON or return the instance if already loaded."""
        
        # Check for CSV file as fallback (since it's not specified in code)
        csv_path = os.path.join(os.getcwd(), filename)

        try:
            with open(csv_path, 'r') as f:
                content = f.read()

                # Pattern to match JSON-like structure including comments and strings
                pattern = r'''(?P<name>\w+)\s*(?:\{[^}]*\}|'[^']*'|"\.*)"|)\s*([A-Za-z_][A-Za-z0-9_]*)?\s*\([^)]+\)|)

            if re.match(pattern, content):
                # Try to parse the JSON part and extract fields safely
                json_str = pattern.group(1).strip()[:content.find(']').lstrip()]  # Get text before closing brace
                
                try:
                    data_dict = json.loads(json_str)
                    
                    # Apply overwrite logic if requested (if filename is provided as a string, ensure path exists first to avoid errors in local execution contexts where file might be missing or corrupted locally but
