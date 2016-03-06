def printstar(n):
	print'*'*n, ',' 
printstar(1)
printstar(10)
printstar(100)

def printstarx(n,row=1):
	i=0
	while i<row:
		printstar(n), ','
		i+=1
print "default 1 row"		
printstarx(10)	
print "10 * 5 rows"
printstarx(10,5)	



def checkprime(n):
		x=[n%i for i in range(2,n-1)]
		for i in x:
			if x[i]==0:
				return False
			else:
				return True

print checkprime(255)
print checkprime(3)			