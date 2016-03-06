#1
def printstar(n):
	answer = n*"*"
	return answer
print printstar(1), printstar(10), printstar(100)


2
def printstarx(n,rows=1):
    for i in range(rows):
    	print ''*rows + '*'*n
print printstarx(10)
print printstarx(10,5)