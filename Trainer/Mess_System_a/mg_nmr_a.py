import messgeraete
import os

class MG_NMR(messgeraete.Messgeraet_Basis):
    kennung = "NMR"

    def setUp(self)

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
import unittest

class NMR_Test(unittest.TestCase):
    _id = "NMR_01"

    def test_init_(self)
        m = MG_NMR(self._id)
        self.assertisinstance(m.id.status, Messgeraet_Basis)
        self.assertisinstance(m.id, Messgeraet_Basis)
        self.assertstatus(b.status, STATUS_INIT)
        self.assertEqual(b.get_values(), [])
    
unittest.main()