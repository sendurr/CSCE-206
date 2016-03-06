import sys

def f(v0,t,g=9.81):
    return v0*t - 0.5*g*t**2

args = sys.argv
print f(float(args[1]),float(args[2]))