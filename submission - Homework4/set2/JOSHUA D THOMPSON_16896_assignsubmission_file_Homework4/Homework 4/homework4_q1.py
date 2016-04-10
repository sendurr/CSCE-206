# Question 1 for Homework 4

from Tkinter import *
root = Tk()

C_entry = Entry(root, width=10)
C_entry.pack(side='top')
D_entry = Entry(root, width=10)
D_entry.pack(side='top')
def compute():
	C = float(C_entry.get())
	D = float(D_entry.get())
	F = C + D
	F_label.configure(text='%g' % F)
def compute1():
	C = float(C_entry.get())
	D = float(D_entry.get())
	F = C - D
	F_label.configure(text='%g' % F)
def compute2():
	C = float(C_entry.get())
	D = float(D_entry.get())
	F = C/float(D)
	F_label.configure(text='%g' % F)
def compute3():
	C = float(C_entry.get())
	D = float(D_entry.get())
	F = C*D
	F_label.configure(text='%g' % F)
compute = Button(root, text=' + ', command=compute)
compute.pack(side='left', padx=6)
compute = Button(root, text=' - ', command=compute1)
compute.pack(side='left', padx=6)
compute = Button(root, text=' / ', command=compute2)
compute.pack(side='right', padx=6)
compute = Button(root, text=' * ', command=compute3)
compute.pack(side='right', padx=6) 
F_label = Label(root, width=6)
F_label.pack(side='bottom')
Funit_label = Label(root, text='Result')
Funit_label.pack(side='left')
root.mainloop()