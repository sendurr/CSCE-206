from numpy import *
import matplotlib.pyplot as plt
x=linspace(-3.14,3.14)
y=exp(x**2)*sin(x)
plt.plot(x,y)
plt.show()