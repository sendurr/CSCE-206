from numpy import *

def sincos(x):
	return sin(x)*cos(x)

x=array([1,3,5,7,10.5])
y=sincos(x)
print (y)