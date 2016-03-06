# number 1
primes=[2,3,5,7,11,13]
for x in primes:
	print (x)

p=[17]
newlist=primes+p

print (newlist)

# number 2

sum_s=0

range(1,20,1)
for k in range(1,21,1):
	s=1.0/k
	sum_s+=s
print (sum_s)

k=1.0
cmax=21
sum_x=0
while cmax > k:
	x=1.0/k
	k+=1
	sum_x+=x
	
print(sum_x)

# number 3

M=[[1,2,3],[4,5,6],[7,8,9]]
del(M[1][1])
print (sum(M[0]+M[1]+M[2]))
