import numpy as np
x=[]
def xi(i,h=0.01):
	answer=1+i*h
	return answer

for a in range(0,101):
	x.append(xi(a))
print x




