#Q1
from tkinter import *
root = Tk()
first_entry = Entry(root, width=5)
first_entry.pack(side='left')

def add():
	A1 = float(first_entry.get())
	A2 = float(second_entry.get())
	A3 = A1 + A2
	results.configure(text='%g'%A3)
addition = Button(root,text='+',command=add)
addition.pack(side='left',padx=8)
def subtract():
	S1 = float(first_entry.get())
	S2 = float(second_entry.get())
	S3 = S1 - S2
	results.configure(text='%g'%S3)
sub = Button(root,text='-',command=subtract)
sub.pack(side='left',padx=8)
def multiply():
	M1 = float(first_entry.get())
	M2 = float(second_entry.get())
	M3 = M1*M2
	results.configure(text='%g'%M3)
mult = Button(root,text='*',command=multiply)
mult.pack(side='left',padx=8)
def divide():
	D1 = float(first_entry.get())
	D2 = float(second_entry.get())
	D3 = D1/D2
	results.configure(text='%g'%D3)
division = Button(root,text='/',command=divide)
division.pack(side='left',padx=8)

second_entry = Entry(root, width=5)
second_entry.pack(side='left')
equal = Label(root,text='=')
equal.pack(side='left')
results=Label(root)
results.pack(side='left')

root.mainloop()

# Q2
import math
import numpy
import pylab
import matplotlib.pyplot as plt

x = numpy.linspace(-3.14,3.14,100)
yf = numpy.e**(x**2)*numpy.sin(x)
pylab.plot(x,yf)
plt.show()

# Q3
import numpy as np
import matplotlib.pyplot as plt
import sys

g = 9.81


def y(t, v0):
    return v0 * t - 0.5 * g * t ** 2

x = plt.subplot()
plt.hold()


def plot_trajectory(v0):
    time_list = np.linspace(0, 2 * v0 / g, 100)
    x.plot(time_list, y(time_list, v0))


speeds = np.array(sys.argv[1:], dtype=np.float)

for x in xrange(len(speeds)):
    plot_trajectory(speeds[x])

plt.show()

#Q4
from numpy import *
def sincos(x):
	for i in x:
		y = []
		a = cos(i)
		b = sin(a)
		y.append(b)
		print(y)
sincos(array([1,3,5,7,10.5]))