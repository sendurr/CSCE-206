# Ex 1.6: Compute the growth of money in a bank

def f(A,p,n):
	final = A*((1.0+(p/100.0))**n)
	return final
print "Money:", f(1000.0,5.0,3.0), "euros"


	