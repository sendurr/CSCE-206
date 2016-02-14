print "Exercise 1.10"
from math import*
def f(x,m,s):
	answer=(1.0/(sqrt(2*pi)*s))*(exp((-0.5)*(((x-m)/(s))**2)))
	return answer
print f(1.0,0,2.0)