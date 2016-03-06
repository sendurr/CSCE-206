#1
print "1."
def printstar(n):
	return n*"* "
print printstar(1)
print printstar(10)
print printstar(100)
print 

#2
print "2."

def printstarx(n,row=1):
	#for i in range(row):
	#	if i % 2 == 0:
	for x in range(row):
		print n*"* "
	#	else:
	#		return (n-1)*"* "
printstarx(10)
print 
printstarx(10,5)
print 

#3
print "3."
def checkprime(n):
	if n < 2:
		return "false - it is not a prime"
	elif n == 2:
		return "true - it is a prime"
	#elif n % 2:
	#	return "false - it is not a prime"
	else:
		for x in range (2,n-1,1):
			if n%x==0:
				return "false - it is not a prime"
		return "true - it is a prime"
print "3:", checkprime (3)
print "255:", checkprime (255)
print 