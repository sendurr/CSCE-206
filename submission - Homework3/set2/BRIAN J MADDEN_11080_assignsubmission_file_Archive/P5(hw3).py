import sys
print(sys.argv)

g=9.81
v0=float(sys.argv[1])
t=float(sys.argv[2])
y=(v0*t)-(0.5*g*t**2)
print("y:", y)