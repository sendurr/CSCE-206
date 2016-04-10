from numpy import *
import matplotlib.pyplot as plt
from math import *

def f(x):
	return exp(x**2)*sin(x)
x=linspace(-3.14,3.14,100)
fv=vectorize(f)
y1=fv(x)
plt.plot(x,y1,'r')
plt.show()


