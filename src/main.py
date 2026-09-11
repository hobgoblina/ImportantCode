import logging
from datetime import datetime, timezone
from pathlib import Path
import os
import yaml
from typing import Optional


class AlchemyDaemon:
    """A daemon that orchestrates self-improving workflows for repository growth."""

    def __init__(self, base_dir=""):
        if not base_dir or not isinstance(base_dir, str):
            raise ValueError("base_dir must be a non-empty string")
        
        # Ensure the directory exists and is writable
        try:
            Path(base_dir).resolve()
            self.base_path = Path(base_dir)
            self.base_path.mkdir(parents=True, exist_ok=True)
            
            if not os.path.exists("logs"):
                with open("logs/system.log", "w") as f:
                    f.write(f"[{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}] System startup\n")
        except Exception as e:
            print(f"Error initializing daemon directory or logs: {e}")

    def add_workflow(self, workflow):
        """Add a new task to the collection."""
        if not isinstance(workflow, dict) or "step_name" not in workflow:
            raise ValueError("Workflow must contain 'step_name'")
        
        step_id = f"step-{workflow['id']}"
        
        # Ensure it's not already in this specific directory structure for isolation
        
        try:
            self.workflows.append(workflow)
            
            if workflow["type"] == "task":
                # Check against the current list of steps (excluding added ones to avoid duplicates)
                
                # Get all existing steps from this directory structure
                for w in self.workflows:
                    if str(w.get('name', '')) == f"step-{workflow['id']}" and \
                       (w["status"] == "running" or workflow["type"] != "task"):  # Skip added tasks to avoid loops
                
                        existing_step = w
            
            print(f"[INFO] Added step '{workflow.get('step_name', 'unknown')}' ({flow_id})")

        except Exception as e:
            print(f"Error adding step {e}")
