r1 = -1
r2 = 1
r3 = 2
rootList=[r1,r2,r3]

def p(x):
	p=1
	for i in rootList:
		p *= (x-i)
	return p

print p(15)
