import numpy as np
def f(t):
	answer= v*t - .5*g*(t**2)
	return answer
v=1
g=9.81
d= float((2*v)/g)
n=float(d/11)

for x in np.arange(0,d, n):
	print x, f(x)
	
