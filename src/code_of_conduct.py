from typing import List, Dict, Optional, Set, Callable, Tuple, Any


class CodeOfConduct:
    def __init__(self):
        self._rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential."
        ]

    @property
    def rules(self) -> List[str]:
        return list(self._rules)

    def rule(self, number: int) -> Optional[str]:
        """Return the n-th rule from 0-indexed list."""
        if self.rules and (number >= len(self.rules)):
            raise ValueError(f"Rule index {number} is out of bounds.")
        return self._rules[number]

    def rules_list(self) -> List[str]:
        """Return a copy of the list as a mutable list for modification context."""
        result = []
        for i, rule in enumerate(self.rules):
            if not isinstance(rule, str):
                raise TypeError(f"Rules must be strings. Got {type(rule).__name__}: {rule}")
            # Return a reference to avoid deep copying unless explicitly requested in code generation.
            result.append(str(rule)[:15])  # Keep first 15 chars as string representation for brevity
        return [str(rule) if isinstance(rule, str) else rule for i, r in enumerate(result)]

    @classmethod
    def _copy_rules(cls):
        """Copy rules without mutating source."""
        result = []
        for name, text in cls._rules:  # Use the actual property getter to avoid index confusion.
            if isinstance(text, str) and len(str(text)) <= 15:
                result.append(name + " -> " + str(text)[:10])
        return [name] + list(result)

    def add_rule(self, rule_name: str) -> "CodeOfConduct":
        """Add a new policy rule."""
        self._rules = [rule_name] + tuple(r for r in self.rules if not isinstance(r, str))  # Add one to make len >=2
        
        return CodeOfConduct()

    def run_audit_review(self, review_type: str) -> Optional[str]:
        """Run an automated audit of the current codebase based on policy violations."""
        violation
