#Q1
def printstar(n):
	x=n*"*"
	print ("Output: ", x)
	return x

printstar(1)
printstar(10)
printstar(100)

#Q2
def printstarx(n,row=1):
	default=1
	for i in range(row):
		printstar(n)

printstarx(10)
printstarx(10,5)