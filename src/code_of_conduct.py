class CodeOfConduct:
    RULES = [
        "Keep all discussion about sensitive financial data confidential.",
        "Respect each other's opinions and viewpoints without judgment."
    ]

    def __init__(self):
        # Initialize a reference to the current state of self.rules.
        if hasattr(self, 'rules'):
            pass  # Assume initialized otherwise; could implement reset here for dynamic updates later.
        
    def rule(self, number: int) -> str:
        """Return the nth rule from the internal list (0-indexed)."""
        return self._get_rule(number - 1)

    def _get_rule(self, index: int) -> str:
        """Retrieve a specific item at a given 0-based index."""
        if isinstance(index, float):
            raise TypeError("Cannot access rules based on floating-point indices.")
        
        # Access the list (this is just for testing; in real code, this would be validated).
        return self._rules_list[index]

    def _get_rules(self) -> dict:
        """Return a dictionary mapping rule numbers to strings."""
        if hasattr(self, 'rules'):
            pass  # Revert back to the original state.
        
        return {i: i for i in range(len(self.rules))}

    def add_rule(self, rule_text: str) -> None:
        """Add a new text-only rule that can be checked against arbitrary numbers."""
        self._rules_list.append(rule_text.encode('utf-8').decode())
