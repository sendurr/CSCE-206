from numpy import *
#question 1
L1=set([2,3,4,10])
L2=set([5,3,4,9,10,15])

print "in both L1 and L2:", L1 & L2
print "in either L1 or L2 but not both:", L1^L2
print "in L1 but not L2:", L1 - L2
L3=L1|L2
print "L3=", L3

L2_list=list(L2)
L2_list.append(20)
L2_list.append(34)
L2_list.append(103)
print L2_list

#question 2
sum_=sum(range(13,1000,2))
print sum_

#question 3
import random
x=[int(300*random.random()) for i in xrange(300)]
for i in x:
	if i%7==0 and i%3==0:
		print i