import sys
import argparse
#Problem 1--------------------
F=input("What is the temperature?")
print(F+"Degrees(F)")
C=(F-32)*5.0/9.0
print(C+"Degrees(C)")

#Problem 2--------------------
F=float(int(sys.argv[1]))
C=(F-32)*5.0/9.0
print(C,"Degrees(C)")

#Problem 3--------------------
import sys
import argparse
parser=argparse.ArgumentParser()

parser.add_argument("-F", type=float)
parser.add_argument("-C", type=float)
args=parser.parse_args()
F=args.F; C=args.C
if F:
	C=(int(float(F))-32)*5.0/9.0
	print(C,"Degrees C")
if C:
	F=32+(int(float(C)))*(9.0/5.0)
	print(F,"Degrees F")