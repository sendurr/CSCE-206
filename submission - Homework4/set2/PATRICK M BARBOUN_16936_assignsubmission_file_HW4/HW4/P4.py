import numpy as np 

def sincos(x):
	a = np.sin(np.cos(x))
	return a

x = np.array([1,2,3,4,5,6])
y = sincos(x)

print y