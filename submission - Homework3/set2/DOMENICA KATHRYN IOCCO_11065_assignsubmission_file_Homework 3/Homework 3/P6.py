import argparse
import math
parser=argparse.ArgumentParser()

try:
	parser.add_argument("-v0", type=float)
	parser.add_argument("-t", type=float)
	args=parser.parse_args()
	v0=args.v0; t=args.t
	g=9.81
	y=v0*t-0.5*g*t**2
	print(y)
except ValueError:
	print("Error: Wrong Values")
if False:
	g=9.81
	v0=input("What is v0?")
	print("v0="+v0)
	t=input("What is t?")
	print("t="+t)
	y=int(float(v0))*int(float(t))-0.5*g*int(float(t))**2
	print(y)