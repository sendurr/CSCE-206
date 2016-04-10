from numpy import *
import matplotlib.pyplot as plt
from math import *
import sys
g=9.81
v1=float(sys.argv[1])
t1=linspace(0,(2*v1)/g,100)
y1=array((v1*t1)-(0.5*g*t1**2))

v2=float(sys.argv[2])
t2=linspace(0,(2*v2)/g,100)
y2=array((v2*t2)-(0.5*g*t2**2))


v3=float(sys.argv[3])
t3=linspace(0,(2*v3)/g,100)
y3=array((v3*t3)-(0.5*g*t3**2))

plt.plot(t1,y1,'r',t2,y2,'b',t3,y3,'g')
plt.show()