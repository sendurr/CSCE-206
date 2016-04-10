# Jeremy Abrams
# CSCE 206
# Homework 4 - Q4.py
# March 24, 2016

from numpy import *
from math import *

def sincos(x):
	result = []
	for i in x:
		y = sin(cos(i))
		result.append(y)
	return result

x = array([1,3,5,7,10.5])
y = sincos(x)
print y