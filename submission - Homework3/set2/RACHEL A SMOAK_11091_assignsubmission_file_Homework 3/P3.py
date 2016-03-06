#Rachel Smoak
#Homework 3
#28 February 2016

#Question 3
import numpy
def minmaxave(numbers):
	print "Maximum value: ",max(numbers) #numpy has functions for this
	print "Minimum value: ",min(numbers)
	print "Mean value: ", "%.3f" %numpy.mean(numbers)

minmaxave([3,5,2.3,5,10,4.2])