def printstar(n):
	print '*'*n
def printstarx(n, row=1):
	default=1
	for i in range(row):
		printstar(n) # call printstar function row number of times
  
printstarx(10)# print star of lenth n and in 4 row
printstarx(10,5)# print stars of length 18 and in one row (default value of row = 1)