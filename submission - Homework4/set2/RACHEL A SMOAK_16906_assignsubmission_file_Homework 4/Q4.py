#Rachel Smoak
#27 March 2016
#Homework 4

#Question 4

from numpy import *
def sincos(x):
	arrayx = array(x)
	result = sin(cos(arrayx))
	return result

x = [1,3,5,7,10.5]
y = sincos(x)
print y