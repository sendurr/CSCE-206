import math

#Q1
def printstar(n):
	print '*'*n

printstar(1)
printstar(10)
printstar(100)


#Q2 define a function call printstarx, which has two parameters.
#n parameter specifies how many stars to print on each row
#row parameter specify how many rows to print stars
#the row parameter should have a default value as 1.
#so this function will print a couple of rows, each row composed of n stars.  
#You can call printstar(n) function in Q1 to work out this problem. 
def printstarx(n,row=1):
	default=1
	for i in range(row):
		printstar(n)

printstarx(10)
printstarx(10,5)


#Q3
def checkprime(n):
	for x in range(2,n-1):
		if n%x==0:
			return "false"
	else:
		return "true"

print checkprime(3)
print checkprime(255)
