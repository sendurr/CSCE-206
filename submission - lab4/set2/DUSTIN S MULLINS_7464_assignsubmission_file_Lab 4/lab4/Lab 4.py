#1
primes = [2,3,5,7,11,13]

for n in primes:
	print n

n1 = 17
primes.append(n1)

print primes

#2
s = 0; k = 1; M = 50

for i in range(k, M + 1):
    s += 1.0/i
print s

s = 0; k = 1.; M = 50
while k <= M:
    s += 1/k
    k += 1
print s


#3
M  = [[1,2,3],[4,5,6],[7,8,9]]

print M

sum = 0
for i in range(len(M)):
	for j in range(len(M[i])):
		print M[i][j],
		if i==0 or i ==2 or j==0 or j==2:
			sum += M[i][j]
		print
print "sum =",sum



