def checkprime(n):
	Number= True
	for x in range(2,n-1):
		if n%x==0:
			Number=False
	if Number:
		print(True)
	else:
		print(False)


print (checkprime(3)) 
print (checkprime(255)) 