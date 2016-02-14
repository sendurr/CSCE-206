#Exercise 1.10

from math import pi, exp, sqrt
m = 0
s = 2
x = 1
b = sqrt(2*pi)
e = ((x-m)/s)**2

#I defined b as the first part of the equation and e as the squared part

f = (1/(b*s))*(exp(-0.5*e))
print (f)