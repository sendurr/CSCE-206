#Q6
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='v',default=0, help='initial velocity')
parser.add_argument('-t', action='store', dest='t',default=0, help='time')
args = parser.parse_args()
g=9.81
v0=eval(args.v)
t=eval(args.t)
y=v0*t -0.5*g*t**2 
print "distance(y)=",y 
