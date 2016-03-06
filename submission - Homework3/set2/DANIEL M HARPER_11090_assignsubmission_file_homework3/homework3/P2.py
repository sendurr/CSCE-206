# Author: Daniel Harper
# Assignment: Homework 3 - P2.py
# Original Date: 2/18/2016
# Last Updated:  2/18/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
#import sys

# Body Section#######################################################
#--------------------------------------------------------------------
# Write a function sumoddnumber(numbers), where the input parameter
# is a list of integer numbers. The function will add all the odd 
# numbers in the numbers list and return the sum.
# Test your function by the following statement:
# print “sum=”,sumoddnumber([2,5,7,4,8,3,5])
# It should print out sum=15.

# FUNCTION: sumoddnumber(numbers)------------------------------------
# Description: Calculate the sum of the odd numbers in a list of 
#	numbers
# Input Parameters:
#	numbers : list of integers
# Output : the sum of the odd numbers in the list numbers
def sumoddnumber(numbers):
	output = 0
	for i in numbers:
		if i % 2 == 1:
			output += i
	return output
#--------------------------------------------------------------------

print("sum=",sumoddnumber([2,5,7,4,8,3,5]))
# whoever wrote the question doesn't know how to do math, it's 20