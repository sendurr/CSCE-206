import sys
from math import *
import matplotlib.pyplot as plt 
from math import *
from numpy import *
import numpy as np
g=9.81
print sys.argv
v0=float(sys.argv[1])
print v0
v1=float(sys.argv[2])
print v1
v2=float(sys.argv[3])
print v2
v3=float(sys.argv[4])
print v3

velocity=(v0,v1,v2,v3)

t=linspace(0,2*v0/g)
t1=linspace(0,2*v1/g)
t2=linspace(0,2*v2/g)
t3=linspace(0,2*v3/g)

y=v0*t-0.5*9.81*t**2
y1=v1*t1-0.5*9.81*t1**2
y2=v2*t2-0.5*9.81*t2**2
y3=v3*t3-0.5*9.81*t3**2
print y, y1, y2, y3


plt.plot(t,y,t1,y1,t2,y2,t3,y3)
plt.xlabel("time")
plt.ylabel("velocity")
plt.title("velocity vs time")
plt.show()
