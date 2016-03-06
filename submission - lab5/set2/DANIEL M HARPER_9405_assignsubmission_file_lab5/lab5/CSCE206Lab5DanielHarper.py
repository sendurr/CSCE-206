# Author: Daniel Harper
# Assignment: Lab 5
# Original Date: 2/16/2016
# Last Updated:  2/16/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
#import sys
#import argparse

# Body Section#######################################################
#--------------------------------------------------------------------
# Q1: define a function called printstar(n), which will print n 
# number of '*' on a single line. (Hint, add a ',' at end of print 
# statement will keep next print to output at same line) test your
# function by calling:
# printstar(1)
# printstar(10)
# printstar(100)

# FUNCTION: printstar(n)---------------------------------------------
# Description: Print n number of stars on a line
# Input Parameters:
#	n : integer number to depict the number of stars to print
# Output : no formal output, but a string of stars will be printed
def printstar(n=1):
	print("*"*n)
#--------------------------------------------------------------------

printstar(1)
printstar(10)
printstar(100)

#--------------------------------------------------------------------
# Q2: define a function call printstarx, which has two parameters.
# n parameter specifies how many stars to print on each row parameter
# specify how many rows to print stars the row parameter should have
# a default value as 1. so this function will print a couple of rows,
# each row composed of n stars. You can call printstar(n) function in
# Q1 to work out this problem. test your function by calling:
# printstarx(10)  #which should print 1 row with 10 stars
# printstarx(10,5)# should print 5 rows, each with 10 stars

# FUNCTION: printstarx(n)--------------------------------------------
# Description: Print n number of stars on a x lines
# Input Parameters:
#	n : integer number to depict the number of stars to print
#	x : integer number to depict the number of rows to print stars on
# Output : no formal output, but a string of stars will be printed on 
#	n rows
def printstarx(n,x=1):
	for i in range(x):
		printstar(n)
#--------------------------------------------------------------------

printstarx(10)
printstarx(10,5)


#--------------------------------------------------------------------
# Q3: (optional) define a function that test if an integer number 
# is a prime number the function should return true or false.
# def checkprime(n):
# 	#your code here
# 	#hint, you just need to check if there is any number x from 2 
# to n-1 that makes n%x==0. if so, it is not a prime, return false.
# otherwise return true.
# test your function by:
# print checkprime(3)  #shoud get true
# print checkprime(255) #should get false

# FUNCTION: checkprime(n)--------------------------------------------
# Description: Determine if a number is prime
# Input Parameters:
#	n : integer number to depict the number to check if prime
# Output : binary true or false depending on if n is prime
def checkprime(n):
	i = 2
	while i < n:
		if n % i == 0:
			return False
		i += 1 
	return True
#--------------------------------------------------------------------

print(checkprime(3))  #should get true
print(checkprime(255)) # should get false


















