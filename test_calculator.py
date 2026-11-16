# GitHub Respository URL: https://github.com/nimma-aryan/Lab11.git
# Partern 1:
# Partern 2: Rhiannon Harpe


import unittest
import calculator
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(3, 5), -2)
        self.assertEqual(sub(5, 5), 0)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(3, 3), 9)
        self.assertEqual(calculator.mul(-3, 3), -9)

            # 3 assertions

    def test_divide(self):# 3 assertions
        self.assertEqual(calculator.div(5, 20), 4)
        self.assertEqual(calculator.div(10, 40), 4)
        self.assertEqual(calculator.div(-10, 40), -4)


    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, -5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(5, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 8)
        with self.assertRaises(ValueError):
            log(1, 8)
        with self.assertRaises(ValueError):
            log(-2, 8)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.log(2, -5)


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(calculator.square_root(49), 7)
        self.assertAlmostEqual(calculator.square_root(64), 8)

        with self.assertRaises(ValueError):
            calculator.square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()