# Jeremy Abrams
# CSCE 206
# Homework 4 - Q1.py

from Tkinter import *
root = Tk()

num1_entry = Entry(root,width=4)
num1_entry.pack(fill=X)

num2_entry = Entry(root,width=4)
num2_entry.pack(fill=X)

def add():
	try:
		num1 = float(num1_entry.get())
		num2 = float(num2_entry.get())
	except:
		total_label.configure(text='number only')
	total = num1 + num2
	total_label.configure(text='%g' % total)


def subtract():
	try:
		num1 = float(num1_entry.get())
		num2 = float(num2_entry.get())
	except:
		total_label.configure(text='number only')
	total = num1 - num2
	total_label.configure(text='%g' % total)


def multiply():
	try:
		num1 = float(num1_entry.get())
		num2 = float(num2_entry.get())
	except:
		total_label.configure(text='number only')
	total = num1 * num2
	total_label.configure(text='%g' % total)


def divide():
	try:
		num1 = float(num1_entry.get())
		num2 = float(num2_entry.get())
	except:
		total_label.configure(text='number only')

	if(num2 == 0):
		total_label.configure(text='Cannot divide by 0')
	else:		
		total = num1 / num2
		total_label.configure(text='%g' % total)

result_label = Label(root, text='Result: ')
result_label.pack(fill=X)
total_label = Label(root, width=24,text='0')
total_label.pack(fill=X)

add = Button(root, text='+', command=add)
add.pack(fill=X, side=LEFT)
subtract = Button(root, text='-', command=subtract)
subtract.pack(fill=X, side=LEFT)
multiply = Button(root, text='*', command=multiply)
multiply.pack(fill=X, side=LEFT)
divide = Button(root, text='/', command=divide)
divide.pack(fill=X, side=LEFT)
root.mainloop()