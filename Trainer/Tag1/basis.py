class Basis:
    def __init__(self, text=None):
        self.text = text

    def read(self):
        self.text = input("Eingabe: ")
        return self

    def write(self):
        print(self.text)
        return self

    def bearbeite_text(self):
        self.text = self.text.upper()
        return self