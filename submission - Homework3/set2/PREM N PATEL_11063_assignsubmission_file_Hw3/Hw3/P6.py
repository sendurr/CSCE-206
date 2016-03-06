import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store', dest='time',default=0, help='time')
parser.add_argument('-v0', action='store', dest='v0',default=0, help='initial velocity')                            
parser.add_argument("-v", "--verbosity", action="count", default=0)
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

g = 9.81
try:
	t = float(args.time)
	v0 = float(args.v0)
except:
	print "ERROR: input t and v0 values"
	t = float(raw_input("t: "))
	v0 = float(raw_input("v0: "))
y = v0*t-0.5*g*t**2
print "y = %f"%y