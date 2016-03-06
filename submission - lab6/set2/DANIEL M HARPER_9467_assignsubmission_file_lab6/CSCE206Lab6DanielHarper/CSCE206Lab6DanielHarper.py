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
#import argparse

# Body Section#######################################################
#--------------------------------------------------------------------
# Q1: Write a program that takes input from user by keyboard
# Make a program that (1) asks the user for the temperature in
# Fahrenheit degrees and reads the numbers; (2) computes the 
# corresponding temperature in Celsius degrees; and (3) prints out
# the temperature in the Celsius scale
# Name of program file: f2c_qa1.py

#--------------------------------------------------------------------
# Q2: take input from command line using sys.argv
# Make a program that reads a temperature in Fahrenheit degrees from command line using sys.argv approach; (2) computes the corresponding temperature in Celsius degrees; and (3) rints out the temperature in the Celsius scale.
# Name of program file: f2c_pq.py
# test you program by running it from the terminal window: 
# python f2c_qa.py

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