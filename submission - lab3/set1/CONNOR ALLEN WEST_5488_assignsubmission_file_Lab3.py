from math import *
# Question 1

L1=[2,3,4,10]
L2=[5,3,4,9,10,15]
Set1=set([2,3,4,10])
Set2=set([5,3,4,9,10,15])

IN = Set1.intersection(Set2)
print(IN)

sym = Set1.symmetric_difference(Set2)
print(sym)

diff = Set1.difference(Set2)
print(diff)

L3 = L1 + L2
print(L3)

L2.append(103)
L2.append(20)
L2.append(34)
print(L2)

#Question 2
A = 13
dA = 2
total = 0
while A <= 999:
	total += A
	A = A + dA
print(total)

#Question 3
import random
x=[int(300*random.random()) for i in range(300)]


for a in x:
	if a%3==0 and a%7==0:
		print(a)