from math import*
m = 0
s = 2
def f(x,s,m):
	answer= ((1/(sqrt(2*pi)*s))*exp((-1/2)*((x-m)/s)**2))
	return answer
print (f(1,2,0))
