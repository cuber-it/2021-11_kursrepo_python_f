import messgeraete
import os

class MG_NMR(messgeraete.Messgeraet_Basis):
    kennung = "NMR"

    def __init__(self, id, con=None):
        super().__init__()
        self.id = id
        self.con = con

    def do_measurement(self):
        self.status = messgeraete.STATUS_READY
        self._values = [ self.id, self.status, (1,2,3,4,5), (5,6,7,8,9)]
        return self

    def shutdown(self):
        print("SHUTDOWN: ", self.id)
        return self

if __name__ == "__main__":

    #r.do_measurement()
    #assert r.status == STATUS_READY
    #assert r.get_values() == [ ID, STATUS_READY, (1,2,3,4,5), (5,6,7,8,9)]

    import unittest

    class MG_NMR_Tests(unittest.TestCase):
        def setUp(self):      # setUp wird am Anfang immer vor JEDEM Test aufgerufen
            self.ID = "kdfmwsoe"
            self.n = MG_NMR(self.ID)

        def test_init_with_default(self):            # methoden für die Tests müssen mit test anfangen
            self.assertIsInstance(self.n, MG_NMR)
            self.assertEqual(self.n.status, messgeraete.STATUS_INIT)
            self.assertEqual(self.n.id, self.ID)

        def test_init_with_twovalues(self):            # methoden für die Tests müssen mit test anfangen
            convalue="test"
            self.n = MG_NMR(self.ID, con=convalue)
            self.assertIsInstance(self.n, MG_NMR)
            self.assertEqual(self.n.status, messgeraete.STATUS_INIT)
            self.assertEqual(self.n.id, self.ID)
            self.assertEqual(self.n.con, convalue)

        def test_do_measurement(self):
            self.n.do_measurement()
            self.assertEqual(self.n.status, messgeraete.STATUS_READY)

        def test_get_values(self):
            self.n.do_measurement()
            self.n.get_values() == [ self.ID, messgeraete.STATUS_READY, (1,2,3,4,5), (5,6,7,8,9)]

        def tearDown(self):   # auch vordefiniert und wird nach JEDEM Test ausgeführt
            print("Ende Test")

    unittest.main(verbosity=9)
