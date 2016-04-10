from numpy import *

def sincos(x):
	
	answer = []
	
	for i in x:
		answer.append(sin(cos(i)))
	
	return answer

x = array([1,3,5,7,10.5])

y = sincos(x)

print y