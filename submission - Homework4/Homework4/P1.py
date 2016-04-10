#Homework 4.1
from Tkinter import *

root = Tk()
num1_entry = Entry(root,width = 4)
num1_entry.pack(side= 'left')
num2_entry = Entry(root,width = 4)
num2_entry.pack(side= 'left')


def compute1():
    try:
        float(num1_entry.get())
        float(num2_entry.get())
    except:
        F_label.configure(text='enter a number')
    a = float(num1_entry.get())
    b = float(num2_entry.get())
    s = a + b
    F_label.configure(text='%g' % s)
def compute2():
    try:
        float(num1_entry.get())
        float(num2_entry.get())
    except:
        F_label.configure(text='enter a number')
    a = float(num1_entry.get())
    b = float(num2_entry.get())
    s = a - b
    F_label.configure(text='%g' % s)
def compute3():
    try:
        float(num1_entry.get())
        float(num2_entry.get())
    except:
        F_label.configure(text='enter a number')
    a = float(num1_entry.get())
    b = float(num2_entry.get())
    s = a / b
    F_label.configure(text='%g' % s)
def compute4():
    try:
        float(num1_entry.get())
        float(num2_entry.get())
    except:
        F_label.configure(text='enter a number')
    a = float(num1_entry.get())
    b = float(num2_entry.get())
    s = a * b
    F_label.configure(text='%g' % s)


compute1 = Button(root, text=' + ',command = compute1)
compute2 = Button(root, text=' - ',command = compute2)
compute3 = Button(root, text=' / ',command = compute3)
compute4 = Button(root, text=' * ',command = compute4)
compute1.pack(side='left', padx=4)
compute2.pack(side='left', padx=4)
compute3.pack(side='left', padx=4)
compute4.pack(side='left', padx=4)


F_label = Label(root, width=24,text="0")
F_label.pack(side='left')
Funit_label = Label(root, text='Answer')
Funit_label.pack(side='left')
root.mainloop()