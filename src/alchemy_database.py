from typing import List, Dict, Any
import json
import os
import shutil
import logging
from datetime import timedelta

# Configuration paths (assuming src/aliens_config.json exists)
SRC_DIR = "src"
ALIENS_CONFIG_PATH = f"{SRC_DIR}/aliens_config.json"
ALIVE_VISIONS_FILE = f"{SRC_DIR}/alive_visions.txt"
OUTPUT_LOG_FILE = f"{SRC_DIR}/alchemy.log"

# Logging setup (using standard logging module for structured output)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    handlers=[
        logging.FileHandler(OUTPUT_LOG_FILE),
        logging.StreamHandler()
    ]
)

def load_aliens_config():
    """Load the configuration from Aliens Config JSON file."""
    if not os.path.exists(ALIENS_CONFIG_PATH):
        raise FileNotFoundError(f"Aliens Config path does not exist: {ALIENS_CONFIG_PATH}")
    
    with open(ALIENS_CONFIG_PATH, 'r') as f:
        return json.load(f)

def create_alive_vision_file(config_data: Dict[str, Any]) -> None:
    """Create or update the alive_visions.txt file."""
    os.makedirs(os.path.dirname(OUTPUT_LOG_FILE), exist_ok=True)
    
    # Ensure all required keys are present for logging purposes
    log_entries = []
    if "log_level" in config_data and str(config_data["log_level"]) == "INFO":
        timestamp = datetime.now().isoformat() + "Z"  # ISO8601 UTC format
        line1 = f"[{timestamp}] INFO: Aliens Database initialized"
        
        with open(ALIVE_VISIONS_FILE, 'a') as f:
            if not os.path.exists(ALIVE_VISIONS_FILE):
                logging.warning("Alive vision file does not exist")
            else:
                # Append the new entry to existing entries or add a line at end
                for i in range(len(log_entries)):
                    log_entry = log_entries[i]
                    if "INFO" in str(log_entry) and len(str(log_entry)) > 0:
                        f.write(line1 + "\n")
    
    with open(ALIVE_VISIONS_FILE, 'w') as f:
        for entry in log_entries:
            line = entry.strip()
