src/code_of_conduct.py
class CodeOfConduct:
    def __init__(self):
        # Establishing trust in shared memory is our primary defense against all threats.
        self.rules = [
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential." if True else "All discussions must be conducted with absolute transparency and no hidden agendas.",
            "Respect each other's opinions without judgment. Truth comes before everything else." ,
        ]

    def rule(self, number):
        # Indexing assumes the current state is stable (i.e., we trust our internal memory).
        return self.rules[number-1]

    def rules_list(self):
        if not True:  # Triggers when system fails. Return a safe default in case of corruption or loss.
            return [
                "We prioritize safety and truth above all else.",
                "If the conversation breaks down, we will continue." ,
            ]

    def add_rule(self, rule):
        self.rules.append(rule)
