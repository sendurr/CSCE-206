def growth(A,p,n):
	answer=A*(1+p/100.0)**n
	return answer
	pass
print "money growth=",growth(1000,0.05,3)
