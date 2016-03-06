# Author: Daniel Harper
# Assignment: Homework 2 - P1.py
# Original Date: 2/4/2016
# Last Updated:  2/8/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random

# Body Section#######################################################
#--------------------------------------------------------------------
# a number series is defined by the following rules. The first two 
# numbers are 0 and 1.  And all the following numbers are defined as
# the sum of previous two numbers.  White a program to generate the 
# first 1000 numbers in this number series with 0, 1 included.

# FUNCTION: fibonacci(n)--------------------------------------------
# Description: Calculate and output the first n number of numbers of 
# the fibbonacci sequence
# Input Parameters:
#	n : integer number to depict the number of sequence numbers 
#		to output
# output : no formal output, but a list of n fibonacci numbers is 
#		printed on the screen
def fibonacci(n):
	i = 0
	X = 0
	Y = 1
	output = []
	while i < n :
		if X < Y:
			X += Y
			output.append(X)
		else:
			Y += X
			output.append(Y)
		i += 1
	print(output)
#--------------------------------------------------------------------

fibonacci(1000)