# Author: Daniel Harper
# Assignment: Lab 6 - f2c_qa1.py
# Original Date: 2/25/2016
# Last Updated:  2/25/2016
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
# Write a program that takes input from user by keyboard
# Make a program that (1) asks the user for the temperature in
# Fahrenheit degrees and reads the numbers; (2) computes the 
# corresponding temperature in Celsius degrees; and (3) prints out
# the temperature in the Celsius scale
# Name of program file: f2c_qa1.py
BadInput = True 
while BadInput:
	try:
		inputF = float(input("Input your Fahrenheit temperature:"))
		print("Celsius:",(inputF - 32) /(9.0/5.0) )
		BadInput = False
	except:
		print("ERROR: Input must be a number")