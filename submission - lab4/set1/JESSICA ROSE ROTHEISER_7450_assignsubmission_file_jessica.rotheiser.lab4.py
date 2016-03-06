#1
primes=[2,3,5,7,11,13]
for x in primes:
	print x

p=17
primes.append(p)
print primes

#2
s1=0
k=1
M=10
for k in range(1,M+1):
	s1+=1./k
print "s1=", s1

s2=0
k=1
M=10
while k<= M:
	s2+=1./k
	k+=1
print "s2=", s2
	

#3
M= ([1,2,3],[4,5,6],[7,8,9])
total=0
for x in M:
	total+= sum(x)
print "sum of matrix:", total
	