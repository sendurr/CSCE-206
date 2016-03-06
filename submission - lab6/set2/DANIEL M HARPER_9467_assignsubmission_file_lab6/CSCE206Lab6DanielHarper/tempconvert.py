# Author: Daniel Harper
# Assignment: Lab 6
# Original Date: 2/25/2016
# Last Updated:  2/25/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
#import sys
import argparse

# Body Section#######################################################
#--------------------------------------------------------------------
# Q3: take input from command line using argparse
# Make a program that reads a temperature in Fahrenheit degree or
# Celsius degree from command line using argparse module and convert 
# to Celsius or Fahrenheit correspondingly. The program should be 
# able to run as below:

# python tempconvert.py -f 100 ==> this should read the temperature
# in Fahrenheit and the program should compute the corresponding 
# temperature in Celsius degrees and print it out as:
#	input: 100 degree(F)
#	output: 37.77 degree(C)

# python tempconvert.py -c 100 ==> this should read the temperature
# in Celsius and the program should compute the corresponding 
# temperature in Fahrenheit degrees and print it out as:
#	input: 100 degree(C)
#	output: 212 degree(F)

BadInput = True 
parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', dest='f', help='degrees Fahrenheit')
parser.add_argument('-c', action='store', dest='c', help='degrees Celsius')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

try:
	inputF = float(eval(args.f))
	print("\tinput: %.2f degrees(F)"%(inputF))
	print("\toutput: %.2f degrees(C)"%((inputF - 32) /(9.0/5.0) ))
except:
	try:
		inputC = float(eval(args.c))
		print("\tinput: %.2f degrees(C)"%(inputC))
		print("\tinput: %.2f degrees(F)"%((9.0/5.0)*inputC + 32))
	except:
		print("ERROR: Invalid Input")