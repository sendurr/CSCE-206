
from math import sqrt, pi, exp
def f(m,s,x):
	answer=((1.0)/(sqrt(2.0*pi)*s))*(exp((-1.0/2.0)*((x-m)/(s))**2))
	return answer
print(f(0,2,1))

