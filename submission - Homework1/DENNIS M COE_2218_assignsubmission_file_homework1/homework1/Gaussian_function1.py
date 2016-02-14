from math import *

m = 0
s = 2
x = 1

f = (1.0 / (sqrt(2 * pi) * s)) * exp(-1.0/2.0 * ((x-m)/float(s))**2)

print (f)