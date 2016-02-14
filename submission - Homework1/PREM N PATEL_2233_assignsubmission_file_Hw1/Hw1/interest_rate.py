def f(A,p,n):
	answer = A*(1.0+(p/100.0))**n
	return answer

print '%.2f'%f(1000,5,3)