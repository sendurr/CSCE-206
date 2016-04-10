from Tkinter import *
root =Tk()

N1_entry = Entry(root, width=4)
N1_entry.grid(row=0, column=0)
N2_entry = Entry(root, width=4)
N2_entry.grid(row=0, column =3)
 
# Nunit_label = Label(root, text='A')
# Nunit_label.pack(side='left')
# Munit_label = Label(root, text='B')
# Munit_label.pack(side='right')

def add():
	A = float(N1_entry.get())
	B = float(N2_entry.get())
	F=A+B
	F_label.configure(text='%g'%F)
def subtract():
	A = float(N1_entry.get())
	B= float(N2_entry.get())
	F=A-B
	F_label.configure(text='%g'%F)
def multiply():
	A = float(N1_entry.get())
	B= float(N2_entry.get())
	F=A*B
	F_label.configure(text='%g'%F)
def divide():
	A = float(N1_entry.get())
	B= float(N2_entry.get())
	F=A/B
	F_label.configure(text='%g'%F)
   
 
add = Button(root, text=' + ', width=4, command=add)
add.grid(row=1, column=0)
subtract = Button(root, text=' - ', width=4, command=subtract)
subtract.grid(row=1, column=1)
multiply = Button(root, text=' * ', width=4, command=multiply)
multiply.grid(row=1, column=2)
divide = Button(root, text=' / ', width=4, command=divide)
divide.grid(row=1, column=3)

F_label = Label(root, width=4)
F_label.grid(row=2, column=3)
Funit_label = Label(root, text='Result')
Funit_label.grid(row=2, column=0)
root.mainloop()
