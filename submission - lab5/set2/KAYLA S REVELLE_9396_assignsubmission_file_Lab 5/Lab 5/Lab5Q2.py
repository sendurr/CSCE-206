
def printstarx(n,row=1):
	
	for i in range(0,row):
		k=[]
		for x in range(0,n):
			k.append('*')
		j=' '.join(k)
		print(j)


print (printstarx(10))
print (printstarx(10,5))
