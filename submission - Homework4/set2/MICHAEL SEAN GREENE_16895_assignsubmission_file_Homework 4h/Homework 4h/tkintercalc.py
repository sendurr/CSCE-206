from Tkinter import *

root = Tk()

x_entry = Entry(root, width=4)
x_entry.pack(side='left')

y_entry = Entry(root, width=4)
y_entry.pack(side='left')

# define the functions for the calculator buttons
def addition():
    x = float(x_entry.get())
    y = float(y_entry.get())  
    F = x + y  
    F_label.configure(text='%g' % F)

# define the buttons after the funtion
addition = Button(root, text=' +', command=addition)
addition.pack(side='left', padx=4)

def subtract():
    x = float(x_entry.get())
    y = float(y_entry.get())  
    F = x - y  
    F_label.configure(text='%g' % F)

subtract = Button(root, text=' -', command=subtract)
subtract.pack(side='left', padx=4)

def multi():
    x = float(x_entry.get())
    y = float(y_entry.get())  
    F = x * y  
    F_label.configure(text='%g' % F)

multi = Button(root, text=' *', command=multi)
multi.pack(side='left', padx=4)

def divide():
    x = float(x_entry.get())
    y = float(y_entry.get())  
    F = x / y  
    F_label.configure(text='%g' % F)

divide = Button(root, text=' /', command=divide)
divide.pack(side='left', padx=4)

# use labels to make calculator presentable
F_label = Label(root, width=4)
F_label.pack(side='right')
Funit_label = Label(root, text='=')
Funit_label.pack(side='left')
root.mainloop()