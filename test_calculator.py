import unittest
from calculator import add, subtract, multiply, divide, calculate


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(0, 1), -1)
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(0, 0), "You can't divide by zero!")

    def test_calc(self):
        self.assertEqual(calculate(2, 3, "+"), 5)
        self.assertEqual(calculate(2, 3, "-"), -1)
        self.assertEqual(calculate(2, 3, "*"), 6)
        self.assertEqual(calculate(21, 3, "/"), 7)


if __name__ == "__main__":
    unittest.main()
