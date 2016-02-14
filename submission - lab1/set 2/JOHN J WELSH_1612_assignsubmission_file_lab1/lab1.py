"""Lab 1 By John Welsh"""

# Learn to store information into variables

# 1. store  2.33, -2, "32233", 'I am a boy' into 4 different variables and then print the variables out

var_1, var_2, var_3, var_4 = 2.33, -2, "32233", 'I am a boy'
print "The four variables in problem 1 are assigned to: %g, %d, %s, %s.\n" % (var_1, var_2, var_3, var_4)

# 2. store a list of numbers into variable called  array1 and print out the numbers of even indexes
# 3,4.0,34,-5,23

array1 = [3, 4.0, 34, -5, 23]
print "The elements corresponding to even indexes are:",
for num in range(0,len(array1),2):
	print array1[num],
print "\n"


# 3. store a list of strings into a variable and print out first and last items.
# "good","very good","excellent"

list_of_strings = ["good", "very good", "excellent"]
print 'The first and last items in the list are: %s, %s\n' % (list_of_strings[0], list_of_strings[-1])


# 4. store a matrix of numbers into a variable m
# 1 2 3
# 4 5 6
# 7 8 9

# print the center number using m with indexes

import numpy as np 
m = np.matrix("1,  2,3; 4, 5, 6; 7, 8, 9")
print "The center number of matrix m is: %g\n" % m[1,1]

