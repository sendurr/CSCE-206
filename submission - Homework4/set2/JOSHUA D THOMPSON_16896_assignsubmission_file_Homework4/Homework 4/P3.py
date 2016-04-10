import sys
import matplotlib.pyplot as plt 
import numpy as np 

grav=9.81

def f(t, v0):
	return v0*t-0.5*grav*t**2

x=plt.subplot(111)
plt.hold(1)

def c(v0):
	tlist=np.linspace(0,2*v0/grav,100)
	x.plot(tlist, f(tlist,v0))

x.set_ylabel('Height (meters)')
x.set_xlabel('Time (seconds)')

vectors=np.array(sys.argv[1:], dtype=np.float)

for i in range(len(vectors)):
	c(vectors[i])

plt.legend(['v0=%g'% v0 for v0 in vectors])
plt.show()