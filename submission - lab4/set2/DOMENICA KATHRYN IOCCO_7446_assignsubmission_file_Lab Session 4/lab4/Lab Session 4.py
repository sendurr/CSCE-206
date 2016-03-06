#QUESTION 1-----------------------
primes=[2,3,5,7,11,13]
print(primes)
for a in primes:
	print(a)
p=17
primes.append(p);
print("updated list:", primes)

#QUESTION 2-----------------------
s=0
k=1
M=20
while k <= M:
	s += 1/k
	k += 1
print(s)

s=0
k=1
M=20
for k in range(1,M+1):
	s += 1/k
	k += 1
print(s)

#QUESTION 3-----------------------
M=([1,2,3],
	[4,5,6],
	[7,8,9])
print(M)
newlist=[]
for x in range(1,10,1):
	newlist.append(x)
	print(sum(newlist))
