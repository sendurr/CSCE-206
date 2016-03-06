import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='v0', type=float, help='initial velocity')
parser.add_argument('-t', action='store', dest='t', type=float, help='time')                            

args = parser.parse_args()

g = 9.81
y = args.v0*args.t - 0.5*g*args.t**2
print y