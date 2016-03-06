r=[-1,1,2]

def poly(r,x):
	p=1
	for n in range(len(r)):
		p+=(x-r[n])
	return p
print poly(r,15)
