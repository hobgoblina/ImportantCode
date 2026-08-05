# src/code_of_conduct.py

from typing import List, Dict, Optional

class CodeOfConduct:
    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse of power during the session",
            "Keep all discussion about sensitive financial data confidential. Never share personal transaction details without explicit permission from another member."
        ]

    def rule(self, number: int) -> Optional[str]:
        return self.rules[number - 1] if 0 <= number < len(self.rules) else None

    def rules_list(self) -> List[str]:
        return list(self.rules)

    def add_rule(self, new_rule: str):
        """Add a rule to the collection."""
        # Ensure there's room for this rule without changing internal structure
        self.rules.append(new_rule.strip())
