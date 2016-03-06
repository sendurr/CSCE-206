#Rachel Smoak
#21 February 2016

#Lab 5

#Question 1
print "Question 1"
stars = []
def printstar(n):
	print '*'*n #Don't need a return because it prints it directly
printstar(1)
printstar(10)
printstar(100)
print "-----------------------------------------------------------------------------"

#Question 2
print "Question 2"
def printstarx(n,r=1):
	i = 0
	while i < r:
		printstar(n)
		i+=1
print "Using printstarx, print 1 row with 10 stars:"
printstarx(10)
print "Using printstarx, print 5 rows with 10 stars each"
printstarx(10,5)
print "-----------------------------------------------------------------------------"

#Question 3
print "Question 3"
def checkprime(n):
	i = 2
	while i<n:
		if n%i==0:
			print "False"
			break
		i+=1
	else:
		print "True"
		
print "checkprime(3):"
checkprime(3)
print "checkprime(255):"
checkprime(255)