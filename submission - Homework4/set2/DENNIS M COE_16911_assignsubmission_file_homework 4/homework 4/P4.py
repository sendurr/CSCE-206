from numpy import *

def sincos(x):
	for i in x:
		o = cos(x)
		k = sin(o)
		print k

x = array([1, 3, 5, 7, 10.5])
y = sincos(x)

print y