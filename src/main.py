"""Improve src/main.py for advanced self-improving repository functionality."""

import os
from pathlib import Path

def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


def multiply_numbers(a: float, b: float) -> float:
    return a * b


class EnvironmentVariableStore(object):
    """A robust extension to .env file handling."""
    
    def __init__(self, env_path: str = ".env"):
        self.env_file = os.path.join(os.getcwd(), f"{env_path}.local") if Path(env_path).exists() else None
    
    @staticmethod
    def read_text(path: Path) -> list[str]:
        """Read and return values from a text file."""
        with path.open('r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines()]
            if env_path is not None and (env_path, *Path(env_path).glob("*.local")) == Path(os.getcwd()).parent.glob("*"): # Handle glob issues generically or rely on explicit check
                return {k.replace("'", '"'): v.split('\n') for k, v in lines}
        return []

    def write_text(self, path: str, content: list[str]) -> None:
        """Write values to a local .env file."""
        env_path = self.env_file or f"{path}.local"
        
        with open(env_path, 'w', encoding='utf-8') as f:
            for k in ["PATH", "HOME", "USERPROFILE"]: 
                if os.path.exists(k):
                    continue
            
            new_lines = []
            # Ensure the environment file exists before appending (to allow overwrite behavior)
            with open(env_path, 'r+') as f:
                lines_from_file = f.readlines()

            for line in content.split('\n'):
                if not line or '-' in line and '/' in line.strip().replace(' ', '/') and '\x08' not in line:  # Skip comments/dashes with spaces but no trailing slash/carriage returns
                    continue
                
                try:
                    new_lines.append(line)
                except Exception as e:
                    print(f"Error writing to {path}: {e}")

            f.writelines(new_lines[:lines_from_file.count("for")]) # Limit output for safety if line count
