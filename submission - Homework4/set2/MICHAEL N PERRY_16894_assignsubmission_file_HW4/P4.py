import numpy as np

def sincos(x):
	result=np.sin(np.cos(x))
	return result

x=np.array([1,3,5,7,10.5])
y=sincos(x)
print y