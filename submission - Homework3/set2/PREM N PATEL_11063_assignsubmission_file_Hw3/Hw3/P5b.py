import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store', dest='time',default=0, help='time')
parser.add_argument('-v0', action='store', dest='v0',default=0, help='initial velocity')                            
parser.add_argument("-v", "--verbosity", action="count", default=0)
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

g = 9.81
y = float(args.v0)*float(args.time)-0.5*g*float(args.time)**2
print "y = %f"%y