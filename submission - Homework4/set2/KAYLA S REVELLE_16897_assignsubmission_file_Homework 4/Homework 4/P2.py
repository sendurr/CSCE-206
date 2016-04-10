import matplotlib.pyplot as plt
import numpy as np
from math import exp
from math import sin

i=np.linspace(-3.14,3.14,100)
def F(x):
	graph = exp(x**2)*sin(x)
	return graph

G=np.vectorize(F)
F1=G(i)
plt.xlabel('x')
plt.ylabel('y')

plt.plot(i,F1)
plt.show()