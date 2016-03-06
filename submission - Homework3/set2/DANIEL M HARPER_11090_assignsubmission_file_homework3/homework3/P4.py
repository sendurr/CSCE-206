# Author: Daniel Harper
# Assignment: Homework 3 - P4.py
# Original Date: 2/18/2016
# Last Updated:  2/25/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
#import sys

# Body Section#######################################################
#--------------------------------------------------------------------
# Prompt the user for input to a formula
# Consider the simplest program for evaluating the formula
# y(t) = v0t - 0.5tt^2:
# v0 = 3; g = 9.81; t = 0.6
# y = v0*t - 0.5*g*t**2
# print y
# Modify this code so that the program asks the user questions t=? 
# and v0=?, and then gets t and v0 from ther user's input through
# the keyboard

# Test Case
# v1 = 3; g = 9.81; t = 0.6
# Z = v1*t - 0.5*g*t**2
# print("test case:",Z)

BadInput = True
while BadInput:
	try:
		t = float(input("Input your t value:"))
		v0 = float(input("Input your v0 value:"))
		g = 9.81
		y = v0*t - 0.5*g*t**2
		print(y)
		BadInput = False
	except:
		print("ERROR: Invalid Input - Reinput valid input")