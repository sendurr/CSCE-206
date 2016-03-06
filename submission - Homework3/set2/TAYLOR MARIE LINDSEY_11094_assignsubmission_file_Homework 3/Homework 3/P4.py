import math

g=9.81
t=float(raw_input('enter time in seconds':))
v0=float(raw_input('enter initial velocity in meters per second':))

y=v0*t-0.5*g*t**2
print 'y:',y,'meters'