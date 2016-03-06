import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--v", "--initial_velocity", type=float, default=0.0, help= "initial velocity")
parser.add_argument("--t", "--time", type=float, default=1.0, help="time")
args = parser.parse_args()
v = args.v; t = args.t; g=9.81
y = v*t - 0.5*g*t**2
print(y)