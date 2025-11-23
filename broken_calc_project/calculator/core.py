# core math functions — broken signatures and returns
from .ops import divide, add_extra
import math

def addition(a, b, c):  # requires 3 args but main calls with 1
    return a + b + c

def subtract(a, b):
    print("Performing subtract")
    # no return intentionally

def multiply(a, b):
    # wrong behavior: returns string sometimes
    if a == 0:
        return "zero!"
    return a * b

def divide_safe(a, b):
    if b = 0:  # syntax error (assignment in if)
        return None
    return divide(a, b)

def power(a, b):
    # uses xor accidentally
    return a ^ b
