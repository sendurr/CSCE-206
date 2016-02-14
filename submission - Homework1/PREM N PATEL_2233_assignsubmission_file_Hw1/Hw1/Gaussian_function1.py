from math import*

def f(m,s,x):
	ans = (1.0/(sqrt(pi*2.0)*2.0))
	ans2 = exp(-0.5*((x)/2.0)**2.0)
	return ans*ans2

print f(0,2,1)