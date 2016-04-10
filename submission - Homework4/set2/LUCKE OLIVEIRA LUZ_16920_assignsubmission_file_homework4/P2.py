# Name: Lucke Oliveira Luz			Assignment: Homework 4        Exercise: 2

from numpy import *
from matplotlib.pyplot import *

def F(x):
	F = exp(x**2)*sin(x)
	return F

x = arange(-3.14,3.15,0.01)

plot(x,F(x))
show()