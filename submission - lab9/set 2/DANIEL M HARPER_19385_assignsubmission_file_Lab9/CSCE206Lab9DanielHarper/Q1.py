# Author: Daniel Harper
# Assignment: Lab9 - Q1.py
# Original Date: 03/31/2016
# Last Updated:  03/31/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
from math import * # basic math functions
#from cmath import * # complex math (solve for algebra equations)
#import random # random number generator
#import matplotlib.pyplot as plt # plotting library
#from numpy import * # arrays, linspaces, most math functions
#import operator # used in sorting dictionaries
#import sys # take input from command line
#import argparse # store input from command line

# Body Section#######################################################
#--------------------------------------------------------------------
# Make a class F that implements the function:
# f(x:a,w) = e^(-ax) * sin(wx)
# A value(x) method computes values of f, while a and w are class
# attributes. Test the class with the following main program:
# from math import *
# f = F(a=1,0,w=0.1)
# print f.value(x=pi)
# f.a = 2
# print f.value(pi)

# CLASS: F()---------------------------------------------------------
# Description: This class will function as the function:
#	f(x:a,w) = e^(-ax) * sin(wx)
#	where x is input, a and w are class items
# Input Parameters:
#	X : numerical value to run the function on
# Output : N/A
class F(object):
	"""docstring for F"""
	def __init__(self, a, w):
		super(F, self).__init__()
		self.a = a
		self.w = w
		
	def value(self, x):
		return exp(-(self.a * x))*sin(self.w * x)

	def printMyValues(self): # used for testing, not required
		print("self.a:",self.a)
		print("self.w:",self.w)
		
		
#--------------------------------------------------------------------
f = F(a=1.0,w=0.1)
print(f.value(x=pi))
# f.printMyValues()
f.a = 2
print(f.value(pi))
#f.printMyValues()