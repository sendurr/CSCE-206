#Ex 1.9: Type in programs and debug
#Does sin^2(x) + cos^2(x)=1?


#Bugged version
#from math import sin, cos
#x = pi/4
#1_val = sin^2(x) + cos^2(x)
#print 1_val


#Corrected version
from math import *
x = (pi/4.0)
val =(sin(x))**2.0 + (cos(x))**2.0
print "val: ", val