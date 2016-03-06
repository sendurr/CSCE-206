import numpy as np
v0=1
g=9.81
n=11
x=np.arange(0,2*v0/(g),2*v0/(g*n))

for t in x:
	y=t*v0-0.5*g*t**2
	print (t,y)
