import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
from math import *

V = int(sys.argv[1])
t = int(sys.argv[2])
# y = V*t-0.5*9.81*t**2

parser.add_argument('initial_velocity','__v0',dest='v0',type=float,default=0,help='initial velocity')
s= args.s0+args.v0*t+0.5*args.a*args.t**2

print '%g is %.1fy' %(y)