import numpy as np
v0=1
g=9.81
n=11
a=2*v0/g

def y(t):
	return v0*t-0.5*g*t**2
for t in np.arange(0,a,(a/11)):
	print "t=", t, "\t", "y=", y(t)