class Messgeraet:
    def __init__(self, name, p1, p2=None):
        self.name = name
        self.extension = "X"
        self.p_1 = p1
        self.p_2 = p2
    
    def mach_was(self):
        print(self.name)
        print(self.p_1)
        print(self.p_2)

    def tu_was(self):
        print("Tolle Dinge passieren hier!", self.extension)

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