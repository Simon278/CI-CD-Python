import unittest
import main


class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(main.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(main.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(main.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            main.divide(10, 0)
