# Author: Daniel Harper
# Assignment: Lab9 - Q2.py
# Original Date: 03/31/2016
# Last Updated:  03/31/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import * # basic math functions
#from cmath import * # complex math (solve for algebra equations)
#import random # random number generator
#import matplotlib.pyplot as plt # plotting library
#from numpy import * # arrays, linspaces, most math functions
#import operator # used in sorting dictionaries
#import sys # take input from command line
#import argparse # store input from command line

# Body Section#######################################################
#--------------------------------------------------------------------
# Make a class "Simple" with one attribute "i", one method "double",
# which replaces the value of i by i+i, and a constructor that 
# initializes the attribute. Try out the follwing code for testing
# the class:
# s1 = Simple(4)
# for i in range(4):
#	s1.double()
# print(s1.i)
#
# s2 = Simple('Hello')
# s2.double()
# s2.double()
# print(s2.i)
# s2.i = 100
# print(s2.i)

# CLASS: Simple()----------------------------------------------------
# Description: This class is to track 1 object and double it when the
#	function double is called
# Input Parameters:
#	i : attribute that contains the variable (can be numerical or 
#		string)
# Output : N/A
class Simple(object):
	"""docstring for Simple"""
	def __init__(self, i):
		super(Simple, self).__init__()
		self.i = i

	def double(self):
		self.i = self.i + self.i

	def printI(self):
		print(self.i)
#--------------------------------------------------------------------

s1 = Simple(4)
for i in range(4):
	s1.double()
print(s1.i)

s2 = Simple('Hello')
s2.double()
s2.double()
print(s2.i)
s2.i = 100
print(s2.i)