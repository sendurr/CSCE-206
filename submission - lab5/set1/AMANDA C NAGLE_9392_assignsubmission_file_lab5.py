#lab 5 Q1

def printstar(n):
	print '*'*n
printstar(1)
printstar(10)
printstar(100)

#lab 5 Q2
def printstarx(n,m=None):
	x=0
	if m is None:
		m=1
	for x in range(0,m):
		printstar(n)
printstarx(10)
print "      "
printstarx(10,5)



