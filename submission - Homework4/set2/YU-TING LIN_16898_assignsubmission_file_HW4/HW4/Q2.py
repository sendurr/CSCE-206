import numpy as np
import matplotlib.pyplot as ax
import sys

from math import *
from pylab import *
x = np.linspace(-3.14, 3.14)
F = np.exp(x**2)*np.sin(x)

#F, ax = plt.subplots()
ax.plot(x, F)
ax.title('Simple plot')

ax.show()
sys.exit(1)