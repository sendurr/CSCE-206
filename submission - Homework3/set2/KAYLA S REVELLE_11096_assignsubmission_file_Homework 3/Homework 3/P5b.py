import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='v',default=0, help='Farenheit Temperature: ')
parser.add_argument('-t', action='store', dest='t',default=0, help='Celsius Temperature: ')
args = parser.parse_args()


g=9.81
v=float(args.v)
t=float(args.t)
y=v*t-0.5*g*t**2

print (y)
