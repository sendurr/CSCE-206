# Name: Lucke Oliveira Luz			Assignment: Homework 4        Exercise: 1

from Tkinter import *
import tkMessageBox

root = Tk()
x_entry = Entry(root,width=4,font='Arial 12 bold',justify='center')
x_entry.grid(ipadx=20,ipady=20,column=0,row=0,columnspan=2)
y_entry = Entry(root,width=4,font='Arial 12 bold',justify='center')
y_entry.grid(ipadx=20,ipady=20,column=2,row=0,columnspan=2)
def add():
	try:
		x = float(x_entry.get())
		y = float(y_entry.get())
	except:
		z_label.configure(text='Input must be numeric',width=25)
	z = x + y
	z_label.configure(text='%.2f'%(z),width=5)
def minus():
	try:
		x = float(x_entry.get())
		y = float(y_entry.get())
	except:
		z_label.configure(text='Input must be numeric',width=25)
	z = x - y
	z_label.configure(text='%.2f'%(z),width=5)
def mult():
	try:
		x = float(x_entry.get())
		y = float(y_entry.get())
	except:
		z_label.configure(text='Input must be numeric',width=25)
	z = x * y
	z_label.configure(text='%.2f'%(z),width=5)
def div():
	try:
		x = float(x_entry.get())
		y = float(y_entry.get())
	except:
		z_label.configure(text='Input must be numeric',width=25)
	z = x / y
	z_label.configure(text='%.2f'%(z),width=5)

plus = Button(root,text='+',command=add,font='Arial 12 bold',justify='center',width=4)
plus.grid(column=0,row=1,ipadx=10,ipady=10)
minus = Button(root,text='-',command=minus,font='Arial 12 bold',justify='center',width=4)
minus.grid(column=1,row=1,ipadx=10,ipady=10)
mult = Button(root,text='*',command=mult,font='Arial 12 bold',justify='center',width=4)
mult.grid(column=2,row=1,ipadx=10,ipady=10)
div = Button(root,text='/',command=div,font='Arial 12 bold',justify='center',width=4)
div.grid(column=3,row=1,ipadx=10,ipady=10)
result = Label(root,text='RESULT =',font='Arial 12 bold',justify='center')
result.grid(column=0,row=2,ipadx=10,ipady=10,columnspan=2)
z_label = Label(root,font='Arial 12 bold',justify='center')
z_label.grid(column=2,row=2,ipadx=10,ipady=10,columnspan=2)

root.mainloop()