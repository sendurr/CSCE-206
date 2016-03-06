import argparse

parser = argparse.ArgumentParser (description='Convert temperatures.')

parser.add_argument('-v', action='store', dest='v', default=0, help='initial velocity')
parser.add_argument('-t', action='store', dest='t', default=0, help='time')                            
# parser.add_argument("-v", "--verbosity", action="count", default=0)
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

g=9.81

try:
	a=float(args.v)
	b=float(args.t)
	y=a*b-0.5*g*b**2
	print ("y=%.4f"%y)
except:
	print ("Error: Input value is NOT a number! Input again:")
	x=float(raw_input("velocity:?\n"))
	z=float(raw_input("time:?\n"))
	y=x*z-0.5*g*z**2
	print ("y=%.4f"%y)

