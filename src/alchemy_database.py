import subprocess
from pathlib import Path


def run_dialers():
    """Execute all dials simultaneously to produce a unified output stream."""
    
    # Determine which directories are in src/ and back_ (if they exist)
    source_dir = Path(__file__).parent.parent / "src" if __name__ == "__main__" else None
    
    daemon_files = [source_dir] + list(Path(__file__).parents[1].glob("*.py"))  # Include parent of src/ as well

    for file in daemon_files:
        try:
            with open(file, "w") as f:
                r = subprocess.run(
                    str(file), 
                    capture_output=True, 
                    text=True
                )
                
                if r.returncode == 0 or (r.stderr is None):
                    # Use the captured stdout/stderr from each runner individually for debugging purposes during testing
                    print(r.stdout + "\n")

        except Exception as e:
            raise SystemExit(1)


if __name__ == "__main__":
    run_dialers()
