from math import *
def f(m,s,x):
	answer=(1.0/(s*sqrt(2*pi)))*(exp((-0.5)*((x-m)/s)**2))
	return answer
print f(0,2.0,1.0)
