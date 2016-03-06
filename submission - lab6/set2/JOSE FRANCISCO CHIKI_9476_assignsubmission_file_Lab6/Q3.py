import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-f','-Fahrenheit',type=float,default=0, help='input Fahrenheit temperature')
parser.add_argument('-c','-Celsius',type=float,default=0, help='input Celsius temperature')                            
args = parser.parse_args()

f=args.f
c=args.c

if sys.argv[1]=="-f":
	print "Input:",args.f,"degree(F)"
	print "Output:",(f-32)*(5/9.0),"degree(C)"
elif sys.argv[-1]=="-c":
	"Input:",args.c,"degree(C)"
	print "Output:",(c+32)*(9.0/5),"degree(C)"
else:
	print "Error: try '>python Q3.py -h' for help"
