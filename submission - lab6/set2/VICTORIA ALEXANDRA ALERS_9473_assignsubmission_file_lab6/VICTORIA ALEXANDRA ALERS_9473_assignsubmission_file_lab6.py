#1-------------------------------------------------
F=input("what is the tempurature in Fahrenheit?")
print("input:",F,"Degree(F)")
C=((F-32)*5)/9.0
print("output:",C,"Degree(C)")
#2--------------------------------------------------
import sys
F=float(sys.argv[1])
C=((F-32)*5)/9.0
print("output:",C,"Degree(C)")
#3-------------------------------------------------
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=float)
parser.add_argument("-c", type=float)
args = parser.parse_args()
f = args.f; c=args.c 
if f:
	C=((int(float(f))-32)*5.0)/9.0
	print("input:",f,"Degree(F)")
	print("output:",C,"degree(C)")
if c:
	F=32+(9.0*int(float(c))/5.0)
	print("input:",c,"Degree(C)")
	print("output:",F,"degree(F)")