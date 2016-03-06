# Author: Daniel Harper
# Assignment: Homework 2 - P5.py
# Original Date: 2/4/2016
# Last Updated:  2/11/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random

# Body Section#######################################################
#--------------------------------------------------------------------
# Given n + 1 roots r0, r1,..., rn of a polynomial p(x) of degree 
# n + 1, p(x) can be computed by:
# p(x) = from 0 to n {(x - ri) = (x-ro)(x-r1)...(x-r(n-1))(x-rn)}
# Store the roots r0,...,rn in a list and make a loop that computes 
# the product in (2.3). Test the program on a polynomial with roots 
# -1,1, and 2

# FUNCTION: polynomialRoot(X)----------------------------------------
# Description: Calculate and output the product of the root list.
# The formula is: sum from 0 to n {(x - ri)}
# Input Parameters:
#	X : root list to be looped through to calculate the output
# output : product of the root list
def polynomialRoot(X):
	output = 1
	length = len(X)
	for i in range(length):
		output *= (length - X[i])
	return output
#--------------------------------------------------------------------


rootList = [-1,1,2]
print(polynomialRoot(rootList))