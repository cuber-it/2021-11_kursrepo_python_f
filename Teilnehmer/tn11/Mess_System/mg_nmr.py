import messgeraete
import os

class MG_NMR(messgeraete.Messgeraet_Basis):
    kennung = "NMR"

    def __init__(self, id, con=None):
        super().__init__()
        self.id = id
        self.con = con

    def do_measurement(self,meas_values=[]):
        self.status = messgeraete.STATUS_READY
        self._values = [ self.id, self.status, meas_values]
        return self

    def shutdown(self):
        print("SHUTDOWN: ", self.id)
        self.status = messgeraete.STATUS_SHUTDOWN
        return self

if __name__ == "__main__":
    import unittest
    class NMR_Test(unittest.TestCase):

        def test_init_with_default(self):
            self.b=MG_NMR("NMR_1")
            self.assertIsInstance(self.b,MG_NMR)
            self.assertEqual(self.b.id,"NMR_1")
            self.assertEqual(self.b.status,messgeraete.STATUS_INIT)
            self.assertEqual(self.b.con,None)

        def test_init_with_two_values(self):    
            self.b=MG_NMR("NMR_1","BT")
            self.assertIsInstance(self.b,MG_NMR)
            self.assertEqual(self.b.id,"NMR_1")
            self.assertEqual(self.b.status,messgeraete.STATUS_INIT)
            self.assertEqual(self.b.con,"BT")
        
        def test_set_measurement_set_up_correctly(self):
            self.b=MG_NMR("NMR_1")
            self.b.do_measurement([1,3,5,7])
            self.assertEqual(self.b._values[2],[1,3,5,7])
            self.assertEqual(self.b.status,messgeraete.STATUS_READY)

        def test_shutdown(self):
            self.b=MG_NMR("NMR_1")
            self.b.shutdown()
            self.assertEqual(self.b.id,"NMR_1")
            self.assertEqual(self.b.status,messgeraete.STATUS_SHUTDOWN)

    unittest.main(verbosity=2)