print "Q1:"
def printstar(n):
	return "*"*n
print printstar(1)
print printstar(10)
print printstar(100)


print "Q2"
def printstarx(n,row=1):
	for i in range(row):
		print printstar(n)
print printstarx(10)
print printstarx(10,5)
# not sure why "None" is printed in results
	
print "Q3 (Optional)"
import math
def checkprime(n):
    if n==2:
        return True
    if n%2==0 or n<=1:
        return False
    sqr=int(math.sqrt(n))+1
    for divisor in range(3,sqr,2):
        if n%divisor==0:
            return False
    return True
print checkprime(3)
print checkprime(255)
