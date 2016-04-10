from Tkinter import *
from matplotlib.pyplot import *
from numpy import *
from math import *
# root = Tk()
# first_entry = Entry(root, width=5)
# first_entry.pack(side='left')
# second_entry= Entry(root, width= 5)
# second_entry.pack(side='right')
# def compute_add():
#     a = float(first_entry.get())
#     b = float(second_entry.get())
#     c = a + b
#     c_label.configure(text="%g" % c)
# compute_add = Button(root, text=' + ', command=compute_add)
# compute_add.pack()
# def compute_sub():
#     a = float(first_entry.get())
#     b = float(second_entry.get())
#     c = a - b
#     c_label.configure(text="%g" % c)
# compute_sub = Button(root, text=' - ', command=compute_sub)
# compute_sub.pack()
# def compute_mult():
#     a = float(first_entry.get())
#     b = float(second_entry.get())
#     c = a * b
#     c_label.configure(text="%g" % c)
# compute_mult = Button(root, text=' * ', command=compute_mult)
# compute_mult.pack()
# def compute_div():
#     a = float(first_entry.get())
#     b = float(second_entry.get())
#     c = a / b
#     c_label.configure(text="%g" % c)   
# compute_div = Button(root, text=' / ', command=compute_div)
# c_label = Label(root, text='answer')
# c_label.pack(side='bottom')
# compute_div.pack()
# root.mainloop()

e=linspace( -3.14, 3.14, 100)
def f(x):
	p= exp(x**2)* sin(x)
	return p

y=[]
for i in e:
	y.append(f(i))
plot(e,y,'r*')
show(plot)