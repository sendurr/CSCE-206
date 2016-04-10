import matplotlib.pyplot as plt
import numpy as np
from numpy import sin

x = np.linspace(-np.pi,np.pi,100)
print x
y=np.exp(x**2)*sin(x)
print y

plt.plot(x,y)
plt.show()