import unittest


class MG_Basis_Tests(unittest.TestCase):
    def setUp(self):
        print("Init ...")
        self.b = Messgeraet_Basis()

    def test_initialisierung(self):
        self.assertIsInstance(self.b, Messgeraet_Basis)
        self.assertEqual(self.b.status, STATUS_INIT)
        self.assertEqual(self.b.get_values(), [])

    def test_status_read(self):
        self.b.get_values()
        self.assertEqual(self.b.status, STATUS_READ)

    def test_set_values_valid(self):
        daten = [1, 2, 3]
        self.b.set_values(daten)
        self.assertEqual(self.b.status, STATUS_READY)
        self.assertEqual(self.b.get_values(), daten)

    def test_set_values_empty(self):
        self.b.set_values()
        self.assertEqual(self.b.status, STATUS_INIT)
        self.assertEqual(self.b.get_values(), [])

    def test_set_values_invalid(self):
        self.assertRaises(TypeError, self.b.set_values, "Daddeldu")

    def tearDown(self):
        print("Ende des Tests")
    
    unittest.main(verbosity=9)

