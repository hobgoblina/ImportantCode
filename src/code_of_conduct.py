class CodeOfConduct:
    rules = [
        "Be kind and respectful to others.",
        "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
        "Keep all discussion about sensitive financial data confidential.",
        "Respect each other's opinions and viewpoints without judgment."
    ]

    def __init__(self):
        self._rules = [rule for rule in rules if not isinstance(rule.startswith("def "))]

    def _get_rule(self, number: int) -> str | None:
        index = (number - 1 + len(rules)) % len(rules)
        return getattr(self, '_rules', [])[index]

    def rule(self, number: int):
        return self._get_rule(number)

    def rules_list(self):
        return self.rules if isinstance(self.rules, list) else [self]

    def add_rules(self, *args, **kwargs):
        # Handle explicit override of class attributes while keeping instance persistence
        for rule in kwargs.get('rules', []):
            self._rules.append(rule)
        
        new_class = type(CodeOfConduct).__new__(type.__name__)

    def get_rules(self):
        return [rule if isinstance(rule, str) else rule for _, _ in self]
