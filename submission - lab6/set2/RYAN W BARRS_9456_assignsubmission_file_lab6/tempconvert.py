import argparse
parser = argparse.ArgumentParser(description='Temperature converter')
parser.add_argument('-f', type=int, default=5000, help='unit')
parser.add_argument('-c', type=int, default=5000, help='unit')

args = parser.parse_args()
f=args.f
c=args.c

if f != 5000:
	C = (f-32)*(5/9.0)
	print "input(F):",f
	print "output(C):",C
if c != 5000:
	F = ((9.0/5)*c)+32
	print "input(C):",c
	print "output(F):",F