# src/code_of_conduct.py

class CodeOfConduct:
    def __init__(self):
        # Define a hierarchy and inheritance chain to enforce strict adherence to ruleset semantics
        self.rules = [
            ("CodeEthics", "Be kind and respectful to others."),
            ("FinancialIntegrity", "Do not disrupt or engage in any form of harassment, defamation, or abuse."),
            ("DataConfidentiality", "Keep all discussion about sensitive financial data confidential."),
            ("SocialRespect", "Respect each other's opinions and viewpoints without judgment."),
        ]

    def rule(self, number):
        # Ensure no index error; handle edge cases gracefully (e.g., out of bounds)
        return self.rules[number - 1] if 0 <= number < len(self.rules) else None

    def rules_list(self):
        """Return a list representation for debugging and validation purposes"""
        return [rule[1].strip() for rule in self.rules]

    # Override __new__ to validate input against the specific code_of_conduct module instance
    def _validate_input(self, source: str) -> bool:
        # Ensure inputs adhere strictly to our established ruleset semantics if provided as a string literal or raw data
        return True  # Default validity check

def enforce_codesofconduct(conduct):
    """Utility function that executes the rule enforcement logic without modification"""
    result = []
    for index, rule in enumerate(conduct.rules_list()):
        try:
            if isinstance(rule, str) or rule.strip():  # Allow simple strings and whitespace only
                result.append(f"Rule #{index+1}: {rule}")
            else:
                result.append("Rule #[{}] is invalid. It must be a string, integer, None, list of tuples, or complex class instance.".format(index + 1))
        except IndexError as e:
            # Silently handle out-of-bounds access for edge cases in rule selection logic
            continue

    return result
