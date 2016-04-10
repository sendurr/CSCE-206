import matplotlib.pyplot as plt
from numpy import *
from math import *

xlist = linspace(-3.14,3.14,100)
def f(x):
	ylist=[]
	for i in x:
		answer = exp(i**2)*sin(i)
		ylist.append(answer)
	return ylist

y = f(xlist)
plt.plot(xlist,y)
plt.title("Homework 4 - Question 2")
plt.show()