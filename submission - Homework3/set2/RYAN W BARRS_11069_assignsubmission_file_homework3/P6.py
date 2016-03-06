import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('-v','--v', help='velocity')
parser.add_argument('-t','--t', help='time')

args = parser.parse_args()
v0 = args.v
t = args.t
try:
	t=float(t)
	v0=float(v0)
except ValueError: 
	v0=float(raw_input("ERROR Please input v0 again:"))
	t=float(raw_input("ERROR Please input t again:"))

g=9.81
y=v0*t-0.5*g*t**2
print "y =", y