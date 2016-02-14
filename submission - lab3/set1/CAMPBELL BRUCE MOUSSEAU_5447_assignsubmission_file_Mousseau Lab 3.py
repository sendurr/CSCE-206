#problem 1
L1=[2,3,4,10]
L2=[5,3,4,9,10,15]
a=set(L1).intersection(L2)
print(a)
d=set(L1).symmetric_difference(L2)
print(d)
z=set(L1).difference(L2)
print(z)
L3=set(L1).union(L2)
print(L3)
(L2).append(103)
(L2).append(20)
(L2).append(34)
print(L2)

#Problem 2
range(13,999)
n=987
sum=0
for i in range(13,999):
	sum=sum+i
print(sum)

#problem 3
import random
x=[int(300*random.random()) for i in xrange(300)]
xrange=300
while index<300:
	if x[index]%3==0 and x[index]%7==0:
		print (x[index]),
	index+=1

