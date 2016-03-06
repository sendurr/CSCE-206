# Author: Daniel Harper
# Assignment: Homework 3 - P5b.py
# Original Date: 2/23/2016
# Last Updated:  2/23/2016
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

g = 9.81
v = eval(args.v)
t = eval(args.t)

y = v*t - 0.5*g*t**2
print(y)