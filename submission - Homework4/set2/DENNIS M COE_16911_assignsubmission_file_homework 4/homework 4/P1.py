from Tkinter import *
root = Tk()

One_Entry = Entry(root, width=5)
One_Entry.grid(row=0, column=0)
Two_Entry = Entry(root, width=5)
Two_Entry.grid(row=0, column=3)

def addition():
	A = float(One_Entry.get())
	B = float(Two_Entry.get())
	F = A + B
	F_label.configure(text='%g' % F)

def subtraction():
	A = float(One_Entry.get())
	B = float(Two_Entry.get())
	F = A - B
	F_label.configure(text='%g' % F)

def multiplication():
	A = float(One_Entry.get())
	B = float(Two_Entry.get())
	F = A * B
	F_label.configure(text='%g' % F)

def division():
	A = float(One_Entry.get())
	B = float(Two_Entry.get())
	F = A / B
	F_label.configure(text='%g' % F)

addition = Button(root, text='+', height = 2, width=5, command=addition)
addition.grid(row=1, column=0)
subtraction = Button(root, text='-', height = 2, width=5, command=subtraction)
subtraction.grid(row=1, column=1)
division = Button(root, text='/', height = 2, width=5, command=division)
division.grid(row=1, column=2)
multiplication = Button(root, text='*', height = 2, width=5, command=multiplication)
multiplication.grid(row=1, column=3)

F_label = Label(root, width=4)
F_label.grid(row=2, column=3)
Funit_label=Label(root, text='Result')
Funit_label.grid(row=2, column=0)
root.mainloop()
