from math import *

m = 0
s = 2
x = 1

guass = (1/(sqrt(2*pi)*s)) * exp(-0.5*((x-m)/float(s))**2)

print "Gauss = %.5f" %(guass)
