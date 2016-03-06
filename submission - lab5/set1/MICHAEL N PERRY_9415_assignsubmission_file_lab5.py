print "Q1"
def printstar(n):
	answer="*"*n
	print answer
	return
printstar(1)
printstar(10)
printstar(100)
print " "

print "Q2"
def printstarx(n,r=1):
	for x in range(r):
		printstar(n)
	return
printstarx(10)
printstarx(10,5)
print " "

print "Q3"
def checkprime(n):
	for x in range(2,n):
		if n%x==0:
			return False
	return True
print checkprime(3)
print checkprime(255)