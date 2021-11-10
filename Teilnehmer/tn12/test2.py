class MessG:
    VERBINDUNG = "IP"
    def __init__(self, name:str , p1, p2=None) -> None:
        """
        Es werden tolle Dinige inizialisiert
        @parameters: name(str) - Geratename
        @parameters: p1(int) - Geraetetyp
        @parameters: p2(int) - Geraetevariante
        """
        assert isinstance(name, str), "Falscher Type für name, str erforderlich"
        self.name=name
        self.p_1=p1
        self.p_2=p2

    def mach_was(self):        
        print(self.name)
        print(self.p_1)
        print(self.p_2)

    def __str__(self):
        return f"{self.name},{self.p_1},{self.p_2},{self.VERBINDUNG}"

if __name__ == "__main__":
    o=MessG("Röntgen",4711,2)
    print(o.p_1, o.p_2)
    o.mach_was()
    print(str(o))

