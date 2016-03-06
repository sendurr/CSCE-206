import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v','--v', type=float)
parser.add_argument('-t', '--t', type=float)

args = parser.parse_args()
v0 = args.v
t = args.t
g = 9.81
y=v0*t-0.5*g*t**2
exec('print "y:",y')