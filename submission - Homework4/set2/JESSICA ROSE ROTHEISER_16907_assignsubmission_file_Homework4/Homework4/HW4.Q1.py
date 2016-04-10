from Tkinter import *
root = Tk()
n1_entry = Entry(root, width=5)
n1_entry.pack(side='left')
n2_entry= Entry(root, width=5)
n2_entry.pack(side='right')

def add():
	x = float(n1_entry.get())
	y = float(n2_entry.get())
	z= x+y
	F_label.configure(text='%g' % z)
def subtract():
	x = float(n1_entry.get())
	y = float(n2_entry.get())
	z= x-y
	F_label.configure(text='%g' % z)
def multiply():
	x = float(n1_entry.get())
	y = float(n2_entry.get())
	z= x*y
	F_label.configure(text='%g' % z)
def divide():
	x = float(n1_entry.get())
	y = float(n2_entry.get())
	z= x/y
	F_label.configure(text='%g' % z)

add = Button(root, text=' + ', command=add)
add.pack(side='left', padx=4) 
subtract = Button(root, text=' - ', command=subtract)
subtract.pack(side='left', padx=4) 
multiply = Button(root, text=' * ', command=multiply)
multiply.pack(side='right', padx=4) 
divide = Button(root, text=' / ', command=divide)
divide.pack(side='right', padx=4) 


F_label = Label(root, width=4)
F_label.pack(side='bottom')
Funit_label = Label(root, text='Result')
Funit_label.pack(side='bottom')
root.mainloop()