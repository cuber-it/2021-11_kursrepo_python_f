import messgeraete
import os
import sys

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

    def shutdown(self, out=sys.stdout):
        self.status = messgeraete.STATUS_SHUTDOWN
        print("SHUTDOWN:", self.id, file=out)
        return self


if __name__ == "__main__":
    import unittest  # am besten Test in eigene Datei

    class NMR_Test(unittest.TestCase):

        def test_init_with_default(self):
            id_value = 'NMR_001'
            b = MG_NMR(id_value)
            self.assertEqual(b.id, id_value)
            self.assertEqual(b.con, None)
            self.assertEqual(b.kennung, "NMR")
        
        def test_init_with_two_values(self):
            id_value = 'NMR_001'
            con_value = 'head_scan'
            b = MG_NMR(id_value, con_value)
            self.assertEqual(b.id, id_value)
            self.assertEqual(b.con, con_value)
            self.assertEqual(b.kennung, "NMR")

        def test_measurement(self):
            id_value = 'NMR_001'
            b = MG_NMR(id_value)
            id, status, m1, m2 = b.do_measurement().get_values()
            self.assertEqual(status, messgeraete.STATUS_READY)
            self.assertEqual(id, id_value)
            self.assertEqual(m1, (1,2,3,4,5))
            self.assertIsInstance(m1, tuple)
            self.assertEqual(m2, (5,6,7,8,9))
            self.assertIsInstance(m2, tuple)

        def test_shutdown(self):
            from io import StringIO
            out = StringIO()
            id_value = 'NMR_001'
            b = MG_NMR(id_value)
            b.shutdown(out=out)
            self.assertEqual(out.getvalue(), f"SHUTDOWN: {b.id}\n")
            self.assertEqual(b.status, messgeraete.STATUS_SHUTDOWN)
        
        def tearDown(self):
            pass


        
    unittest.main(verbosity=9)