print "Problem 1"
def printstar(n):
	printstar = "*"*n
	return printstar

print printstar(1)
print printstar(10)
print printstar(100)

print "Problem 2"
def printstarx(n, row=1):
	for i in range(row):
		print i+1, printstar(n)

printstarx(10)
print "5 rows:"
printstarx(10,5)

print "Problem 3"
def checkprime(n):
	if n == 2:
		return True
	if n%2==0 or n <= 1:
		return False
	for x in range(3,n,2):
		if n%x == 0:
			return False
	return True

print '3', checkprime(3)
print '255', checkprime(255)