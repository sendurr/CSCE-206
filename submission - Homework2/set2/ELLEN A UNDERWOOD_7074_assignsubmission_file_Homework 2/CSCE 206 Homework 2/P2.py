import numpy as np
v=1
g=9.81
d=float((2*v)/g)
n=float(d/11)
def y(t):
	answer=v*t-0.5*g*t**2
	return answer
for x in np.arange(0,d,n):
	print "%10.3f %10.3f"%(x,y(x))
