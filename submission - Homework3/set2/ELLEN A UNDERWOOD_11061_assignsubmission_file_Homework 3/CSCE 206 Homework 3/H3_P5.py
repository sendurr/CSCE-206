import sys

g=9.81

v0=float(sys.argv[0])
t=float(sys.argv[2])
y=v0*t-0.5*g*t**2
print (y)


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='v')
parser.add_argument('-t', action='store', dest='t')                            
args = parser.parse_args()
v0=float(v)
t=float(t)
y=v0*t-0.5*g*t**2
print (y)
