from Tkinter import *
root = Tk()

C_entry1 = Entry(root, width=4)
C_entry1.pack(side='left')
C_entry2 = Entry(root, width=4)
C_entry2.pack(side='left')

x=C_entry1.get()
y=C_entry2.get()

def add(x,y):
	s=float(x)+float(y)
	return s
def subtract(x,y):
	s=float(x)-float(y)
	return s
def divide(x,y):
	s=float(x)/float(y)
	return s
def multiply(x,y):
	s=float(x)*float(y)
	return s
compute = Button(root, text='+', command=add)
compute.pack(side='left', padx=4)
compute = Button(root, text='-', command=subtract)
compute.pack(side='left', padx=4)
compute = Button(root, text='/', command=divide)
compute.pack(side='left', padx=4)
compute = Button(root, text='*', command=multiply)
compute.pack(side='left', padx=4)

F_label = Label(root, width=5,text="0")
F_label.pack(side='right')
Funit_label = Label(root, width=5,text='Result:')
Funit_label.pack(side='right')
root.mainloop()