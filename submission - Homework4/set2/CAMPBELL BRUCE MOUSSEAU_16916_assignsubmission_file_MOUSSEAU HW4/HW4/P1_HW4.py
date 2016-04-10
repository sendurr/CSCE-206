import sys
from Tkinter import *
root = Tk()

yinput=Entry(root)
xinput=Entry(root)

yinput.grid(row=0, column=0, columnspan=2)
xinput.grid(row=0, column=2, columnspan=2)

def Button1():
    y=float(yinput.get())
    x=float(xinput.get())
    f=y+x
    flabel.configure(text='%g' % f)
Button1 = Button(root, text=' + ', command=Button1)
Button1.grid(row=1, column=0)

def Button2():
    y=float(yinput.get())
    x=float(xinput.get())
    f=y-x
    flabel.configure(text='%g' % f)
Button2 = Button(root, text=' - ', command=Button2)
Button2.grid(row=1, column=1)

def Button3():
    y=float(yinput.get())
    x=float(xinput.get())
    f=y/x
    flabel.configure(text='%g' % f)
	
Button3=Button(root, text=' / ', command=Button3)
Button3.grid(row=1, column=3)

def Button4():
    y=float(yinput.get())
    x=float(xinput.get())
    f=y*x
    flabel.configure(text='%g' % f)
Button4 = Button(root, text=' * ', command=Button4)
Button4.grid(row=1, column=2)

flabel = Label(root)
flabel.grid(row=2, column=2, columnspan=2)

Label(root, text='Result:').grid(row=2, column=0, columnspan=2)
root.title('Calculator')

root.mainloop()
