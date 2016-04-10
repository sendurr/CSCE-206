from math import *
from numpy import *

def sincos(x):
	y = cos(x)
	result = sin(y)
	return result

x = array([1,3,5,7,10.5])

y = sincos(x)

print y