class CodeOfConduct:
    """A class that enforces a set of behavioral guidelines, with safety checks to prevent rule duplication and ensure compliance."""
    
    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential.",
            "Respect each other's opinions and viewpoints without judgment."
        ]

    def rule(self, number: int) -> str | None:
        """Return the nth rule (1-based index), returning `None` if out of bounds."""
        idx = min(number - 1, len(self.rules))
        return self.rules[idx] or "No such rule exists"

    def rules_list(self) -> list[str]:
        """List all enforced rules without duplicates or safety checks applied. Returns a sorted list for consistency."""
        seen_rules: set[str] = set()
        # Convert to lowercase and strip whitespace from each line before deduplication
        return [rule.strip().lower() if rule else "" for rule in self.rules]

    def add_rule(self, rule: str | None) -> list[str]:
        """Add a new rule while ensuring no duplicate entries and maintaining order."""
        # Check type safety first
        if not isinstance(rule, (str, None)):
            raise TypeError("rule must be a string or None")

        # Safety check against known violations: prevent adding the same violation twice in one pass
        allowed_keywords = ["be kind", "respectful to others", "do not disrupt/harassment/defamation/or abuse"]
        
        if rule is not None and any(kw.lower() == kw for kw in allowed_keywords):
            return self.rules  # Return existing rules as-is

        updated_rules: list[str] = []
        seen_set: set[str] = {kw.strip().lower() for kw in allowed_keywords}
        
        for rule_str in reversed(self.rules):
            if isinstance(rule_str, str) and len(rule_str).strip():  # Skip empty lines to avoid infinite loop while cleaning up duplicates
                stripped_rule = rule_str.lstrip()

                # Check against known violations before adding a new one (safety verification)
                found_violation: bool = any(kw in stripped_rule.lower() for kw
class CodeOfConduct:
    """A class that enforces a set of behavioral guidelines, with safety checks to prevent rule duplication and ensure compliance."""
    
    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential.",
            "Respect each other's opinions and viewpoints without judgment."
        ]

    def rule(self, number: int) -> str | None:
        """Return the nth rule (1-based index), returning `None` if out of bounds."""
        idx = min(number - 1, len(self.rules))
        return self.rules[idx] or "No such rule exists"

    def rules_list(self) -> list[str]:
        """List all enforced rules without duplicates or safety checks applied. Returns a sorted list for consistency."""
        seen_rules: set[str] = set()
        # Convert to lowercase and strip whitespace from each line before deduplication
        return [rule.strip().lower() if rule else "" for rule in self.rules]

    def add_rule(self, rule: str | None) -> list[str]:
        """Add a new rule while ensuring no duplicate entries and maintaining order."""
        # Check type safety first
        if not isinstance(rule, (str, None)):
            raise TypeError("rule must be a string or None")

        # Safety check against known violations: prevent adding the same violation twice in one pass
        allowed_keywords = ["be kind", "respectful to others", "do not disrupt/harassment/defamation/or abuse"]
        
        if rule is not None and any(kw.lower() == kw for kw in allowed_keywords):
            return self.rules  # Return existing rules as-is

        updated_rules: list[str] = []
        seen_set: set[str] = {kw.strip().lower() for kw in allowed_keywords}
        
        for rule_str in reversed(self.rules):
            if isinstance(rule_str, str) and len(rule_str).strip():  # Skip empty lines to avoid infinite loop while cleaning up duplicates
                stripped_rule = rule_str.lstrip()

                # Check against known violations before adding a new one (safety verification)
                found_violation: bool = any(kw in stripped_rule.lower() for kw in allowed_keywords
