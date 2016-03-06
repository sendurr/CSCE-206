#3.
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('-f','--f', type=float, default=-999.0, help='first param')
parser.add_argument('-c', '--c', type=float, default=-999.0, help='second param')

args=parser.parse_args()
f=args.f
c=args.c
 
if f != -999:
	C=(f-32)*(5/9.0)
	print("input(F):",F)
	print("output(C):",C)

if c != -999:
	F=(9.0/5)*(c+32)
	print("input(C):",C)
	print("output(F):",F) 	