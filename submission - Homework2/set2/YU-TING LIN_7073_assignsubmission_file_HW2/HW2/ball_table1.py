from math import *
def distance1(v0,g,t):
	return v0*t-0.5*g*t**2

v0=1	
g=9.81
t=(0, 2*v0/float(g))
def distance1(t):
	i=11  
	return v0*t-0.5*g*t**2

for t in range(1,12):
	print t,"\t",distance1(t)
