g=9.81
import argparse
parser= argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='v', default=0, help="initial velocity")
parser.add_argument('-t', action='store', dest='t', default=0, help="time")
args=parser.parse_args()
print args.v
print args.t

v=eval(args.v)
t=eval(args.t)
y=v*t-0.5*g*t**2
print y

