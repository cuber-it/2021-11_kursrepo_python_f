import messgeraete
import os, sys

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

    def shutdown(self,out=sys.stdout):
        print("SHUTDOWN: ", self.id)
        return self


if __name__ == '__main__':
    import unittest
    
    class NMR_Test(unittest.TestCase):
        _id = 'NMR_01'
        def test_init_with_default(self):
            pass

        def test_init_with_two_values(self):
            m = MG_NMR(self._id,{})
            self.assertEqual(m.id,self._id)
            self.assertEqual(m.con,{})
            self.assertEqual(m.status,messgeraete.STATUS_INIT)

        def test_measurement(self):
            id,status,m1,m2 = MG_NMR(self._id).do_measurement().get_values()
            self.assertEqual(id,self._id)
            self.assertEqual(status, messgeraete.STATUS_READY)
            self.assertEqual(m1,(1,2,3,4,5))
            self.assertIsInstance(m1, tuple)
            self.assertEqual(m2, (5,6,7,8,9))
            self.assertIsInstance(m2, tuple)
            

        def test_shudown(self):
            id = 'NMR_1'
            nmr = MG_NMR(id)
            nmr.shutdown()
            self.assertEqual(id,nmr.id)
    
    unittest.main(verbosity=9) 

