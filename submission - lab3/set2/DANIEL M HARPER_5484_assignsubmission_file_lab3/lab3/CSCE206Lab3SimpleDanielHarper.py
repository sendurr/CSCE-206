# Author: Daniel Harper
# Assignment: Lab 3
# Original Date: 2/4/2016
# Last Updated:  2/4/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
import random

# Body Section#######################################################
#--------------------------------------------------------------------
# 1. play with list and set
L1=[2, 3, 4,10]
L2=[5,3,4,9,10,15]

L1 = set(L1)
L2 = set(L2)
# Print out the numbers that exist in both variables L1 and L2 using 
# set operations
print("Intersection:",set.intersection(L1,L2))

# Print out numbers that exists in either L1 or L2, but not both using 
# set operation
answer3 = set.difference(L1,L2) 
answer2 = set.difference(L2,L1)
print("Mutual Exclusive:",set.union(answer2,answer3))

# Print out numbers that exist in L1 but not in L2. 
print("L1 Exclusive:",answer3)

# merge L1 and L2 and save it into variable L3
L3 = L1 | L2
print("L3 (L1 + L2):",L3)

# Add the following numbers to L2,   103, 20, 34 using  append() 
# function of list. 
L2 = list(L2)

L2.append(103)
L2.append(20)
L2.append(34)

print("L2 appended:",L2)

#--------------------------------------------------------------------
# 2. while loop application
# starting with 13, add all the odd numbers from 13 up to 999
# save it to variable sum
total = 0
i = 13
while(i < 1000):
	if i % 2 == 1:
		total += i
	i += 1
print("Total (13-999 odd):",total)

#--------------------------------------------------------------------
# 3. The following code generates 300 random integers
# use while loop to print out all the numbers that have factors of 3 
# and 7 hint: use % operator
x=[int(300*random.random()) for i in range(300)]
i = 0
factors = []
while i < len(x):
	if x[i] % 7 == 0:
		if x[i] % 3 == 0:
			factors.append(x[i])
	i += 1
print("Factors 3 and 7:", factors)

