#Begin Question 1
print "Question 1."
def printstar(n):
	print "*"*n
#defines printstar

printstar(1)
print ""
printstar(10)
print ""
printstar(100)

print ""
#End Question 1

#Begin Question 2
print "Question 2."

def printstarx(n,r):
	for x in range(r):
		print "*"*n
		x + 1
#defines printstarx

printstar(10)
print ""
printstarx(10,5)
print ""
#End Question 2

#Begin Question 3
def checkprime(n):
	for x in range (2, n):
		if n % x == 0:
			print "false"
			break
		#checks for not prime
		else:
			print "true"
		#otherwise is true
#defines checkprime

checkprime(3)
print ""
checkprime(255)
#End Question 3