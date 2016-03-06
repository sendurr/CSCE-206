def checkprime(n):
	status = True 
	for num in range(2, n-1):
		if n % num == 0:
			status = False
	return status 

print checkprime(3)
print checkprime(255)
