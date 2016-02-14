#Lab 3 Problem 1 by John Welsh

# 1. play with list and set

# L1=[2, 3, 4,10]
# L2=[5,3,4,9,10,15]

# Print out the numbers that exist in both variables L1 and L2 using set operations

# Print out numbers that exists in either L1 or L2, but not both using set operation

# Print out numbers that exist in L1 but not in L2. 

# merge L1 and L2 and save it into variable L3

# Add the following numbers to L2,   103, 20, 34 using  append() function of list. 

L1 = [2, 3, 4, 10]
L2 = [5, 3, 4, 9, 10, 15]
print list(set(L1)&set(L2))
print list(set(L1)-set(L2))+list(set(L2)-set(L1))
print list(set(L1)-set(L2))
L3 = L1+L2
print L3
for value in [103, 20, 34]:
	L2.append(value)
print L2
