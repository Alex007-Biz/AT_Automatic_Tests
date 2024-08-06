import unittest
from main_HW import divide

class TestMath(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(4, 3), 1)
        self.assertEqual(divide(20, 5), 0)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)


if __name__ == '__main__':
    unittest.main()

