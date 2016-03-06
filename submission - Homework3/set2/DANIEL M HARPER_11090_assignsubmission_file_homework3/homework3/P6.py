# Author: Daniel Harper
# Assignment: Homework 3 - P6.py
# Original Date: 2/23/2016
# Last Updated:  2/23/2016
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
# Modify the program p5b.py in P5 so that when user input wrong value
# for v0 and t, it will report an error and ask the user to input it
# agin using raw_input function. (use try-except statement)
#
# P5b.py question:
# Consider the simplest program for evaluating the formula
# y(t) = v0t-0.5gt^2 :
# v0 = 3; g = 9.81; t = 0.6
# y = v0*t - 0.5*g*t**2
# print y
#
# write a program to work from the command line with the following 
# command: python p5b.py -v 5 -t 0.8
# which will assign 5 to v0 and 0.8 to t (use argparse module)

parser = argparse.ArgumentParser()
parser.add_argument('-g', action='store', dest='g',default=9.81, help='gravity value')
parser.add_argument('-v', action='store', dest='v',default=0, help='initial velocity value')
parser.add_argument('-t', action='store', dest='t',default=0, help='time value')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

badInput = True
try:
	g = 9.81
	v = eval(args.v)
	t = eval(args.t)
	y = v*t - 0.5*g*t**2
	print(y)
except:
	print("ERROR: INVALID INPUT - Please input valid values")
	while badInput:
		try:
			t = float(input("Input the time (t > 0):"))
			v = float(input("input the initial velocity (v0 > 0):"))
			y = v*t - 0.5*g*t**2
			print(y)
			badInput = False
		except:
			print("ERROR: REALLY? JUST PUT VALID INPUTS SO I CAN FINISH!!!")
			continue

