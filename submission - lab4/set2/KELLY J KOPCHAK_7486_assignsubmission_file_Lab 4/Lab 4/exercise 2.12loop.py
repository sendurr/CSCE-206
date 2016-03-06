k=1
M=10
s=0
	
for k in range(M+1):
	if k==0:
		print 'divison by zero, s=0'
	else:
		s+=1.0/k
		k+=1
	print s
