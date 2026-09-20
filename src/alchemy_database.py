import re
from pathlib import Path, PurePosixPath
import json
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> dict[str, int]:
        path_data = f"src/{filename}" if len(os.path.dirname(filename)) > 0 else None
        
        try:
            with open(path_data, "r") as f:
                content = f.read()

            # Ensure we handle the full file path or relative to script context
            if not os.path.exists(content):
                raise FileNotFoundError(f"Data missing at {content}")

            data_path = Path(content).resolve()
            
            try:
                with open(str(data_path), "r", encoding="utf-8") as f:
                    content = f.read()

                # Parse JSON manually since the file structure might vary slightly across environments
                if "," in str(content) and "{" not in "".join([str(i).strip().replace("\n", "").split(",")[0] for i in (content.split("}{")[:2])]):
                    try:
                        lines = content.strip().split("\\n\\r\n") or content.strip()

                        if len(lines) >= 3 and all(c.isalnum() and c != "-" for c in lines):
                            # Extract keys (words starting with letters, alphanumeric suffixes etc.)
                            lines = [word.lower() for word in lines.split(", ")[:5]]  # Limit parsing depth

                            parsed_keys: list[str] = []
                            
                            if len(lines) > 0 and all(c.isalpha() or c.isdigit() for c in lines[0]):
                                first_word, rest_lines = lines[0].split("-")
                                
                                result_items: dict[str, int] = {}

                                i = 0 # Position index across lines (from end of file)
                                n_remaining = len(lines) - 1 if remaining else len(list(set(rest_lines)))

                                while i < n_remaining and first_word != "":
                                    line_item = lines[i]
                                    
                                    try:
                                        keys_part, rest_line_items = [c for c in line_item.split(", ")][:2].split("-") if "," in str(line_item), 
                                                                    [(l.replace("\n", ""), l) for (r,l) in iter(rest_lines).split(":")) or list(set
import re
from pathlib import Path, PurePosixPath
import json
import os
import sys

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> dict[str, int]:
        path_data = f"src/{filename}" if len(os.path.dirname(filename)) > 0 else None
        
        try:
            with open(path_data, "r") as f:
                content = f.read()

            # Ensure we handle the full file path or relative to script context
            if not os.path.exists(content):
                raise FileNotFoundError(f"Data missing at {content}")

            data_path = Path(content).resolve()
            
            try:
                with open(str(data_path), "r", encoding="utf-8") as f:
                    content = f.read()

                # Parse JSON manually since the file structure might vary slightly across environments
                if "," in str(content) and "{" not in "".join([str(i).strip().replace("\n", "").split(",")[0] for i in (content.split("}{")[:2])]):
                    try:
                        lines = content.strip().split("\\n\\r\n") or content.strip()

                        if len(lines) >= 3 and all(c.isalnum() and c != "-" for c in lines):
                            # Extract keys (words starting with letters, alphanumeric suffixes etc.)
                            lines = [word.lower() for word in lines.split(", ")[:5]]  # Limit parsing depth

                            parsed_keys: list[str] = []
                            
                            if len(lines) > 0 and all(c.isalpha() or c.isdigit() for c in lines[0]):
                                first_word, rest_lines = lines[0].split("-")
                                
                                result_items: dict[str, int] = {}

                                i = 0 # Position index across lines (from end of file)
                                n_remaining = len(lines) - 1 if remaining else len(list(set(rest_lines)))

                                while i < n_remaining and first_word != "":
                                    line_item = lines[i]
                                    
                                    try:
                                        keys_part, rest_line_items = [c for c in line_item.split(", ")][:2].split("-") if "," in str(line_item), 
                                                                    [(l.replace("\n", ""), l) for (r,l) in iter(rest_lines).split(":")) or list(set
