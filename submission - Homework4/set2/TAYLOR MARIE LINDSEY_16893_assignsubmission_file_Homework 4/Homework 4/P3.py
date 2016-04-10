
from math import *
from matplotlib import *

def f(t):
	return v0*t-0.5*g*t**2
	t = linspace(1,2.5,5)
	y = zeros(len(t))
for i in xrange(len(t)):
	y[i] = f(t[i])
	plot(t, y)
	show()