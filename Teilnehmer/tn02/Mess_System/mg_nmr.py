import messgeraete as mg
import mg_nmr
import os

class MG_NMR(mg.Messgeraet_Basis):
    kennung = "NMR"

    def __init__(self, id, con=None):
        super().__init__()
        self.id = id
        self.con = con

    def do_measurement(self):
        self.status = mg.STATUS_READY
        self._values = [ self.id, self.status, (1,2,3,4,5), (5,6,7,8,9)]
        return self

    def shutdown(self):
        print("SHUTDOWN: ", self.id)
        self.status = mg.STATUS_DOWN
        return self



if __name__ == "__main__":
    import unittest

    class MG_NMR_Tests(unittest.TestCase):
        _id = "NMR01"
        _con = "COM1"
        _kennung = "NMR"
        def setUp(self):
            self.nmr = MG_NMR(self._id, self._con)

        def test_kennung(self):
            self.assertEqual(self.nmr.kennung, self._kennung)
        
        def test_initialisierung(self):
            self.assertIsInstance(self.nmr, MG_NMR)
            self.assertEqual(self.nmr.id, self._id)
            self.assertEqual(self.nmr.con, self._con)
            self.assertEqual(self.nmr.status, mg.STATUS_INIT)
            self.assertEqual(self.nmr.get_values(), [])

        def test_do_measurement(self):
            self.assertIsInstance(self.nmr.do_measurement(), MG_NMR)

        def test_get_values(self):
            self.assertEqual(self.nmr.do_measurement().get_values(), [self._id, mg.STATUS_READY, (1,2,3,4,5), (5,6,7,8,9)])

        def test_shutdown(self):
            self.assertEqual(self.nmr.shutdown().status, mg.STATUS_DOWN)

        def tearDown(self):
            pass

    unittest.main(verbosity=9)