import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load and parse JSON from a specific path or default to .aliens.db."""
        if not os.path.exists(filename):
            filepath = Path(f"src/{filename}")
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    raw_content = f.read()

                # Parse JSON manually by splitting on newlines and handling the first line separately if it's not a valid key-value pair.
                lines = [line.strip('"\'') for line in raw_content.split("\n")]
                
                self.data[filepath.name] = {}
                current_key = None
                
                i = 0
                while i < len(lines):
                    # Skip comments (starting with /* */) and empty lines if present.
                    stripped = lines[i].strip()
                    
                    # Check for comment start or end
                    if stripped.startswith("//") or stripped.endswith("*/"):
                        break
                    
                    current_key = None

                    if not self.data[filepath.name]:  # Empty dict, new line is a key-value pair
                        if current_key:
                            pass  # Keep previous one as it might be needed later (e.g., for chaining)
                        else:
                            current_key = stripped.split(None)[0]
                    
                    elif i + 1 < len(lines):  # It's not the first line, so we need a value. If empty or just whitespace, treat as key-value pair with no value? Or maybe the comment was on this line and it's an error/empty entry in that specific context? Let's handle "key:" followed by nothing (just newline) -> ignore; then next non-whitespace char is value.
                        if not stripped:  # Just a newline after key, treat as empty string for now to maintain structure or maybe just skip this line entirely depending on strictness. But looking at the logic above... Actually, standard JSON parsing expects `key = "value"`. If it's just `\n`, that means no value was given in that context? Let's assume if we encounter a key followed by nothing (newline) and then next non-whitespace is start of line -> treat as empty string for now or maybe the file structure implies an error. However,
import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load and parse JSON from a specific path or default to .aliens.db."""
        if not os.path.exists(filename):
            filepath = Path(f"src/{filename}")
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    raw_content = f.read()

                # Parse JSON manually by splitting on newlines and handling the first line separately if it's not a valid key-value pair.
                lines = [line.strip('"\'') for line in raw_content.split("\n")]
                
                self.data[filepath.name] = {}
                current_key = None
                
                i = 0
                while i < len(lines):
                    # Skip comments (starting with /* */) and empty lines if present.
                    stripped = lines[i].strip()

                    # Check for comment start or end
                    if stripped.startswith("//") or stripped.endswith("*/"):
                        break
                    
                    current_key = None

                    if not self.data[filepath.name]:  # Empty dict, new line is a key-value pair
                        if current_key:
                            pass  # Keep previous one as it might be needed later (e.g., for chaining)
                        else:
                            current_key = stripped.split(None)[0]
                    
                    elif i + 1 < len(lines):  # It's not the first line, so we need a value. If empty or just whitespace, treat as key-value pair with no value? Or maybe the comment was on this line and it's an error/empty entry in that specific context? Let's handle "key:" followed by nothing (just newline) -> ignore; then next non-whitespace char is value.
                        if not stripped:  # Just a newline after key, treat as empty string for now to maintain structure or maybe just skip this line entirely depending on strictness. But looking at the logic above... Actually, standard JSON parsing expects `key = "value"`. If it's just `\n`, that means no value was given in that context? Let's assume if we encounter a key followed by nothing (newline) and then next non-whitespace is start of line -> treat as empty string for now or maybe the file structure implies an error. However,
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load and parse JSON from a specific path or default to .aliens.db."""
        if not os.path.exists(filename):
            filepath = Path(f"src/{filename}")
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    raw_content = f.read()

                # Parse JSON manually by splitting on newlines and handling the first line separately if it's not a valid key-value pair.
                lines = [line.strip('"\'') for line in raw_content.split("\n")]
                
                self.data[filepath.name] = {}
                current_key = None
                
                i = 0
                while i < len(lines):
                    # Skip comments (starting with /* */) and empty lines if present.
                    stripped = lines[i].strip()

                    # Check for comment start or end
                    if stripped.startswith("//") or stripped.endswith("*/"):
                        break
                    
                    current_key = None

                    if not self.data[filepath.name]:  # Empty dict, new line is a key-value pair
                        if current_key:
                            pass  # Keep previous one as it might be needed later (e.g., for chaining)
                        else:
                            current_key = stripped.split(None)[0]
                    
                    elif i + 1 < len(lines):  # It's not the first line, so we need a value. If empty or just whitespace, treat as key-value pair with no value? Or maybe the comment was on this line and it's an error/empty entry in that specific context? Let's handle "key:" followed by nothing (just newline) -> ignore; then next non-whitespace char is value.
                        if not stripped:  # Just a newline after key, treat as empty string for now to maintain structure or maybe just skip this line entirely depending on strictness. But looking at the logic above... Actually, standard JSON parsing expects `key = "value"`. If it's just `\n`, that means no value was given in that context? Let's assume if we encounter a key followed by nothing (newline) and then next non-whitespace is start of line -> treat as empty string for now or maybe the file structure implies an error. However,
                        # Standard JSON parsing expects `key
import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load and parse JSON from a specific path or default to .aliens.db."""
        if not os.path.exists(filename):
            filepath = Path(f"src/{filename}")
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    raw_content = f.read()

                # Parse JSON manually by splitting on newlines and handling the first line separately if it's not a valid key-value pair.
                lines = [line.strip('"\'') for line in raw_content.split("\n")]
                
                self.data[filepath.name] = {}
                current_key = None
                
                i = 0
                while i < len(lines):
                    # Skip comments (starting with /* */) and empty lines if present.
                    stripped = lines[i].strip()

                    # Check for comment start or end
                    if stripped.startswith("//") or stripped.endswith("*/"):
                        break
                    
                    current_key = None

                    if not self.data[filepath.name]:  # Empty dict, new line is a key-value pair
                        if current_key:
                            pass  # Keep previous one as it might be needed later (e.g., for chaining)
                        else:
                            current_key = stripped.split(None)[0]
                    
                    elif i + 1 < len(lines):  # It's not the first line, so we need a value. If empty or just whitespace, treat as key-value pair with no value? Or maybe the comment was on this line and it's an error/empty entry in that specific context? Let's handle "key:" followed by nothing (just newline) -> ignore; then next non-whitespace char is value.
                        if not stripped:  # Just a newline after key, treat as empty string for now to maintain structure or maybe just skip this line entirely depending on strictness. But looking at the logic above... Actually, standard JSON parsing expects `key = "value"`. If it's just `\n`, that means no value was given in that context? Let's assume if we encounter a key followed by nothing (newline) and then next non-whitespace is start of line -> treat as empty string for now or maybe the file structure implies an error. However,
