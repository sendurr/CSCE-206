# Author: Daniel Harper
# Assignment: Lab 4
# Original Date: 2/11/2016
# Last Updated:  2/11/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
#import sys

# Body Section#######################################################
#--------------------------------------------------------------------
# 1. Set a variable primes to a list containint the numbers 2, 3, 5, 
#	7, 11, and 13. Write out each list element in a for loop. Assign 17
#	to a variable p and add p to the end of the list. Print out the 
#	whole new list. 
primes = [2,3,5,7,11,13]
for i in primes:
	print(i)
primes.append(17)
print(primes)

#--------------------------------------------------------------------
# 2. calculate the sum from k=1 to M of 1/k. Write two programs to 
#	calculate the mathematical sum. One program uses for loop.
#	Another one uses while loop.

# FUNCTION: sumFor(M)------------------------------------------------
# Description: calculate the sum from 1 to M of 1/k using a for loop
# Input Parameters:
#	M : the top of the range for the loop (1-M)
# output : the float number representing the sum of the function in 
#	the description
def sumFor(M):
	output = 0.0
	for k in range(1,M+1):
		output += 1.0/k
	return(output)
#--------------------------------------------------------------------

# FUNCTION: sumWhile(M)----------------------------------------------
# Description: calculate the sum from 1 to M of 1/k using a while
#	loop
# Input Parameters:
#	M : the top of the range for the loop (1-M)
# output : the float number representing the sum of the function in 
#	the description
def sumWhile(M):
	output = 0.0
	k = 1
	while k <= M:
		output += 1.0/k
		k += 1
	return output
#--------------------------------------------------------------------

print("sumFor: ",sumFor(3))
print("sumWhile: ",sumWhile(3))


#--------------------------------------------------------------------
# 3. Store the following matrix into M, and calculate the sum of all 
# the numbers on the boundary
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# sum = 40

# FUNCTION: sumMatrixBorder(Z)---------------------------------------
# Description: calculate and output the sum of the border of a matrix
# Input Parameters:
#	Z : the matrix
# output : the sum of the border of the matrix Z
def sumMatrixBorder(Z):
	output = 0
	x = 0
	y = 0
	while x < len(M):
		while y < len(M[0]):
			if x == 0 or y == 0:
				output += M[x][y]
			elif x == (len(M) - 1) or y == (len(M[0]) - 1):
				output += M[x][y]
			y += 1
		x += 1
		y = 0
	return output
#--------------------------------------------------------------------

M = [[1,2,3],[4,5,6],[7,8,9]]
print("matrix border sum = ", sumMatrixBorder(M))