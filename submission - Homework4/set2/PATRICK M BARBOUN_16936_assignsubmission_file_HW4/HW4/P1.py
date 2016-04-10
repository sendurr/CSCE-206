from Tkinter import *

root = Tk()

x_entry = Entry(root, width=4)
x_entry.pack(side='left')

y_entry = Entry(root, width=4)
y_entry.pack(side='right')

def add():
	try:
		x = float(x_entry.get())
		y = float(y_entry.get())
	except:
		z_label.configure(text='x and y must be numbers')
	z = x+y
	z_label.configure(text='%g' % z)

def sub():
	try:
		x = float(x_entry.get())
		y = float(y_entry.get())
	except:
		z_label.configure(text='x and y must be numbers')
	z = x-y
	z_label.configure(text='%g' % z)

def mult():
	try:
		x = float(x_entry.get())
		y = float(y_entry.get())
	except:
		z_label.configure(text='x and y must be numbers')
 	z = x*y
 	z_label.configure(text='%g' % z)

def div():
 	try:
 		x = float(x_entry.get())
 		y = float(y_entry.get())
 	except:
 		z_label.configure(text='x and y must be numbers')
 	if y == 0:
 		z_label.configure(text='Cannot divide by zero')
 	elif y != 0:
 		z = x/y
 		z_label.configure(text='%g' % z)

z_label = Label(root,text='0')
z_label.pack(side='bottom')
addition = Button(root, text=' + ', command=add)
subtraction = Button(root, text=' - ', command=sub)
multiplication = Button(root, text=' * ', command=mult)
division = Button(root, text=' / ', command=div)
division.pack(side='bottom')
multiplication.pack(side='bottom')
subtraction.pack(side='bottom')
addition.pack(side='bottom')




root.mainloop()

