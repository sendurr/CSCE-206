import numpy as np
primes=[2,3,5,7,11,13]
p=17
n=[]

for x in primes:
	print x
primes.append(p)
n.append(primes)
print n

s=[]
k=1.0
M=10.0	
total=0
def sumoffunc(k):
	answer=(1/k)
	return answer
for x in np.arange(k,M+1):
	s.append(sumoffunc(x))
	total=sum(s)
print "%0.3f"%total

total=0
a=[]
k=1.0
M=10.0
while k<M+1:
	a.append(sumoffunc(k))
	total=sum(a)
	k+=1
print "%0.3f"%total	


n=[]
total=0
M=np.array([[1,2,3],[4,5,6],[7,8,9]])
M.sum(axis=1)
n.append(M[0, :].sum())
n.append(M[2,:].sum())
n.append(M[1][2])
n.append(M[1][0])
total=sum(n)
print total






