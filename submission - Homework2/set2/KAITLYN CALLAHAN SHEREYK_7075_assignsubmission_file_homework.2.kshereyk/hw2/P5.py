roots=[-1,1,2]

def poly(roots,x):
	p=1
	for i in range(len(roots)):
		p*=(x-roots[i])
	return p
print poly(roots,15)
