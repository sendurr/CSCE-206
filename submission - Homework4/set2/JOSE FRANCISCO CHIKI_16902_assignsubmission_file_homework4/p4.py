from numpy import *
x=array([1,3,5,7,10.5])
def sincos(x):
	for i in x.tolist():
		z=sin(cos(x))
		return z
y=sincos(x)
print y