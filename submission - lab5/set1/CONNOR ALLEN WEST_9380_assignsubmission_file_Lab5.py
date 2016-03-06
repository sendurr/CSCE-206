#Q1

def printstar(n):
	print('*'*n),
printstar(1)
printstar(10)
printstar(100)

#Q2
def printstarx(n,r=1):
	f = ('*'*n)
	i = 1
	while i <= r:
		print(f)
		i = i+1
printstarx(10)
printstarx(10,5)

#Q3
def checkprime(n):
	if n > 1:
		for i in range(2,n-1):
			if n%i==0:
				print("FALSE")
				break
		else:
			print("TRUE")

checkprime(3)
checkprime(255)