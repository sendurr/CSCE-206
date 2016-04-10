# Jeremy Abrams
# CSCE 206
# Homework 4 - Q2.py
# March 24, 2016

import numpy as np
from math import *
import matplotlib.pyplot as plt

def f(x):
	f0 = []
	for i in x:
		y = exp(i**2)*sin(i)
		f0.append(y)

	return np.array(f0)

x = np.linspace(-3.14, 3.14, 100)
plt.plot(x, f(x))
plt.show()