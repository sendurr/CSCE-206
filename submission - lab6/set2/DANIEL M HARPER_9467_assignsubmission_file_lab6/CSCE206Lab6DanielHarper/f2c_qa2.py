# Author: Daniel Harper
# Assignment: Lab 6 - f2c_qa.py
# Original Date: 2/25/2016
# Last Updated:  2/25/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
import sys
import argparse

# Body Section#######################################################
#--------------------------------------------------------------------
# take input from command line using sys.argv
# Make a program that reads a temperature in Fahrenheit degrees from
# command line using sys.argv approach; (2) computes the
# corresponding temperature in Celsius degrees; and (3) prints out
# the temperature in the Celsius scale.
# Name of program file: f2c_pq2.py
# test you program by running it from the terminal window: 
# python f2c_qa2.py 25

BadInput = True 

f = sys.argv[1]
print(f)
while BadInput:
	try:
		inputF = float(f)
		print("Celsius:",(inputF - 32) /(9.0/5.0) )
		BadInput = False
	except:
		print("ERROR: Input must be a number")
		f = input("Input your Fahrenheit temperature:")