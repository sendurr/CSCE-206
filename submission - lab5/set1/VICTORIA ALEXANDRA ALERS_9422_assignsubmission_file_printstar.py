def printstar(n):
	print("*"*n)
print(printstar(1))
print(printstar(10))
print(printstar(100))
#-----------------------
#by setting k=1 it defults the perameter to one row unless k is defined
def printstarx(j,k=1):
	for i in range(k):
		printstar(j)
printstarx(10)
printstarx(10,5)
#-----------------------

def checkprime(l):
	c=2
	while c < l-1:
		if l%c== 0:
			return False
		l+=1
	return True
print(checkprime(3))
print(checkprime(255))


  