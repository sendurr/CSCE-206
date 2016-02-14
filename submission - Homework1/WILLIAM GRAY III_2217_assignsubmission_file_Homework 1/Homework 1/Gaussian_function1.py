from math import*

def f(x,s,m):
	answer=(1/sqrt(2*pi)*s)*exp((-1/2)*((x-m)/s)**2)
	return answer
	pass

print(f(1,2,0))