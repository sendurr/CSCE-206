from numpy import *
import matplotlib.pyplot as plt
t=linspace(0,2*v0)
v=.5*9.81*t
y=v*t-.5*9.81*t**2
plt.plot(t,y)
plt.show()