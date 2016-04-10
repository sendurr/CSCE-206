# Name: Lucke Oliveira Luz			Assignment: Homework 4        Exercise: 4

from numpy import *

def sincos(x):
	result = sin(cos(x))
	return result

x = array([1,3,5,7,10.5])
y = sincos(x)
print y