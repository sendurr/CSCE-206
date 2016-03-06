import argparse
import sys
parser=argparse.ArgumentParser()
parser.add_argument('-t','--t')
parser.add_argument('-v','--v')

args=parser.parse_args()
v0=args.v
t=args.t
try:
	t=float(t)
	v0=float(v0)
except ValueError: 
	t=float(raw_input("Input the t value  once again:"))
	v0=float(raw_input("Input the v0 value once again:"))
	
g=9.81
y=(v0*t)-(0.5*g*t**2)
exec('print "y:",y')