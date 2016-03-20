# Author: Daniel Harper
# Assignment: Lab 7 - Calculator.py
# Original Date: 3/1/2016
# Last Updated:  3/1/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
import sys
import argparse
#import matplotlib.pyplot as plt
#from numpy import *


# Body Section#######################################################
#--------------------------------------------------------------------
# Write a calculator program that accepts commands from command line.
# The program has the following function when executed:
# python Calculator.py * 5 4 => will print out 5*4=20
# python Calculator.py + 5 4 => will print out 5+4=9
# python Calculator.py - 5 4 => will print out 5-4=1
# python Calculator.py / 5 4 => will print out 5/4=1
# python Calculator.py / 5 0 => will print out
# error: denominator cannot be 0.

firstNumber = 0
secondNumber = 0
operation = ""

try:
	operation = str(sys.argv[1])
	firstNumber = str(sys.argv[2])
	secondNumber = str(sys.argv[3])
except:
	print("ERROR: Input Error")

try:
	if operation == "/" and secondNumber == "0":
		print("ERROR: denominator cannot be 0")
	else:
		print(firstNumber + operation + secondNumber + "=" + str(eval(firstNumber+operation+secondNumber)))
except:
	print("ERROR: evaluation error")