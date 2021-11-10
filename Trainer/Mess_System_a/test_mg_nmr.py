import unittest
import mg_nmr
import messgeraete

class NMR_Test_Init(unittest.TestCase):
    _id = "NMR_01"

    def test_init_with_default(self):
        m = mg_nmr.MG_NMR(self._id)
        self.assertEqual(m.id, self._id)
        self.assertEqual(m.con, None)
        self.assertEqual(m.status, messgeraete.STATUS_INIT)

    def test_init_with_two_values(self):
        m = mg_nmr.MG_NMR(self._id, {})
        self.assertEqual(m.id, self._id)
        self.assertEqual(m.con, {})
        self.assertEqual(m.status, messgeraete.STATUS_INIT)

class NMR_Test_Misc(unittest.TestCase):
    _id = "NMR_01"

    def setUp(self):
        self.m = mg_nmr.MG_NMR(self._id)

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

if __name__ == "__main__":
    unittest.main(verbosity=9)