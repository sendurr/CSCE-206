import argparse
import sys

try:
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '-initial_velocity',type=float,default=0,help='input initial velocity value')
	parser.add_argument('-t', '-time',type=float,default=0,help='input time value')                            
	args = parser.parse_args()
	print "v0=",args.v
	print "t=",args.t
	t=args.t
	v0=args.v
	print "y(t)=", v0*t-.5*9.81*t**2
except:
	print "ERROR: Please input again using raw_input function. v0 and t must be numerical values only"