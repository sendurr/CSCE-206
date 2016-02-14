# Author: Daniel Harper
# Assignment: Lab 1 - Learn to store information into variables
# Original Date: 1/15/2016
# Last Updated:  1/21/2016
# Written using Python 3.0
#####################################################################
# Importation Section################################################
from math import *

# Body Section#######################################################
#--------------------------------------------------------------------
# 1. store the following into 4 different variables and then print 
# the variables out ( 2.33, -2, "32233", 'I am a boy')
# print("1. Store four different variables, and print them (2.33, -2, '32233', 'I am a boy')")

doubleNumber = 2.33
negativeNumber = -2
numberString = "32233"
pinocchio = 'I am a boy'

print(doubleNumber)
print(negativeNumber)
print(numberString)
print(pinocchio)


#--------------------------------------------------------------------
# 2. Store a list of numbers into a variable called array1 and print
# out the numbers of even indexes (3, 4.0, 34, -5, 23)
# print("2. Store a list of numbers, print the even indexes (3, 4.0, 34, -5, 23)")

array1 = [3,4.0,34,-5,23]
arrayIndex = 0

for i in array1:
	if arrayIndex % 2 == 0:
		print(i)
	arrayIndex += 1


#--------------------------------------------------------------------
# 3. Store a list of strings into a variable and print out the first
# and last items ("good", "very good", "excellent")	
#print("3. Store a list of strings, print the first and last ('good', 'very good', 'excellent')")

ratingList = ["good", "very good", "excellent"]
arrayIndex = 0

#for i in ratingList:
#	if arrayIndex == 0:
#		print(i)
#	if arrayIndex == len(ratingList) - 1:
#		print(i)
#	arrayIndex += 1
print(ratingList[0])
print(ratingList[-1])


#--------------------------------------------------------------------
# 4. Store a matrix of numbers into a variable m
# 1 2 3
# 4 5 6
# 7 8 9
# Then print the center number using m with indexes
# print("4. Store a matrix, then print the center index using coordinates (center index is a 5)")
m = [[0 for x in range(3)] for x in range(3)]
# print("Initial Matrix:", m)
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
m = [a,b,c]

#mm=[a,b,c,m]
#print("matrix:", mm[1][1])
#print("Final Matrix:  ", m)

mCenterHeight = floor(len(m) / 2) # mathematically determines the center index
mCenterWidth = floor(len(m[0]) / 2)
print(m[mCenterHeight][mCenterWidth])

# End of Program#####################################################