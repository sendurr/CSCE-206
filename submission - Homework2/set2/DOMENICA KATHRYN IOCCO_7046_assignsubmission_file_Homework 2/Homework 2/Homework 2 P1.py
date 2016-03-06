#Question 1--------------------
from math import *
def recur_fibonacci(n):	
	if n <= 1: 
		return n
	if n > 1: 
		return recur_fibonacci(n-1)+(recur_fibonacci(n-2))
print("Fibonacci sequence:")
for i in range(0,1000,1):
	print(recur_fibonacci(i))
