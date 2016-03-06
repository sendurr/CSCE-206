import sys
#print sys.argv
if len(sys.argv)-1 >= 3:
	print ("Please enter only two parameters: t and v0")
sys.exit()

v0=float(sys.argv[1])
t=float(sys.argv[2])
g=9.81
y=(v*t)-(0.5*g*t**2)
print (y)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v','--v', type=float)
parser.add_argument('-t','--t', type=float)

args = parser.parse_args()
v = args.v
t = args.t
g=9.81
y=(v*t)-(0.5*g*t**2)
print (y)

