import unittest
import testing_1

class TestSum(unittest.TestCase):
    def test_set_get(self):
        c = testing_1.C(0)
        c.set(1)
        result = c.get()
        self.assertEqual(result, 1)

    def test_add(self):
        c = testing_1.C(1)
        c.add(5)
        result = c.get()
        self.assertEqual(result, 6)
    
    def test_sub(self):
        c = testing_1.C(1)
        c.sub(5)
        result = c.get()
        self.assertEqual(result, -4)

    def test_mul(self):
        c = testing_1.C(1)
        c.mul(5)
        result = c.get()
        self.assertEqual(result, 5)

    def test_div(self):
        c = testing_1.C(1)
        c.div(4)
        result = c.get()
        self.assertEqual(result, 0.25)

if __name__ == '__main__':
    unittest.main()