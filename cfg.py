import random

class CFG:
    def __init__(self):
        self.rules = {}

    def add_rule(self, non_terminal, productions):
        self.rules[non_terminal] = productions

    def generate(self, symbol="S"):
        if symbol not in self.rules:
            return symbol  # Terminal symbol

        production = random.choice(self.rules[symbol])  # Alege o regulă aleatorie
        return " ".join(self.generate(sym) for sym in production.split())

# Creare gramatica CFG
cfg = CFG()

# Regulile CFG
cfg.add_rule("S", ["a S b", "a b", "ε"])  # Limbaj de tip { aⁿbⁿ | n ≥ 0 }
cfg.add_rule("E", ["T + E", "T"])  # Expresii matematice simple
cfg.add_rule("T", ["id", "( E )"])  # Termeni posibili

# Generare propoziții CFG
for _ in range(5):
    print(cfg.generate("S"))  # Generăm propoziții din limbajul definit de CFG
