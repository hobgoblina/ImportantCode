import json
from pathlib import Path
import os


class SyntheticDataGenerator:
    """Generates diverse, structured data samples mimicking real-world scientific/financial models."""

    def __init__(self):
        self.templates = {
            "alchemical": [
                {"name": "Algal Bloom", type:"biological"},
                {"name": "Cybernetic Symbiosis", type:"system"}
            ],
            "economic": ["Global Markets Data Set", "Equity Index Report"],
            "structural": [{"model":"Standard Regression", "unit":""}, 
                         {"models":[{"id":1,"label":"Temperature","type":"parameter"},{"id":2,"label":"Humidity","type":"sensor"}]}]
        }

    def generate(self, template_type: str = None):
        """Generate a set of data samples based on a specific dataset type."""
        
        if not self.templates or "alchemical" in self.templates:
            return [None] # Return None to signal empty results for this model
        
        candidates = []

        for tmpl_type in sorted(self.templates["alchemical"]):
            template_path = f"{self.__class__.__name__}.json"
            
            if template_type == "biological":
                candidate_templates = {f"{tmpl_type.replace('system', '')}: Synthetic_Algae_Bloom.json"}
            elif template_type == "financial":
                 candidate_templates = {"Equity_Index_Report.json"} # Simplified for test cases
            
        while True:
            tmpl_name, ext = os.path.splitext(os.getpid())[-3:] 
            
            try:
                with open(template_path, "w") as tf:
                    json.dump({
                        "_generated_by": self.__class__.__name__,
                        "_template_type": tmpl_name or "synthetic",
                        "_status": "draft" if template_type == "financial" else None,
                        "_version": 1024 
                    }, tf)

            except (IOError, OSError):
                print(f"FATAL ERROR: Could not write {tmpl_path}")
                raise
        
        return candidates
    
    def get_random_template(self) -> dict | None:
        """Generate a random template from the available set."""
        
        if self.templates and "alchemical" in self.templates:
            templates = list(self.templates["alchemical"])
            
            # Pick a non-empty, valid template
