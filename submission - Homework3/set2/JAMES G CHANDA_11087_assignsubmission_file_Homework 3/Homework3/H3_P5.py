''' Question 5: consider the simplest program for evaluating the formula
write two programs that let users to input v0 and t from commang line
using the following to methods'''
#method 1: 3 0.6, which will assing 3 to v0 and 0.6 to t

import sys

# t= float(sys.argv[2])
# v= float(sys.argv[1])

t= eval(sys.argv[2])
v= eval(sys.argv[1])
g=9.81
y = (v0*t)-(0.5*g*t**2)
print y