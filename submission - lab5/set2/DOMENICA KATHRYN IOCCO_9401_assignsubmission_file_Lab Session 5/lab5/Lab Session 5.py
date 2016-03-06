#1 Printstar-------------------
def printstar(n):
	print ('*'*n)
printstar(1), printstar(10), printstar(100)
print(printstar(1), printstar(10), printstar(100))

#2 Printstar with Parameters---
def printstarx(c,d=1):
	for j in range(d):
		printstar(c)
printstarx(10)
printstarx(10,5)

#3 Check prime------------------
def checkprime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for x in range(2, int(n-1), 1):
		if n % x == 0:
			return False
	return True
#function test:
print(checkprime(3))
print(checkprime(255))
