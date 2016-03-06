r0 = -1
r1 = 1
r2 = 2
from sympy import Symbol, expand
x = Symbol('x')
p = expand((x-r0)*(x-r1)*(x-r2))
print p