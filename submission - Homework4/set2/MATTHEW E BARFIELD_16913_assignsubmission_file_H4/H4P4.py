from numpy import *

def sincos(x):
	result = []
	
	for i in x:
		result.append(sin(cos(i)))
	return result

x = array([1,3,5,7,10.5])
y = sincos(x)

print y