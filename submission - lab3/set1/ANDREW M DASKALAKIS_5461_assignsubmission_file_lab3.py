from math import *
from sets import Set
import random

#####################################################
#		Problem 1
#####################################################

print "problem 1:"

L1 = [2,3,4,10]
L2 = [5,3,4,9,10,15]

intersection = sorted(list(set(L1)&set(L2)))
print intersection		#returns the sorted list of the intersection between L1 and L2

XOR = sorted(list((set(L1)|set(L2))-set(intersection)))
print XOR				#returns the exculsive or of L1 and L2

XL1 = sorted(list(set(L1)-set(L2)))
print XL1				#returns L1 - L2

L2.append(103)
L2.append(20)
L2.append(34)
print L2

#####################################################
#		Problem 2
#####################################################
print ""
print "problem 2:"

sumx = 0

for x in range(13,999):
	sumx = sumx + x

print sumx

#####################################################
#		Problem 3
#####################################################
print ""
print "problem 3:"

x = [int(300*random.random()) for i in xrange(300)]

count = 0
#Dont know why we needed to use a while loop for this. Seems like a classic for loop problem
#the loop runs through the values of x
while count <= len(x)-1:
	#the if statement checks to see if the specific number in x has a factor of 3 or 7 and is not zero
	if x[count]!= 0 & x[count]%3==0 | x[count]%7==0:
		print x[count]
	count += 1
