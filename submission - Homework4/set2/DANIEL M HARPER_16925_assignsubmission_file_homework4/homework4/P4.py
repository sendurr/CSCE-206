# Author: Daniel Harper
# Assignment: Homework4 - P4.py
# Original Date: 03/24/2016
# Last Updated:  03/24/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
from math import * # basic math functions
#from cmath import * # complex math (solve for algebra equations)
#import random # random number generator
#import matplotlib.pyplot as plt # plotting library
#from numpy import * # arrays, linspaces, most math functions
import numpy as np
#import operator # used in sorting dictionaries
#import sys # take input from command line
#import argparse # store input from command line

# Body Section#######################################################
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Define an array based vectorization function sincos(x) so that you
# can compute:. This function will calculate the sin(cos(x)) for each
# value of the input vector/array x.
# from numpy import *
# def sincos(x):
#	result=… to be finished by you
# 	return result
# x=array([1,3,5,7,10.5])
# y=sincos(x)
# print y


# FUNCTION: sincos(x)------------------------------------------------
# Description: Calculate sin(cos(x)) based on input x and output it
# Input Parameters:
#	x : Input number to be use for the trigonometric function on 
# Output : sin(cos(x))
def sincos(x):
	try:
		return np.sin(np.cos(x))
	except:
		return "CALCULATION ERROR"
#--------------------------------------------------------------------
x=[1,3,5,7,10.5]
y=sincos(x)
print(y)