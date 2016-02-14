L1=set([2,3,4,10])
L2=set([5,3,4,9,10,15])
print "numbers in both",L1&L2
print "in L1 not L2", L1-L2
print "different", (L1|L2)-(L1&L2)


L3=L1 | L2
print "put together:",L3

L1=[2,3,4,10]
L2=[5,3,4,9,10,15]

L2.append(103)
L2.append(20)
L2.append(34)
print "appended L2:",L2

sum=0
i=0
a=range(13,1000)
while i<len(a):
	sum+=a[i]
	i+=1
print "sum from 13-999:", sum

import random

x=[int(300*random.random()) for i in xrange(300)]
for i in x:
		if x[i]%3==0 and x[i]%7==0:
			i+=1
print "divisible by 3 and 7:",x[i]

	
	
		

	

