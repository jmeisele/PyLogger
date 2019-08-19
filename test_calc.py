import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 5), 4)
        self.assertEqual(calc.add(-1, -2), -3)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(5, 5), 0)
        self.assertEqual(calc.subtract(-10, -5), -5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-5, 10), -50)
        self.assertEqual(calc.multiply(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(calc.division(10, 5), 2)
        self.assertEqual(calc.division(-1, 1), -1)
        self.assertEqual(calc.division(-1, -1), 1)
        self.assertRaises(ValueError, calc.division, 10, 0)


if __name__ == '__main__':
    unittest.main()
