g=9.81
import argparse
parser= argparse.ArgumentParser()
parser.add_argument('-v0', action='store', dest='v', default=0, help="initial velocity")
parser.add_argument('-t', action='store', dest='t', default=0, help="time")
args=parser.parse_args()
# print args.v
# print args.t
# y=v*t-0.5*g*t**2
# print y

try:
	v0=float(args.v0)
except:
	print "Error: Input a numerical value"
	v0=eval(raw_input("v0=?\n"))

try:
	t=float(args.t)
except:
	print "Error: Input must a number"
	t=eval(raw_input("t=?\n"))
y=v0*t-0.5*g*t**2
print y