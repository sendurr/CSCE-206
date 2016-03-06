import sys 
g=9.81
v0=float(sys.argv[1])
t=float(sys.argv[2])
y=int(v0)*int(t)-0.5*g*int(t)**2
print(y)

    