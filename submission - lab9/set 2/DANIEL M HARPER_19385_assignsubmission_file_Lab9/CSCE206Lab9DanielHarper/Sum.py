# Author: Daniel Harper
# Assignment: Lab9 - Sum.py
# Original Date: 03/31/2016
# Last Updated:  03/31/2016
# Written using Python 3.4.3.7
# All rights reserved
# HEAVILY SOURCED FROM: 
#https://github.com/noahwaterfieldprice/python_primer/blob/master/ch_7/Sum.py
#####################################################################
# Importation Section################################################
#from math import * # basic math functions
#from cmath import * # complex math (solve for algebra equations)
#import random # random number generator
#import matplotlib.pyplot as plt # plotting library
from numpy import * # arrays, linspaces, most math functions
#import operator # used in sorting dictionaries
#import sys # take input from command line
#import argparse # store input from command line
import sympy as sy
# Body Section#######################################################
#--------------------------------------------------------------------
# READ THE DOCUMENT Exercies 7.18 - too much stuff to type out here

# FUNCTION: factorial(n)---------------------------------------------
# Description: Calculate the factorial of n (recursively)
# Input Parameters:
#	n : the integer we are to calculate the factorial for
# Output : the numerical factorial of n
#--------------------------------------------------------------------
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

# CLASS: Sum()-------------------------------------------------------
class Sum(object):
	"""docstring for Sum"""
	def __init__(self, fx, M, N):
		super(Sum, self).__init__()
		self.fx = fx # this needs to be the function we are summing
		self.M = M # lower bound
		self.N = N # upper bound
		self.first_neglected_term = None
		self.lastSum = None

	def __call__(self, x):
		S = 0
		f_k, M, N = self.fx, self.M, self.N
		for k in range(M, N + 1):
			S += self.fx(x, k)
		# calcuate and store next term in the series
		self.first_neglected_term = self.fx(x, N + 1)
		return S
#--------------------------------------------------------------------

# FUNCTION: table(term, x, M, Nlist, f)------------------------------
# Description: Format and print a table with the results of the 
#	function and its inputs
# Input Parameters:
#	term : the function being tested. Must be pre-defined
#	   x : the simple input parameter for the function in term
#	   M : starting point for the summation
#	Nlist : list containing the end points of the summation
#	   f : function for print at top of table for labeling
# Output : No proper output, but the table containing the data is 
#		print to the screen
#--------------------------------------------------------------------
def table(term, x, M, Nlist, f):
	# print top of table
    print('=' * 70)
    print('%-18s %-17s %-17s %-17s'%('x=%1.10f'%x, "f (approx.)", 'Error', 'Next term'))
    print('-' * 70)
    for N in Nlist:
        S = Sum(term, M, N)
        #print("S:",S.first_neglected_term)
        print('N = %-8d | %16.6E  %16.6E  %16E'%(N, S(x), f(x) - S(x), S.first_neglected_term))
    print('=' * 70 + '\n')

# FUNCTION: taylor1(x,k)---------------------------------------------
# Description: Taylor approximation of 1/(1+x)
# Input Parameters:
#	x : value to tested in the taylor approximation
#	k : value of the power to raise x to 
# Output : the approximate taylor summation
#--------------------------------------------------------------------
def taylor1(x,k):
	return (-x)**k
#--------------------------------------------------------------------

# FUNCTION: taylor2(x,k)---------------------------------------------
# Description: Taylor approximation of sin(x)
# Input Parameters:
#	x : value to tested in the taylor approximation
#	k : value of the power to raise x to 
# Output : the approximate taylor summation
#--------------------------------------------------------------------
def taylor2(x, k): 
	return ((-1)**k*(x**(2*k+1)))/float(factorial(2*k+1))

# FUNCTION: taylor3(x,k)---------------------------------------------
# Description: Taylor approximation of ln(1 + x)
# Input Parameters:
#	x : value to tested in the taylor approximation
#	k : value of the power to raise x to 
# Output : the approximate taylor summation
#--------------------------------------------------------------------
def taylor3(x, k): 
    return (1/float(k))*(x/float(1+x))**k

#TEST CODE///////////////////////////////////////////////////////////
x = 0.5
print("x = ", x)
print()
#t taylor1
S = Sum(taylor1, M=0, N=100)
print('f(x) = 1/(1+x)')
print("From 0 to 100")
print("Summation:",S(x))
print("1st neglection:",S.first_neglected_term)

# taylor2
print('\nf(x) = sin(x)')
for x in (pi, 30 * pi):
    table(taylor2, x, M=0, Nlist=(5, 10, 20), f=sin)

# taylor3
print('\nf(x) = ln(1 + x)')
for x in (2, 5, 10):
    table(taylor3, x, M=1, Nlist=(5, 10, 20), f=log)
