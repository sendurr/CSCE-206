def printstar(n):
	for i in range(n):
		print ("*",)
print 
printstar(100)
printstar(10)
printstar(1)

def printstarx(n,row):
	for i in range(row):
		printstar(n)
		printstar(10,1)
		printstar(10,5)

def checkprime(n):
	'''check if integer n is a prime numeber'''
	n=abs(int(n))
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for x in range (3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
		return True