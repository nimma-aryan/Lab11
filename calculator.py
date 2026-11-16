# GitHub Respository URL: https://github.com/nimma-aryan/Lab11.git
# Partern 1:
# Partern 2: Rhiannon Harpe


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


