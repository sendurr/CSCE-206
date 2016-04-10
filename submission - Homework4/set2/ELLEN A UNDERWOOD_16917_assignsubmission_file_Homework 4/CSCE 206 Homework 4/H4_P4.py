import numpy as np
from numpy import *
from math import *
import matplotlib.pyplot as plt

def sincos(x):
		return sin(cos(x))

x=np.array([1,3,5,7,10.5])

b=linspace(-3.14,3.14,100)
for i in x:
	sincosv=vectorize(sincos)
	y=sincosv(b)
print (y)