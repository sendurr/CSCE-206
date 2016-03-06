import argparse
def f(v0,t,g=9.81):
    return v0*t - 0.5*g*t**2

parser=argparse.ArgumentParser()
parser.add_argument('-v',dest='v',help='Initial Velocity')
parser.add_argument('-t',dest='t',help='time')
args=parser.parse_args()

print f(float(args.v),float(args.t))
