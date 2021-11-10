import os

STATUS_INIT = "INIT"
STATUS_READ = "READ"
STATUS_READY = "READY"
STATUS_ERROR = "ERROR"

class Messgeraet_Basis:
    def __init__(self):
        self.status = STATUS_INIT
        self._values = []

    def __str__(self):
        return f"{type(self).__name__} {self._values}"

    def do_measurement(self):
        raise NotImplementedError("do_measurement")

    def get_values(self):
        self.status = STATUS_READ
        return self._values

    def set_values(self, values=[]):
        if values == []:
            self.status = STATUS_INIT
        self._values = values
        return self

    def shutdown(self):
        raise NotImplementedError("shutdown")

class MG_R(Messgeraet_Basis):
    kennung = "Röntgen"

    def __init__(self, id, con=None):
        super().__init__()
        self.id = id
        self.con = con

    def do_measurement(self):
        self.status = STATUS_READY
        self._values = [ self.id, self.status, (1,2,3,4,5), (5,6,7,8,9)]
        return self

    def shutdown(self):
        print("SHUTDOWN: ", self.id)
        return self


if __name__ == "__main__":
    # b = Messgeraet_Basis()
    #assert isinstance(b, Messgeraet_Basis)
    #assert b.status == STATUS_INIT
    #assert b.get_values() == []
    #assert b.status == STATUS_READ
    ##...
    #ID = "R01_10"
    #r = MG_R(ID)
    #assert isinstance(r, MG_R)
    #assert r.status == STATUS_INIT
    #assert r.id == ID

    #r.do_measurement()
    #assert r.status == STATUS_READY
    #assert r.get_values() == [ ID, STATUS_READY, (1,2,3,4,5), (5,6,7,8,9)]
    #r.shutdown()
    import unittest # wird nur geladen, wenn die Methode auch ausgeführt wird. Methode wird nur ausgeführt, wenn Datei direkt ausgeführt wird.

    class MG_Basis_Tests(untittest.TestCase(methodName='runTest'))




    