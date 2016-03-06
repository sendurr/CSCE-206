import sys
t= sys.argv[2]
t=float(t)
v0= sys.argv[1]
v0= float(v0)
g= 9.81
y= v0*t-.5*g*t**2
print y

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action= 'store')
parser.add_argument('-v', action= 'store')

args = parser.parse_args()
t=float(args.t)
v= float(args.v0)
g= 9.81
y= v0*t-.5*g*t**2
print y