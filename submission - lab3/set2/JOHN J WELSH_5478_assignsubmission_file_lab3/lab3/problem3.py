#Lab 3 Problem 3 by John Welsh

# 3. The following code generates 300 random integers
# use while loop to print out all the numbers that have factors of 3 and 7
# hint: use % operator


import random
x=[int(300*random.random()) for i in xrange(300)]
i = 0
numbers = []
while i < len(x):
	if x[i]%3 == 0 and x[i]%7 == 0 and x[i] != 0:
		numbers.append(x[i])
	i += 1
print numbers
