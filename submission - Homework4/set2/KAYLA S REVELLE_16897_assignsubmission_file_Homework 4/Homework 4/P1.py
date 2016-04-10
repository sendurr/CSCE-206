from Tkinter import *
root = Tk()

numberone_entry = Entry(root, width=5)
numberone_entry.grid(row=0, column=0)
numbertwo_entry = Entry(root, width=5)
numbertwo_entry.grid(row=0, column=3)
def add():
	A = float(numberone_entry.get())
	B = float (numbertwo_entry.get())
	F = A + B 
	F_label.configure(text='%g' % F)
def subtract():
	A = float(numberone_entry.get())
	B = float (numbertwo_entry.get())
	F = A - B 
	F_label.configure(text='%g' % F)
def multiply():
	A = float(numberone_entry.get())
	B = float (numbertwo_entry.get())
	F = A * B 
	F_label.configure(text='%g' % F)
def divide():
	A = float(numberone_entry.get())
	B = float (numbertwo_entry.get())
	F = A / B 
	F_label.configure(text='%g' % F)
add = Button(root, text='+', height = 2, width = 5,command =add)
add.grid(row=1, column=0) 
subtract = Button(root, text='-', height = 2, width = 5, command=subtract)
subtract.grid(row=1, column=1)
multiply = Button(root, text='*', height = 2, width = 5, command=multiply)
multiply.grid(row=1, column=2)
divide = Button(root, text ='/', height = 2, width = 5, command=divide)
divide.grid(row=1, column=3)
F_label = Label(root, width = 4)
F_label.grid(row=2, column=3)
Funit_label=Label(root, text='Result')
Funit_label.grid(row=2, column=0)
root.mainloop()
