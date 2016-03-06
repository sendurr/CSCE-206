def sum_for(m):
	y = []
	for i in range(1,m+1):
		z = 1./(float(i))**2
		y.append(z)
	return sum(y)

print sum_for(5)

def sum_while(M):
	a = []
	b = 1
	while b<M+1:
		c = 1./(float(b))**2
		b = b + 1
		a.append(c)	
	return sum(a)

print sum_while(5)