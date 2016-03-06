from math import fib

def fib(1000):
    a, b = 0, 1
    for i in range(1000):
        a, b = b, a + b
    return a

