from Tkinter import *
root = Tk()

y_entry = Entry(root)
y_entry.grid(row=0, column=0, columnspan=2)

x_entry = Entry(root)
x_entry.grid(row=0, column=2, columnspan=2)

def add():
    y = float(y_entry.get())
    x = float(x_entry.get())
    f = y + x
    f_label.configure(text='%g' % f)
	
add = Button(root, text=' + ', command=add)
add.grid(row=1, column=0)

def subtract():
    y = float(y_entry.get())
    x = float(x_entry.get())
    f = y - x
    f_label.configure(text='%g' % f)
	
subtract = Button(root, text=' - ', command=subtract)
subtract.grid(row=1, column=1)

def multiply():
    y = float(y_entry.get())
    x = float(x_entry.get())
    f = y*x
    f_label.configure(text='%g' % f)
	
multiply = Button(root, text=' * ', command=multiply)
multiply.grid(row=1, column=2)

def divide():
    y = float(y_entry.get())
    x = float(x_entry.get())
    f=y/x
    f_label.configure(text='%g' % f)
	
divide = Button(root, text=' / ', command=divide)
divide.grid(row=1, column=3)

f_label = Label(root)
f_label.grid(row=2, column=2, columnspan=2)

Label(root, text='Result:').grid(row=2, column=0, columnspan=2)

root.mainloop()





