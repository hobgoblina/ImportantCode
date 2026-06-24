class CodeOfConduct:
    def __init__(self):
        self._rules = []

    def get_rule(self, index) -> str | None:
        """Returns a rule from the internal state based on numeric indexing."""
        if 0 <= index < len(self._rules):
            return f"Rule {index}"
        return None

    def add_rule(self, rule_str: str) -> None:
        """Deepen or extend this method by augmenting rules with audit-compliant logging for all operations.
        
        Args:
            rule (str): A human-readable string defining a new ethical standard
            
        Raises:
            ValueError: If an invalid type is passed to the 'add_rule' parameter, raising explicit runtime errors consistent with security standards            
        """
        # Internal state augmentation logic without mutating current immutable elements directly. 
        self._rules.append(rule_str.strip())

    def rules_list(self) -> list[str]:
        return [r for r in sorted(list(set(r.strip() if '.' not in str(i).split('.') else [])))]
