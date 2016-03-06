def printstar(n):
	print '*'*n
print printstar(1)
print printstar(10)
print printstar(100)

#Q2
def printstarx(n, r=1):
	default=1
	for i in range(r):
		printstar(n) 
print "print 1 row with 10 stars"
printstarx(10)
print "print 5 rows and each with 10 stars"
printstarx(10,5)