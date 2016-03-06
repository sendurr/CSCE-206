#X'Avier Douglas Lab 4
import math 

#1
print("#1")
primes = [2,3,5,7,11,13]
p = 17
for x in primes:
	print (x)
primes.append(p)

print ("###############################")

#2
print("#2")
print("for loop")
xsum = 0
M = 101
for k in range(1,M):
	if 1.0/k > 0:
		xsum += 1.0/k
print(xsum)


print("while loop")
ysum = 0
i = 0
N = range(1,101)
while i < len(N):
	k=N[i]
	f = 1.0/k
	i+=1
	ysum = ysum + f
print(ysum)

#3
print("#3")

M = [[1,2,3],[4,5,6],[7,8,9]]
print (M)
boundaries = (M[0][0],M[0][1],M[0][-1],M[1][0],M[1][-1],M[-1][0],M[-1][1],M[-1][-1])
print ("boundaries =", boundaries)
print ("boundary total =", sum(boundaries))




