def checkprime(n):
		for i in range(2,n):
			if n%i == 0:
				return "false"
		else:
			return "true"
print checkprime(3)
print checkprime(255)
