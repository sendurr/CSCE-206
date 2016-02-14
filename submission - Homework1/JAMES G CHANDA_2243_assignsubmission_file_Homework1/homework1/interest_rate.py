# Exercise 1.6: Compute the growth of money in a bank

def f(A,p,n):
	answer = A*((1.0+(p/100.0))**n)
	return answer
print "Money:", f(1000.0,5.0,3.0), "euros"


	