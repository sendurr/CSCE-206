import numpy as np
import matplotlib.pyplot as plt
import sys

def y(t):
    return v0*t -0.5*g*t**2
g = 9.81

d=[1,2.5,5]
legends = [] 
for v0 in d:
    v0 = float(v0)
    t = np.linspace(0,2*v0/g,100)
    y = v0*t -0.5*g*t**2
    plt.hold(True)
    plt.plot(t,y)
    #egends.append('v0=%g'%v0)
plt.xlabel('time(s)')
plt.ylabel('height(m)')
#legend(legends)
plt.show()