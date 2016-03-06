import sys
print (sys.argv)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--initial_velocity','--v0', dest='V0', type=float, default=5, help="initial_velocity")
parser.add_argument('--time','--t', dest='t', type=float, default=0.8, help='time')
args = parser.parse_args()

v0= float(sys.argv[1])
t= float(sys.argv[3])
g = 9.81; v0 = args.v0; t = args.t
y = v0*t-0.5*g*t**2
print(y)

