from numpy import *
def sincos(x):
	for i in x:
		return sin(cos(x))
x=array([1,3,5,7,10.5])
y=sincos(x)
print y
#in radians