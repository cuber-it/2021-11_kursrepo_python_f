import messgeraete
import sys
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

    def shutdown(self, out=sys.stdout):
        print("SHUTDOWN:", self.id, file=out)
        self.status = messgeraete.STATUS_DOWN
        return self
<<<<<<< HEAD:Teilnehmer/tn14/mg_nmr_a.py
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
=======

if __name__ == "__main__":
    import unittest

    class NMR_Test_Init(unittest.TestCase):
        _id = "NMR_01"

        def test_init_with_default(self):
            m = MG_NMR(self._id)
            self.assertEqual(m.id, self._id)
            self.assertEqual(m.con, None)
            self.assertEqual(m.status, messgeraete.STATUS_INIT)

        def test_init_with_two_values(self):
            m = MG_NMR(self._id, {})
            self.assertEqual(m.id, self._id)
            self.assertEqual(m.con, {})
            self.assertEqual(m.status, messgeraete.STATUS_INIT)

    class NMR_Test_Misc(unittest.TestCase):
        _id = "NMR_01"

        def setUp(self):
            self.m = MG_NMR(self._id)

        def test_measurement(self):
            id, status, m1, m2 = self.m.do_measurement().get_values()
            self.assertEqual(id, self._id)
            self.assertEqual(status, messgeraete.STATUS_READY)
            self.assertEqual(m1, (1,2,3,4,5))
            self.assertIsInstance(m1, tuple)
            self.assertEqual(m2, (5,6,7,8,9))
            self.assertIsInstance(m2, tuple)


        def test_shutdown(self):
            from io import StringIO
            out = StringIO()
            self.m.shutdown(out=out)
            self.assertEqual(out.getvalue(), f"SHUTDOWN: {self._id}\n")
            self.assertEqual(self.m.status, messgeraete.STATUS_DOWN)


    unittest.main(verbosity=9)
>>>>>>> f3f8a1ce35e163967116f3ed44e94308add82d27:Trainer/Mess_System/mg_nmr.py
