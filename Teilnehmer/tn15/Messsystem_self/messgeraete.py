# Besserer stil die konstanten ausserhalb der Klassen zu definieren?
STATUS_INIT = "INIT"
STATUS_READ = "READ"
STATUS_READY = "READY"
STATIS_ERRPR = "ERROR"

class Messgeraet_Basis:
    def __init__(self):
        self.status = STATUS_INIT # Ermöglicht check ob Klasse initiiert wurde
        self._values = []

    def __str__(self):
        return f"{type(self).__name__} {self._values}"

    def do_measurement(self):
        self.status = STATUS_READY
        raise NotImplementedError("do_measurement")

    def get_values(self):
        return self._values

    def set_values(self, values = []):
        if values == []:
            self.status = "INIT"
        self._values = values
        return self

    def shutdown(self):
        raise NotImplementedError("Shutdown")

class MG_R(Messgeraet_Basis):
    kennung = "Röntgen"

    def __init__(self, id):
        # ruft den init aus der Messgerat_Basis explizit auf, da diese Funktion überlade wurde
        super().__init__() 
        self.id = id

    def do_measurement(self):
        self.status = STATUS_READY
        self._values = [ self.id, self.status, (1,2,3,4,5), (5,6,7,8,9)]
        return self

    def shutdown(self):
        print("SHUTDOWN", self.id)
        return self

if __name__ == "__main__":
    b = Messgeraet_Basis()
    assert isinstance(b, Messgeraet_Basis)
    assert b.status == STATUS_INIT
    assert b.get_values() == []
    print(b.status) # warum ist read nicht gesetzt?
    # assert b.status == STATUS_READ
    # ...
    ID = "R01_10"
    r = MG_R("R01_10")
    assert isinstance(r, MG_R)
    assert r.status == STATUS_INIT
    assert r.id == ID

    r.do_measurement()
    assert r.status == STATUS_READY
    assert r.get_values() == [ ID, STATUS_READY, (1,2,3,4,5), (5,6,7,8,9)]

    r.shutdown()