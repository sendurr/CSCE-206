print("1. play with list and set")
L1=[2,3,4,10]
L2=[5,3,4,9,15]
print (list(set(L1).intersection(L2)))
print (list(set(L1).union(L2)))
print (list(set(L1)-set(L2)))
L3=L1+L2
print (L3)
L2.append(103)
L2.append(20)
L2.append(34)
print (L2)
print ("2. while loop application")
def func(n):
	num=range(13,999)
	variablesum=[x for x in num if x%2]
	return (variablesum)
variablesum=func(999)
print (variablesum)


print ("3. random integers")
import random
def xrange():
	x=[int(300*random.random(300)) for i in xrange(300)]
	if i%7==0 and i%3==0:
		print(i)