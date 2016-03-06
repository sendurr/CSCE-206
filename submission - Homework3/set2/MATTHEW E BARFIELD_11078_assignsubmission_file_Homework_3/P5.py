print "Homework 3 - Question 5"
print ""

import sys
g=9.81
t=float(sys.argv[2])
v=float(sys.argv[1])
y=v*t-0.5*g*t**2
print "Distance(y) = ", y