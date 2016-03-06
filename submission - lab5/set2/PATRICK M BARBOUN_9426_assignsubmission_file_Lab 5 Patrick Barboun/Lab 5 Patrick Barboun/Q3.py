def isprime(n):
	i = range(2,n-1)
	if n==2:
		return 'prime'
	else:
		answer = 0
		for x in i:
			if n%x==0:
				answer+=1
		if answer>=1:
			return 'not prime'
		else:
			return 'prime'

print isprime(13)



