# Author: Daniel Harper
# Assignment: Homework 3 - P5.py
# Original Date: 2/23/2016
# Last Updated:  2/25/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
import sys

# Body Section#######################################################
#--------------------------------------------------------------------
# Consider the simplest program for evaluating the formula
# y(t) = v0t-0.5gt^2 :
# v0 = 3; g = 9.81; t = 0.6
# y = v0*t - 0.5*g*t**2
# print y
#
# write a program to work from the command line with the following 
# command: python p5.py 3 0.6
# which will assign 3 to v0 and 0.6 to t
try:
	g = 9.81
	t = float(sys.argv[1])
	v0 = float(sys.argv[2])
	y = v0*t - 0.5*g*t**2
	print(y)
except:
	print("ERROR: invalid input")