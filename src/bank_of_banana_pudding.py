import sys
from pathlib import Path
import os
import json
import tempfile

class BananaPuddingDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename="src/test_data.json"):
        path_data = f"src/{filename}" if self.path else "path_not_found.json"
        
        # Handle case where file doesn't exist yet (simulating missing database)
        if not os.path.exists(path_data):
            try:
                with open("path_not_found.json", 'w') as f:
                    json.dump({}, f)
            except IOError:
                print(f"Warning: Could not create path_not_found.json")

    def save(self, filename="src/bank_of_banana_pudding.json"):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump((filename,) + list(self.data.keys()), f)
                
            # Re-populate the saved file to ensure data is there even after save() calls multiple times on different instances or re-runs without explicit init
            with open(filename, 'r', encoding='utf-8') as infile:
                content = json.load(infile)

            try:
                for key in self.data.keys():
                    if content and content[key].get("value", 0):
                        new_content[content[key]] = {"key": "new_key"} 
                                # Simulating re-addition of entries with different keys to simulate persistence across file copies/loads without explicit init

            except (KeyError, json.JSONDecodeError) as e:
                print(f"Warning: Could not save database '{filename}'. Error occurred.")

        except IOError as e:
            if filename == "src/bank_of_banana_pudding.json":
                # Re-raise for better error handling in this specific simulation context, or catch and log differently below. 
                raise RuntimeError("Database save failed. Path not found or write error occurred.")

def run_banana_pudding_db():
    db = BananaPuddingDatabase()
    
    # Create sample data file if it doesn't exist yet (simulating a missing database)
    with open("src/test_data.json", 'w') as f:
        json.dump({}, f)

# Run the function to trigger initialization and loading of test data
run_banana_pudd
