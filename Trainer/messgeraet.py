class Messgeraet:
    basisverbindung = "IP"

    def __init__(self, name, p1, p2=None):
        """
        Anlage des Messgerätetreibers

        @parameters: name (str) - Geräte Typ
        @parameters: p1 (int) - Geräte ID
        """
        assert isinstance(name, str), "Invalid Type for name" # Möglichkeit a - in python noch akzeptiert

        if isinstance(p1, str): # p1 muss aber int sein -  automatische Umwandlung wenn machbar
            p1 = int(p1)

        self.name = name
        self.extension = "X"
        self.p_1 = p1
        self.p_2 = p2
        
    def mach_was(self):
        print(self.name)
        print(self.p_1)
        print(self.p_2)
        print(self.basisverbindung)

    def tu_was(self):
        print("Tolle Dinge passieren hier!", self.extension)

    def __str__(self):
        return f"{self.name},{self.extension},{self.basisverbindung},{self.p_1},{self.p_2}"

if __name__ == "__main__":
    r = Messgeraet("Röntgen", 4711)
    n = Messgeraet("NMR", 4712, 123)
    s = Messgeraet("Spektroskop", 4713, 567)
    assert r.name == "Röntgen"
    assert r.extension == "X"
    assert n.name == "NMR"
    assert n.extension == "X"
    assert s.name == "Spektroskop"
    assert s.extension == "X"