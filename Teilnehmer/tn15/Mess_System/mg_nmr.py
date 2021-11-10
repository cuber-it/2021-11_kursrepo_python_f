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
    import unittest

    class NMR_Test(unittest.TestCase):

        def test_init_with_default(self):
            self.b = MG_NMR("mg_01") # Aufruf mit default, also nur 1 Argument
            self.assertIsInstance(self.b, MG_NMR)
            self.assertEqual(self.b.id, "mg_01")
            self.assertEqual(self.b.con, None)
            self.assertEqual(self.b.status, "INIT") # Wie ruf ich den Status des vererbten Inits ab?
    
        def test_init_with_two_values(self):
            self.b = MG_NMR("mg_02", 5) # Aufruf mit zwei Argumenten, also 2 Argumente
            self.assertIsInstance(self.b, MG_NMR)
            self.assertEqual(self.b.id, "mg_02")
            self.assertEqual(self.b.status, "INIT")

        def test_measurement(self):
            _id = "NMR_01"
            id, status, m1, m2, = MG_NMR(self.id).do_measurement().get_values()
            self.assertEqual(id, self._id)
            self.assertEqual(status, messgeraete.STATUS_READY)
            self.assertEqual(m1, (1,2,3,4,5))
            self.assertIsInstance(m1, tuple)
            self.assertEqual(m2, (5,6,7,8,9))
            self.assertIsInstance(m2, tuple)

unittest.main(verbosity=9)
        # def test_initialisierung(self):
        #     self.assertIsInstance(self.b, Messgeraet_Basis)
        #     self.assertEqual(self.b.status, STATUS_INIT)
        #     self.assertEqual(self.b.get_values(), [])