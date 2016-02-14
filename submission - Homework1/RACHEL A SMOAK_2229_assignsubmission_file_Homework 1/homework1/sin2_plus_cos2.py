#Rachel Smoak
#HW1 Exercise 1.9

#Debug this:
#from math import sin, cos
#x=pi/4
#1_val = sin^2(x)+cos^2(x)
#print 1_VAL

#could also import all, but need to remember to import pi
from math import sin, cos, pi
x=pi/4
#cannot start a variable with a number, you need ** instead of ^
#remember to use (sin(x)) squared instead of sin squared (x)
val_1 = (sin(x))**2+(cos(x))**2
print val_1

