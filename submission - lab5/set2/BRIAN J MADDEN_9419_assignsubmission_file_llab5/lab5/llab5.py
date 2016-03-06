
from math import*
#1
def printstar(n):
	return "*"*n

print(printstar(1))
print(printstar(10))
print(printstar(100))

#2
def printstarx(n,r=1):
	"""Print 'number' of *'s in rows and columns"""
	for x in range(r):
		print ('*'*n)

print(printstarx(2,5))

#3
import math
def checkprime(x):
    if x%2==0 and x>2: 
        return False
    return all(x%i for i in range(3, int(math.sqrt(x))+1,2))

print(checkprime(3))
print(checkprime(255))