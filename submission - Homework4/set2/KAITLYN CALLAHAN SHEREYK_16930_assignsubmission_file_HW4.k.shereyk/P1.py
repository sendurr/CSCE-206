# Kate Shereyk
from Tkinter import *
root = Tk()
n1_entry=Entry(root,width=6)
n1_entry.pack(side='left')
n2_entry=Entry(root,width=6)
n2_entry.pack(side='left')
def addition():
	n1=float(n1_entry.get())
	n2=float(n2_entry.get())
	Result=n1+n2
	Result_label.configure(text='%g'%Result)
addition=Button(root,text='+',command=addition)
addition.pack(side='left',padx=6)
def subtraction():
	n1=float(n1_entry.get())
	n2=float(n2_entry.get())
	Result=n1-n2
	Result_label.configure(text='%g'%Result)
subtraction=Button(root,text='-',command=subtraction)
subtraction.pack(side='left',padx=6)
def multiplication():
	n1=float(n1_entry.get())
	n2=float(n2_entry.get())
	Result=n1*n2
	Result_label.configure(text='%g'%Result)
multiplication=Button(root,text='*',command=multiplication)
multiplication.pack(side='left',padx=6)
def division():
	n1=float(n1_entry.get())
	n2=float(n2_entry.get())
	Result=n1/n2
	Result_label.configure(text='%g'%Result)
division=Button(root,text='/',command=division)
division.pack(side='left',padx=6)

Result_label=Label(root,width=6)
Result_label.pack(side='right')
Resultunit_label=Label(root,text='Result=')
Resultunit_label.pack(side='left')
root.mainloop()
