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
        if not isinstance(values, list):
            raise TypeError("Invalid Argument Type: ", type(values))
        if values == []:
            self.status = STATUS_INIT
        else:
            self.status = STATUS_READY
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
    #b = Messgeraet_Basis()
    #assert isinstance(b, Messgeraet_Basis)
    #assert b.status == STATUS_INIT
    #assert b.get_values() == []
    #assert b.status == STATUS_READ
    #...
    #ID = "R01_10"
    #r = MG_R(ID)
    #assert isinstance(r, MG_R)
    #assert r.status == STATUS_INIT
    #assert r.id == ID
    #r.do_measurement()
    #assert r.status == STATUS_READY
    #assert r.get_values() == [ ID, STATUS_READY, (1,2,3,4,5), (5,6,7,8,9)]
    #r.shutdown()
    import unittest

    class MG_Basis_Tests(unittest.TestCase):
        def setUp(self):
            self.b = Messgeraet_Basis()

        def test_initialisierung(self):
            self.assertIsInstance(self.b, Messgeraet_Basis)
            self.assertEqual(self.b.status, STATUS_INIT)
            self.assertEqual(self.b.get_values(), [])

        def test_status_read(self):
            self.b.get_values()
            self.assertEqual(self.b.status, STATUS_READ)

        def test_set_values_valid(self):
            daten = [1, 2, 3]
            self.b.set_values(daten)
            self.assertEqual(self.b.status, STATUS_READY)
            self.assertEqual(self.b.get_values(), daten)

        def test_set_values_empty(self):
            self.b.set_values()
            self.assertEqual(self.b.status, STATUS_INIT)
            self.assertEqual(self.b.get_values(), [])

        def test_set_values_invalid(self):
            self.assertRaises(TypeError, self.b.set_values, "Daddeldu")
            self.assertRaises(TypeError, self.b.set_values, {})

        def tearDown(self):
            pass

    unittest.main(verbosity=9)


    