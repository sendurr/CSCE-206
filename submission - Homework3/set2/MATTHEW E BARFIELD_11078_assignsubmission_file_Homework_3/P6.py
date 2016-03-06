print "Homework 3 - Question 6"
print ""

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-v", action="store", dest="v", default=0, help="Initial Velocity")
parser.add_argument("-t", action="store", dest="t", default=0, help="Time")
args = parser.parse_args()

g=9.81

try:
	v=eval(args.v)
	t=eval(args.t)
	y=v*t-0.5*g*t**2
	print "Distance = ",y
except:
	print "Input is Not a Number"