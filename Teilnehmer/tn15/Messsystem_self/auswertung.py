class Roentgen:
    def __init__(self, daten):
        self.daten = daten

    def analyze(self):
        return self

    def report(self, output_target = None):
        if output_target is None:
            print(self.daten)