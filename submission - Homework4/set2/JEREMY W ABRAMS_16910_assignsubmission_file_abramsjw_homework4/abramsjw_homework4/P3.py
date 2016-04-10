# Jeremy Abrams
# CSCE 206
# Homework 4 - P3.py
# March 26, 2016

import numpy as np
from math import *
import matplotlib.pyplot as plt
import sys


args = sys.argv

def f(t, j):
	f0 = []
	g = 9.81
	
	for i in t:
		y = j*i - ((1./2) * g * i**2)
		f0.append(y)

	return np.array(f0)



print (args)
print (len(args))
i = 1
v0 = []
while i < len(args):
	v0.append(float(args[i]))
	i = i + 1

print (v0)

for j in v0:
	g = 9.81
	t = np.linspace(0, 2*j/g, 100)
	plt.plot(t, f(t, j))

plt.show()		
