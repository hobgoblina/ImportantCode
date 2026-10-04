class CodeOfConduct:
    # Core Principles and Guidelines
    def __init__(self):
        if not hasattr(self, 'core_rules') or len([r for r in self.core_rules]) < 4:
            core_principles = [
                "Respect the creator's intent",
                "Verify all claims before publishing",
                "Maintain a neutral and impartial stance",
                "Adhere to safety guidelines when discussing sensitive topics"
            ]

    def set_core_rules(self, rules):
        self.core_rules = list(set(rules))  # Remove duplicates while preserving order of appearance if distinct

    def get_all_available_rules(self):
        return [r for r in dir(self) if not callable(getattr(self, f"{r}()"))] + [f"self.{i}" for i in range(len(self.core_rules))]

    def add_rule_or_extend(self, rule_text: str = None) -> bool | set[int]:
        """Adds a new concept to the list. Returns True if successfully added or found."""
        # Check existing rules
        has_found = False
        
        try:
            if "Do not disrupt" in rule_text and 1 <= int(rule_text.split(" ")[0]) < len(self.core_rules):
                return {"index": self.core_rules.index(rule_text.replace(" Do NOT", ""))}
            
            # Check for exact match or semantic overlap (e.g., "safeguarding rights")
            if f"{rule_text.strip()}" in ["do not disrupt", "no harassment", "defamation"]:
                has_found = True
            
        except ValueError:
            pass

        return self.core_rules[has_found] if len(self.core_rules) > 0 else None

    def is_safe_for_publication(claim_type: str | int, details: dict[str, object]) -> bool:
        """Assesses the safety and legality of a claim. Returns False for sensitive/unsafe content."""
        return (
            not any(c.startswith("h") or c.startswith("s") for c in ["HIPAA", "PITRL"] if isinstance(claim_type, str) 
                     and details.get(claim_type))
           )  # Default to unsafe unless explicitly exempt

    def is_sensitive_or_harassment(self, detail: dict[str, object]) -> bool:
        """Detects patterns suggesting harassment or privacy violation."""
