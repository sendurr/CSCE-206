import numpy as np
import matplotlib.pyplot as plt


j = np.linspace(-3.14, 3.14)
k = np.exp(j**2)*np.sin(j)
 
f, ax = plt.subplots()
ax.plot(j, k)
ax.set_title('Plot')
 
plt.show()
