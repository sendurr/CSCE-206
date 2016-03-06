root=[-1,1,2]
print len(root)

def poly(root,x):
	a=1
	for i in range(len(root)):
	
		a*=(x-root[i])
	return a	
print poly(root,15)
