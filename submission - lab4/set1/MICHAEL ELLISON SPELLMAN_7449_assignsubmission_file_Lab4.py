primes = [2,3,5,7,11,13]
for x in primes:
	print x
p=17
primes.append(p)
print primes

m=range(20)
m=range(1,20,1)
print m
sum=0
for x in m:
	sum+=1.0/x
print sum

M= [1,2,3],[4,5,6],[7,8,9]
print M

sum=0
for i in range(len(M)):
	for j in range(len(M[i])):
		print M[j][i],
		if i==j:
			sum+=M[i][j]
	print
print sum