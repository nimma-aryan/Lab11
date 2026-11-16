"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# Import
import math

# Functions
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('Cannot division by zero')
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithmic arguments")
    return math.log(b, a)

def exp(a, b):
    return a ** b


if __name__ == "__main__":
    print(square_root(49))
    print(hypotenuse(5, 12))
    print(add(2, 3))
    print(sub(5, 3))
    print(mul(2, 3))
    print(div(2, 10))
    print(log(2, 8))
    print(exp(2, 3))
