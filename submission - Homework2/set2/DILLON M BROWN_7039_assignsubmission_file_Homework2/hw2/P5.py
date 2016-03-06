##P5: Print out a polynomial function of given roots r1,r2,r3
from sympy import *
x = Symbol('x')
r1 = 1
r2 = -1
r3 = 15
roots = [r1,r2,r3]
equ = 1
for a in roots:
    equ = equ*(x-a)
print expand(equ)

