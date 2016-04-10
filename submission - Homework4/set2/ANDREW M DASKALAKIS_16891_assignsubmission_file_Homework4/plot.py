import matplotlib.pyplot as plt
from math import *
from numpy import *

x = linspace(-pi,pi,100)

F = exp(x**2)*sin(x)

plt.plot(x,F)
plt.show()