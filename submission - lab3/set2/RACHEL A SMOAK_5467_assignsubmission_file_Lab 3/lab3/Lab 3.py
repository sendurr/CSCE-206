#Rachel Smoak
#Lab 3
#7 February 2016

#Question 1
print "Question 1"
from math import *
L1 = [2,3,4,10] #define lists
L2 = [5,3,4,9,10,15]
#Print out numbers that exist in L1 and L2 using set operations
setL1 = set(L1) #make lists into sets so I can use set operations
setL2 = set(L2)
intersection = setL1&setL2 #find intersection
print "Intersection = ", intersection
#Print out numbers that exist in either L1 or L2 but not both using set operations
Union = setL1|setL2 #find all unique numbers in both sets
Either = Union-intersection #subtract out numbers in both sets from unique list
print "In either list but not both = ",Either
#Print out numbers that exist in L1 but not L2
ButNot = setL1-setL2 #set subtraction, to remove values in L2 from L1
print "In L1 but not in L2 = ", ButNot
#Merge L1 and L2 and save as L3
L3 = list(Union) #already did the math, but want it as a list
print "Merge L1 and L2 and save into L3: ", L3
#Append to L2
L2.append(103) #append numbers to the end
L2.append(20)
L2.append(34)
print "Append values to L2: ", L2
print '------------------------------------------------------------------'

#Question2
print "Question 2"
#Starting with 13, add all the odd numbers from 13 up to 999; save to variable sum
TotalSum = 0 #Set beginning number for sum; didn't want to use sum as a variable, since it is already a defined function
VariableSum = 13 #Set value I'm changing; start at 13
while VariableSum<1000: #set range
	if VariableSum%2==1: #identify odd numbers
		TotalSum =TotalSum+VariableSum #add odd numbers to list
	VariableSum+=1 #next element
print "Sum = ",TotalSum
print '------------------------------------------------------------------'

#Question 3
print "Question 3"
#The following code generates 300 random integers: use while loop to print out all the numbers that have factors of 3 and 7
import random
List = []
x=[int(300*random.random()) for i in xrange(300)]
#print x
i = 0
while i<len(x):
	if x[i]%3==0 and x[i]%7==0 and x[i]!=0:
		List.append(x[i])
	i+=1
print "Divisible by 3 and 7:", List
