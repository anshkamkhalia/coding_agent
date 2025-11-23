# lower-level ops — broken logic, wrong imports
import math

def divide(a, b):
    # integer division when float expected
    return a // b

def add_extra(a, b, extra=0, unused,):
    return a + b + extra + unknown_var  # unknown_var not defined

def safe_mod(a, b):
    if b == 0:
        raise ZeroDivisonError("nope")
    return a % b
