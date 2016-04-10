import matplotlib.pyplot as plt
from math import *
from numpy import *
import sys

g = 9.81

v0=[float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])]


for x in range(0,3):
	t = linspace(0,2*v0[x]/g,100)
	y = v0[x]*t-0.5*g*t**2
	plt.plot(t,y)

plt.show()
