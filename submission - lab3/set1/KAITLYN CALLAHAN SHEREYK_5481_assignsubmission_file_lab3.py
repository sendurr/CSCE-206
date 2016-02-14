
L1=set([2,3,4,10])
L2=set([5,3,4,9,10,15])

print L1&L2 #exists in both
print L1^L2 #exists in either
print L1-L2 #exists in L1 not L2
L3=L1|L2 #merged lists
 
L2_lists=list(L2)
L2_lists.append(103) #how to add numbers to end of list
L2_lists.append(20)
L2_lists.append(34)
print L2_lists



C=range(13,1000,2) # for loop approach
total=0
for num in C:
	if num%2: #for odd numbers
		total+=num
print total
sum=total
print sum


import random
x=[int(300*random.random())for i in xrange(300)]
for i in x:
	if i%7==0 and i%3==0:
		print i



