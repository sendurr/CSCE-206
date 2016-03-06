import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('-v','--v')
parser.add_argument('-t','--t')

args = parser.parse_args()
v0 = args.v
t = args.t
try:
	t=float(t)
	v0=float(v0)
except ValueError: 
	v0=float(raw_input("Please input value for v0 again:"))
	t=float(raw_input("Please input value for t again:"))
g=9.81
y=v0*t-0.5*g*t**2
exec('print "y:",y')