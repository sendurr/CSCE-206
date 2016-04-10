import numpy as np 
import matplotlib.pyplot as py 

x = np.arange(-3.14,3.14,.01)
y = np.exp(x**2)*np.sin(x)

py.plot(x,y)
py.show()