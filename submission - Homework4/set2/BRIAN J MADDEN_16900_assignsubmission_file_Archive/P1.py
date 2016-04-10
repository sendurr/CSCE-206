from Tkinter import *
root=Tk()
C_entry=Entry(root, width=10)
C_entry.grid(row=0, column=0)
root2=Tk()
D_entry=Entry(root,width=10)
D_entry.grid(row=0, column=2)

def addition():
	A = float(C_entry.get())
	B = float(D_entry.get())
	F = A+B
	F_label.configure(text='%g' %F)
addition=Button(root, text='+',command=addition)
addition.grid(row=1,column=0)

def subtraction():
	A = float(C_entry.get())
	B = float(D_entry.get())
	F = A-B
	F_label.configure(text='%g' %F)
subtraction=Button(root, text='-',command=subtraction)
subtraction.grid(row=1,column=1)

def multiplication():
	A = float(C_entry.get())
	B = float(D_entry.get())
	F = A*B
	F_label.configure(text='%g' %F)
multiplication=Button(root, text='*',command=multiplication)
multiplication.grid(row=1,column=2)

def division():
	A = float(C_entry.get())
	B = float(D_entry.get())
	F = A/B
	F_label.configure(text='%g' %F)

division=Button(root, text='/',command=division)
division.grid(row=1,column=3)

F_label = Label(root, width=5)
F_label.grid(row=2,column=2)
Funit_label = Label(root, text='results:')
Funit_label.grid(row=2, column=0)

root.mainloop()