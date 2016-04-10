'''Question 2: Plot a figure for the following function
F(x)=exp(2**2)*sin(x) for x in [-3.14, 3.14]'''
# from math import *
# import numpy as np  
# import matplotlib.pyplot as plt  

# def graph(formula, x_range):  
#     x = np.array(x_range)  
#     y = formula(x)
#     plt.plot(x, y)  
#     plt.show()  

# def my_formula(x):
#     return exp(x**2)*sin(x)

#graph(my_formula, range(-3.14, 3.14))

from math import *
from numpy import *
from matplotlib.pylab import *

P= linspace(-3.14, 3.14, 100)

f=[]
for x in P:
	f.append(math.exp(x**2)*sin(x))

plot(P,f)
show()

