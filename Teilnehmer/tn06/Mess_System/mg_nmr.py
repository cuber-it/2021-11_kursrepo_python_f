import messgeraete
import os
import io
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

    def shutdown(self):
        print("SHUTDOWN:", self.id)
        return self

if __name__ == "__main__":
    import unittest

    class NMR_Test(unittest.TestCase):
        def test_init_with_default(self):
            id = "NMR"
            nmr = MG_NMR(id)
            self.assertIsInstance(nmr, MG_NMR)
            self.assertEqual(nmr.id, id)
            self.assertIsNone(nmr.con)
            self.assertEqual(nmr.kennung, "NMR")
            self.assertEqual(nmr.status, messgeraete.STATUS_INIT)

        def test_init_with_two_values(self):
            id = "NMR"
            con = "Eth"
            nmr = MG_NMR(id, con)
            self.assertIsInstance(nmr, MG_NMR)
            self.assertEqual(nmr.id, id)
            self.assertEqual(nmr.con, con)
            self.assertEqual(nmr.kennung, "NMR")
            self.assertEqual(nmr.status, messgeraete.STATUS_INIT)
        
        def test_measurement(self):
            id = "NMR"
            con = "Eth"
            nmr = MG_NMR(id, con)
            meas = nmr.do_measurement()
            self.assertEqual(nmr.status, messgeraete.STATUS_READY)
            self.assertIsInstance(meas, MG_NMR)
            self.assertEqual(nmr.kennung, "NMR")
            self.assertEqual(nmr.status, messgeraete.STATUS_READY)
        
        def test_shutdown(self):
            id = "NMR"
            con = "Eth"
            nmr = MG_NMR(id, con)
            capturedOutput = io.StringIO()          # Create StringIO object
            sys.stdout = capturedOutput                   #  and redirect stdout.
            nmr.shutdown()                                 # Call unchanged function.
            sys.stdout = sys.__stdout__                   # Reset redirect.
            self.assertEqual(capturedOutput.getvalue(), f"SHUTDOWN: {id}\n")




    unittest.main(verbosity=2)