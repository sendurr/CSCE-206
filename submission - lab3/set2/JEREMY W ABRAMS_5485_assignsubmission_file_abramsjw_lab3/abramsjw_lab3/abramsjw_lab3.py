# Jeremy Abrams
# CSCE 206
# Lab 3
# February 2, 2016

# Question 1

# Create and instantiate L1 and L2
L1 = [2, 3, 4, 10]
L2 = [5, 3, 4, 9, 10, 15]

print "Question 1 Answers:"
# Use set operations to determine which values are in L1 and L2
intersect = set(L1) & set(L2)
print "Intersection: ",intersect

# Use set operations to determine which values are in L1 or L2, but not both
unique = set(L1) ^ set(L2)
print "Unique Numbers: ", unique

# Use set operations to determine what is in L1 but not L2
difference = set(L1) - set(L2)
print "L1 Unique Numbers: ", difference

# Merge L1 and L2 into a new array
L3 = L1 + L2
print "Merged List: ", L3

# Add new values to end of L2
L2.append(103)
L2.append(20)
L2.append(34)

print "Appended List: ", L2

print '\n'
# Question 2

# Create an index variable for the while loop and set it equal to 13.
index = 13

# Create a total variable to use to add up all odd numbers between 13 and 999.
total = 0

# While loop to add all odd numbers between 13 and 999.
while index < 999:
	total = total + index
	index = index + 2

print "Question 2 Answer: "
print total, "\n"


# Question 3

print "Question 3 Answer: "
# Randomly generate 300 numbers between 0 and 300. 
import random
x = [int(300*random.random()) for i in xrange(300)]

i = 0

# Loop through the array and find values that are multiples of 3 and 7.
while i < len(x):
	if x[i]%3==0 and x[i]%7==0:
		print x[i]
	i= i + 1

