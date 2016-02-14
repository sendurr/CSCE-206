# Ex 1.10: Gaussian function

from math import *

def f(m,x,s):
	final = (1.0/(sqrt(2.0*pi)*s))*exp((-1/2.0)*(((x-m)/s)**2.0))
	return final
print f(0,1.0,2.0)
