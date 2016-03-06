from math import *
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f', action='store', dest='f', default=0, help='Temp in degF')
parser.add_argument('-c', action='store', dest='c',default=0, help='Temp in degC')
parser.add_argument("-v", "--verbosity", action="count", default=0)
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

if args.f:
	Tc = (float(args.f)-32)*(5.0/9)
	print "input: %0.2f degree(F)" %float(args.f)
	print "Output: %0.2f degree(C)" %(Tc)
elif args.c:
	Tf = float(args.c)*(9.0/5)+32
	print "input: %0.2f degree(C)" %float(args.c)
	print "Output: %0.2f degree(F)" %(Tf)	
