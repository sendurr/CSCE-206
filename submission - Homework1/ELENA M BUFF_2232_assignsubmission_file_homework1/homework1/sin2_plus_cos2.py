#from math import sin,cos
#must import all math functions for pi to be defined
from math import *
x=pi/4.0
#print (x)
#1_val = sin^2(x)+cos^2(x)
#cannot start with number
#must insert * to show multiplication
val=sin(x)*sin(x)+cos(x)*cos(x)
#print 1_val
print (val)


if val==1.0:
	print ("Yes, sin^2(x) + cos^2(x) = 1")