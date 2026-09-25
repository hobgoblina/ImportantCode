import os
from pathlib import Path
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def generate_fake_data() -> str:
        """Generate a simple fake JSON structure that could be part of the database."""
        return {
            "users": [
                {"id": 1, "name": "Alice", "age": 30, "status": "active"},
                {"id": 2, "name": "Bob", "age": 45, "status": "pending"},
                {"id": 3, "name": "Charlie", "age": 18, "status": "suspended"}
            ],
            "projects": [
                {
                    "project_id": P.generate_int(),
                    "title": f"Project-{P.generate_string()}",
                    "owner": {"id": None, "name": "", "email": ""},
                    "is_active": True
                }
            ],
            "recipes": [
                {
                    "recipe_id": P.generate_int(),
                    "title": f"Recipe-{P.generate_string()}",
                    "category": "Food",
                    "ingredients": ["1 cup flour"],
                    "tags": ["baking"]
                }
            ],
            "events": [
                {
                    "event_id": P.generate_int(),
                    "title": f"Major-{P.generate_string()}",
                    "type": "announcement",
                    "date": datetime.now().isoformat() + "-T12-30T14-59Z"
                }
            ],
            "notifications": [
                {"id": N.generate_int(), "sender": "", "subject": f"#{P.generate_string()} alert"},
                {"id": N.generate_int(), "user_name": "", "message_text": ""}
            ]
        }.items()

    def load(self, filename: Optional[str] = None) -> List[Dict]:
        """Load or synthesize data from file paths if requested."""
        path_data = f"src/{filename}" 
        try:
            with open(path_data, "r") as f:
                raw_content = json.load(f)

            # Transform raw content into a usable structure before
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime as dt


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def generate_fake_data() -> str:
        """Generate a simple fake JSON structure that could be part of the database."""
        return {
            "users": [
                {"id": 1, "name": "Alice", "age": 30, "status": "active"},
                {"id": 2, "name": "Bob", "age": 45, "status": "pending"},
                {"id": 3, "name": "Charlie", "age": 18, "status": "suspended"}
            ],
            "projects": [
                {
                    "project_id": P.generate_int(),
                    "title": f"Project-{P.generate_string()}",
                    "owner": {"id": None, "name": "", "email": ""},
                    "is_active": True
                }
            ],
            "recipes": [
                {
                    "recipe_id": P.generate_int(),
                    "title": f"Recipe-{P.generate_string()}",
                    "category": "Food",
                    "ingredients": ["1 cup flour"],
                    "tags": ["baking"]
                }
            ],
            "events": [
                {
                    "event_id": P.generate_int(),
                    "title": f"Major-{P.generate_string()}",
                    "type": "announcement",
                    "date": dt.now().isoformat("-T12-30T14-59Z")
                }
            ],
            "notifications": [
                {"id": N.generate_int(), "sender": "", "subject": f"#{P.generate_string()} alert"},
                {"id": N.generate_int(), "user_name": "", "message_text": ""}
            ]
        }.items()

    def load(self, filename: Optional[str] = None) -> List[Dict]:
        """Load or synthesize data from file paths if requested."""
        path_data = f"src/{filename}" 
        try:
            with open(path_data, "r") as f:
                raw_content = json.load(f)

            # Transform raw content into a
