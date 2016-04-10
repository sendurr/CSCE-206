import numpy as np
import matplotlib.pyplot as plt
import sys

g = 9.81

def f(t, v0):
	return v0*t - 0.5*g*t**2

x = plt.subplot(111)
plt.hold(1)

def graph(v0):
	klist = np.linspace(0, 2*v0/g, 100)
 	x.plot(klist, f(klist, v0))


x.set_xlabel('time in seconds')
x.set_ylabel('height in meters')
 
vec = np.array(sys.argv[1:], dtype=np.float)

for i in range(len(vec)):
	graph(vec[i])

plt.legend(['v0 = %g' % v0 for v0 in vec])
plt.show()
