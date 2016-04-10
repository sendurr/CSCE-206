#Rachel Smoak
#27 March 2016
#Homework 4

#Question 2

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1*np.pi, np.pi, 0.1)
y = np.exp(x**2)*np.sin(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('F(x) = exp(x^2)*sin(x)')
plt.show()