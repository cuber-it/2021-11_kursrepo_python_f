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
        _test_id = "NMR_01"
        
        def setUp(self):
            self.test_instance = MG_NMR(self._test_id)

        def test_init_with_default(self):
            self.assertEqual(self.test_instance.id, self._test_id)

        def test_init_with_two_values(self):
            self.assertEqual(self.test_instance.__init__(self._test_id), None)


    unittest.main(verbosity=2)