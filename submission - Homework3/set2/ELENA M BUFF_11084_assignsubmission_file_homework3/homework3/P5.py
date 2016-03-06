# v0=3; g=9.81; t=0.6
# y=v0*t-0.5*g*t**2
# print "y=",y

import sys

print 

v0=float(sys.argv[1])
t=float(sys.argv[2])

g=9.81
y=v0*t-0.5*g*t**2

print ("y=%.4f"%y)

print
