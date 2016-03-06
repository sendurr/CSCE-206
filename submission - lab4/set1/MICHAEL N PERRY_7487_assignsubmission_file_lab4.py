print "Q1"
primes=[2,3,5,7,11,13]
for x in primes:
	print x
p=17
primes.append(p)
print primes
print " "

print "Q2"
s=0
k=float(1)
M=100
while k<=M:
	s+=1/k
	k+=1
print "using a while loop", s

def L(n,x):
	x=float(x)
	s=0
	for i in range(1,n+1):
		s+=(x/i)
	return s
x=1
print "using a for loop",L(100,x)
print " "

print "Q3"
M=[
[1,2,3],
[4,5,6],
[7,8,9]
]
print sum(M[0]+M[2])+M[1][0]+M[1][2]