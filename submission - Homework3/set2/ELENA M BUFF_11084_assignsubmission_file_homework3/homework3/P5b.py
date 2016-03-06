import argparse

parser = argparse.ArgumentParser (description='Convert temperatures.')

parser.add_argument('-v', action='store', dest='v', default=0, type=float, help='initial velocity')
parser.add_argument('-t', action='store', dest='t', default=0, type=float, help='time')                            
# parser.add_argument("-v", "--verbosity", action="count", default=0)
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

g=9.81
a=args.v
b=args.t
y=a*b-0.5*g*b**2

print ("y=%.4f"%y)
