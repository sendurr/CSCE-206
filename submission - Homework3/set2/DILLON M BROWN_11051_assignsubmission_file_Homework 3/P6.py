import argparse
def f(v0,t,g=9.81):
    return v0*t - 0.5*g*t**2

parser=argparse.ArgumentParser()
parser.add_argument('-v',dest='v',help='Initial Velocity')
parser.add_argument('-t',dest='t',help='time')
args=parser.parse_args()

try:
    float(args.v)
except:
    args.v = raw_input("Error: Please enter a valid number for velocity: ")
try:
    float(args.t)
except:
    args.t = raw_input("Error: Please enter a valid time: ")

print f(float(args.v),float(args.t))
