class Basis: # Modifikation der ursprünglichen Basis
    def __init__(self, text=None):
        self.text = text

    def read(self, datei=None):
        if datei:
            self.text = datei.read()
        else:
            self.text = input("Eingabe: ")
        return self

    def write(self, datei=None):
        if datei:
            print(self.text, file=datei)
        else:
            print(self.text)
        return self

    def bearbeite_text(self):
        self.text = self.text.upper()
        return self