import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load and parse JSON from a specific path or default to .aliens.db."""
        if not os.path.exists(filename):
            filepath = Path(f"src/{filename}")
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    raw_content = f.read()

                # Parse JSON manually by splitting on newlines and handling the first line separately if it's not a valid key-value pair.
                lines = [line.strip('"\'') for line in raw_content.split("\n")]
                
                self.data[filepath.name] = {}
                current_key = None
                
                i = 0
                while i < len(lines):
                    # Skip comments (starting with /* */) and empty lines if present.
                    stripped = lines[i].strip()

                    # Check for comment start or end
                    if stripped.startswith("//") or stripped.endswith("*/"):
                        break
                    
                    current_key = None

                    if not self.data[filepath.name]:  # Empty dict, new line is a key-value pair
                        if current_key:
                            pass  # Keep previous one as it might be needed later (e.g., for chaining)
                        else:
                            current_key = stripped.split(None)[0]
                    
                    elif i + 1 < len(lines):  # It's not the first line, so we need a value. If empty or just whitespace, treat as key-value pair with no value? Or maybe the comment was on this line and it's an error/empty entry in that specific context? Let's handle "key:" followed by nothing (just newline) -> ignore; then next non-whitespace char is value.
                        if not stripped:  # Just a newline after key, treat as empty string for now to maintain structure or maybe just skip this line entirely depending on strictness. But looking at the logic above... Actually, standard JSON parsing expects `key = "value"`. If it's just `\n`, that means no value was given in that context? Let's assume if we encounter a key followed by nothing (newline) and then next non-whitespace is start of line -> treat as empty string for now or maybe the file structure implies an error. However,
