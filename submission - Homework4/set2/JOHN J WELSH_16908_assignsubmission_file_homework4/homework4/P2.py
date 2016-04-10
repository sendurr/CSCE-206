import matplotlib.pyplot as plt 
from math import exp, sin
import numpy as np 

def F(x):
	F0 = []
	for i in x:
		F0.append(exp(i**2)*sin(i))
	return F0

x = np.linspace(-3.14,3.14,1000)

plt.figure(1)
plt.plot(x, F(x))
plt.show()


