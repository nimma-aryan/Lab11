import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
def test_multiply(self):
    self.assertEqual(calculator.mul(2, 3), 4)
    self.assertEqual(calculator.mul(3, 3), 6)

        # 3 assertions


def test_divide(self):# 3 assertions
    self.assertEqual(calculator.div(5, 20), 4)
    self.assertEqual(calculator.div(10, 40), 4)



    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
def test_log_invalid_argument(self): # 1 assertion
    with self.assertRaises(ValueError):
        calculator.log(2, -5)


def test_hypotenuse(self): # 3 assertions
    self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
    self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)

def test_sqrt(self): # 3 assertions
    self.assertAlmostEqual(calculator.sqrt(49), 7)
    self.assertAlmostEqual(calculator.sqrt(64), 8)

    with self.assertRaises(ValueError):
        calculator.square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()