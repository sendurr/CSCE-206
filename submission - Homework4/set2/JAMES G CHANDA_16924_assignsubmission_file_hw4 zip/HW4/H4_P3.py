'''Question 3: plot a formula for several parameters. make a program that
reads a set of V0 values from the command line and plots the curves y(t)=V0t-0.5gt^2'''

from sys import argv
import matplotlib.pyplot as plt
import numpy as np 
from math import *

g = 9.81 
V = 0.0

for n in range(0,20/9.81):
	y0 = []
	v = (argv[n])
	t = np.linspace(0, 2*V/g, 100)
	for i in t:
		y0.append(v*i-0.5*g*i**2)
	label = "V0 = " + str(V)
	plt.plot(t, y0, label = label)

plt.legend()
plt.xlabel('t'); plt.ylabel('y(t)')
plt.show()