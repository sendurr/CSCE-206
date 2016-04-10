import matplotlib.pyplot as plt 
from math import *
from numpy import *
import numpy as np
x=np.linspace(-3.14,3.14,100)
print x
def f(x):
	answer=exp(x**2)*sin(x)
	return answer
y=np.vectorize(f)
f1=y(x)
print f1

plt.plot(x,f1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()