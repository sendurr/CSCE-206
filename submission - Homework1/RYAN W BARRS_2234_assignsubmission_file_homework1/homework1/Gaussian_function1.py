from math import exp, sqrt, pi

m = 0.0
s = 2.0
x = 1.0

A = (1/(sqrt(2*pi)*s))
B = exp((-1/2)*((x-m)/s)**2)

print A*B