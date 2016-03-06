# Author: Daniel Harper
# Assignment: Homework 3 - P3.py
# Original Date: 2/18/2016
# Last Updated:  2/25/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
#import sys

# Body Section#######################################################
#--------------------------------------------------------------------
# write a function called minmaxave(numbers), which will calculate
# the maximum, minimum and average values of the given list of
# numbers and return them to the calling statement.
# Test your function as below:
# print minmaxave([3,5,2.3,5,10,4.2])
# Should print out: 10, 2.3,4.916

# FUNCTION: minmaxave(numbers)---------------------------------------
# Description: Calculate and output the max, min, and average of the
#	list of numbers
# Input Parameters:
#	numbers : list of integer numbers
# Output : tuple of 3 float numbers for the max, min, and ave of the 
#	numbers list
def minmaxave(numbers):
	minimum = float(numbers[0])
	maximum = float(numbers[0])
	average = 0.0
	for i in numbers:
		average += i
		if i > maximum:
			maximum = i
		if i < minimum:
			minimum = i
	average = average/len(numbers)
	return minimum,maximum,average
#--------------------------------------------------------------------
a = [3,5,2.3,5,10,4.2]
b = minmaxave(a)
print("Min:",b[0])
print("Max:",b[1])
print("Ave:",b[2])