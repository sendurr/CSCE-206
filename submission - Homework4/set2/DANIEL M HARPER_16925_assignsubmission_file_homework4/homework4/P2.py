# Author: Daniel Harper
# Assignment: Homework4 - P2.py
# Original Date: 03/23/2016
# Last Updated:  03/24/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
from math import * # basic math functions
#from cmath import * # complex math (solve for algebra equations)
#import random # random number generator
import matplotlib.pyplot as plt # plotting library
from numpy import * # arrays, linspaces, most math functions
#import operator # used in sorting dictionaries
#import sys # take input from command line
#import argparse # store input from command line

# Body Section#######################################################
#--------------------------------------------------------------------
# 2. Plot a figure for the following function
# F(x)= exp(x^2)* sin(x) for x in [-3.14, 3.14]

# define the function F(x) as explained above------------------------
def F(x):
	return exp(x**2)*sin(x)
#--------------------------------------------------------------------
Fv = vectorize(F) # vectorize the function just to be safe/efficient
X = linspace(-3.14,3.14,100)
plt.plot(X,Fv(X),'-')
plt.title("(e^2)*sin(x)")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()