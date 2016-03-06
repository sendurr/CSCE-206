print "Homework 3 - Question 3"
print ""

def minmaxave(numbers):
	print "Maximum = ", max(numbers)
	print "Minimum = ", min(numbers)
	print "Average =  %.4f"%(sum(numbers)/len(numbers))
numbers = [3,5,2,2.3,5,10,4.2]
minmaxave(numbers)