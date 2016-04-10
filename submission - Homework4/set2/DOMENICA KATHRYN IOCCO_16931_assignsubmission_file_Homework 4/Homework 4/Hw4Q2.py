import numpy as np
import matplotlib.pylab as plt
from math import *
x=np.linspace(-3.14,3.14)
y=np.exp(x**2)*np.sin(x)
z, kx = plt.subplots()
kx.plot(x,y)
kx.plot(x,y)
kx.set_title('Single Function Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()