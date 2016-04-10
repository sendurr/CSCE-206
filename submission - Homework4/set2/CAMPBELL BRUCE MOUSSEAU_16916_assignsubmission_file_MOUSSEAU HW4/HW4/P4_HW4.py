import numpy as np 
from math import sin, cos

def sincos(x):
	final=np.sin(np.cos(x))
	return final

x=np.array([1,3,5,7,10.5])
print (sincos(x))
