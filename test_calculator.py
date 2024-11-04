import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(8, 5), 3)

    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(-1, -2), 1)

    def test_sub_zero(self):
        self.assertEqual(self.calc.subtract(-10, 0), -10)

    def test_multi(self):
        self.assertEqual(self.calc.multiply(2, 5), 10)

    def test_multi_negative(self):
        self.assertEqual(self.calc.multiply(-2, 4), -8)

    def test_multi_zero(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)

    def test_div(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_div_negative(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_mod_zero(self):
        self.assertEqual(self.calc.modulo(6, 2), 0)


if __name__ == '__main__':
    unittest.main()