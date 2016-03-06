#Q1

F = eval(input("Temperature in Fahrenheit"))
C = (F-32)/(1.8)
print(C)

#Q2

import sys
i = (sys.argv[1])
F = int(i)
C = (F-32)/(1.8)
print(C)

#Q3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("a")
parser.add_argument("b")
args = parser.parse_args()
if args.a == '-f':
	F = int(args.b)
	C = (F-32)/(1.8)
	print(C)
elif args.a == '-c'
	C = int(args.b)
	F = (C*1.8)+32
	print(F)