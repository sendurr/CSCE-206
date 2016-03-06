''' Question 3:  write a function called minmaxave(numbers), which will calculate
the maximum, minimum and average values of the given list of numbers and return 
them to the calling statement.
Test your function as below:
print minmaxave([3,5,2.3,5,10,4.2])'''

from math import *
# numbers = ([3,5,2.3,5,10,4.2])
# average = 0
# sum = 0

def minmaxave(numbers):
 # 	maximum = numbers[0]
	# for x in numbers[1:]:
	# 	if x > maximum:
	# 		maximum = x

	# minimum = numbers[0]
	# for y in numbers[1:]:
	# 	if y < minimum:
	# 		minimum = y
	# return minimum and maximum

	# for n in n numbers:
	# 	sum = sum + n
	# average = sum / len(numbers)

	print "Max =", max(numbers)
	print "Min =", min(numbers)
	print "Ave = %.2f"%(sum(numbers)/len(numbers))
numbers = ([3,5,2.3,5,10,4.2])
minmaxave(numbers)


	
#print minmaxave([3,5,2.3,5,10,4.2])
