import Severity

class Allergy:
    def __init__(self, name: str, severity: Severity):
        self.name = name
        self.severe = severity