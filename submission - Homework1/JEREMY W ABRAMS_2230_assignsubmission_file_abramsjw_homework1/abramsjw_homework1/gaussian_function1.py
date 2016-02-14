# Jeremy Abrams
# CSCE 206
# Gaussian - Homework 1
# January 22, 2016

# Import math library
from math import *

# Define gaussian function, compute, and print
def gaussian(m, s, x):
	answer = (1/(sqrt(2*pi)*s))*exp((-0.5)*(((x-m)/2)**2))
	print answer

# Call the gaussian function
gaussian(0, 2, 1)