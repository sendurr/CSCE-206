
from math import *
A=1000 #euros
p=5
def F(n):
	answer=1000*((1+5.0/100)**n)
	return answer
print F(3)