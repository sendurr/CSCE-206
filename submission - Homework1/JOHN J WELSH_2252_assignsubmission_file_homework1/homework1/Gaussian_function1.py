#Homework 1,Exercise 3 by John Welsh

from math import exp, pi, sqrt 					#Import necessary functions

m = 0.; s = 2.; x = 1. 							#Declare variables

f = 1/(sqrt(2*pi)*s)*exp(-0.5*((x-m)/s)**2) 	#Solve Gaussian function
print f 										#Print solution