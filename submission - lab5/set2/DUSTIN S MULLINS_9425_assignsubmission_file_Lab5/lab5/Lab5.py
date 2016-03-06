#1.
def printstar(n):
	print '*'*n

printstar(1)
printstar(10)
printstar(100)

#OR
#def printstar(n):
	#return '*'*n

print printstar(1)
print printstar(10)
print printstar(100)


#2.
def printstarx(n,r=1):
	"""Print '*' in rows and columns"""
	for x in range(r):
		print '*'*n

printstarx(10)
printstarx(10,5)


#3.

import math
def checkprime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

#Test function:
print checkprime(3)
print checkprime(255)