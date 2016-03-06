def printstar(n):
	return '*'*n


print printstar(1)
print printstar(10)
print printstar(100)

def printstarx(n, row = 1):

	for i in range(0, row):
		ls = []
		for j in range(0, n):
			ls.append('*')
		strng = ' '.join(ls)
		print(strng)
print printstarx(10)
print printstarx(10,5)

def checkprime(n):
	
	Prime = True
	for div in range (2,n-1):
		if n%div == 0:
			Prime = False

	if Prime:
		print(True)
	else:
		print(False)

print checkprime(3)
print checkprime (225)
