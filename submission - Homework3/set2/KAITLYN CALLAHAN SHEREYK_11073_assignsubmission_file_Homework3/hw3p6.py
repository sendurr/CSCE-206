import sys

v0=float(raw_input("imput a velocity:"))
t=float(raw_input("imput a time:"))
g=9.81

try:
    v0=float(sys.argv[0])
    t=float(sys.argv[1])
except:
    print "Error, the velocity input is incorrect"
    print "Error, the time input is incorrect"
y=v0*t-.5*g*t**2
v0=float(raw_input("Input a correct velocity:"))
t=float(raw_input("Input a correct time:"))
y=v0*t-.5*g*t**2
print y

