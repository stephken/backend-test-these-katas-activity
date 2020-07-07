import unittest
import katas
import math


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(2, 3), 2 + 3)

    def test_multiply(self):
        self.assertEqual(katas.multiply(2, 3), 2 * 3)

    def test_power(self):
        self.assertEqual(katas.power(2, 3), math.pow(2, 3))

    def test_factorial(self):
        self.assertEqual(katas.factorial(3), math.factorial(3))

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(9), 21)


if __name__ == '__main__':
    unittest.main()
