import argparse
parser=argparse.ArgumentParser()

parser.add_argument("-v", type=float)
parser.add_argument("-t", type=float)
args=parser.parse_args()
v=args.v; t=args.t
g=9.81
y=v*t-0.5*g*t**2
print(y)

