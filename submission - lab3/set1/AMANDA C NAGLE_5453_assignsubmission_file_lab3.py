# Lab Question 1
L1= [2,3,4,10]
L2= [5,3,4,9,10,15]
sl1= set(L1)
sl2= set(L2)

#print numbers in both
a= sl1 & sl2
print a

# print nubers in one or other but not both
b= sl1 | sl2
c= b-a
print c

#print L1 but not L2
d= sl1-sl2
print d

#merge
L3= L1+L2

#add
L2.append(103)
L2.append(20)
L2.append(34)

#Lab question 2
x=13
total=0
while x <= 999:
	total+=x
	x +=2
print total

#lab question 3
import random
x=[int(300*random.random()) for i in xrange(300)]
x.sort()
i=0
e=[]
for number in range(len(x)):
	if (x[i]%3 == 0) and (x[i]%7 == 0):
		e.append(x[i])
	i+=1
print e








