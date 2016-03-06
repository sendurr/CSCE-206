#3.
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f','--f', type=float,
default=-999.0, help='1st parameter')
parser.add_argument('-c', '--c', type=float,
default=-999.0, help='2nd parameter')

args = parser.parse_args()
f = args.f
c = args.c
 
if f != -999:
	C = (f-32)*(5/9.0)
	print "input(F):",f
	print "output(C):",C 	#C based on equation
if c != -999:
	F = (9.0/5)*(c+32)
	print "input(C):",c
	print "output(F):",F 	#F based on equation