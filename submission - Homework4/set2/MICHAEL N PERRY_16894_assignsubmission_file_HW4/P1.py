from Tkinter import *
root=Tk()
A_entry=Entry(root, width=10)
A_entry.grid(row=0, column=0)
root2=Tk()
B_entry = Entry(root,width=10)
B_entry.grid(row=0, column=2)
def addition():
	A=float(A_entry.get())
	B=float(B_entry.get())
	answer=A+B
	Ans_label.configure(text='%g' %answer)
addition=Button(root, text='+',command=addition)
addition.grid(row=1,column=0)
def subtraction():
	A=float(A_entry.get())
	B=float(B_entry.get())
	answer=A-B
	Ans_label.configure(text='%g' %answer)
subtraction=Button(root, text='-',command=subtraction)
subtraction.grid(row=1,column=1)
def multiplication():
	A=float(A_entry.get())
	B=float(B_entry.get())
	answer=A*B
	Ans_label.configure(text='%g' %answer)
multiplication=Button(root, text='*',command=multiplication)
multiplication.grid(row=1,column=2)
def division():
	A=float(A_entry.get())
	B=float(B_entry.get())
	answer=A/B
	Ans_label.configure(text='%g' %answer)
division=Button(root, text='/',command=division)
division.grid(row=1,column=3)
Ans_label = Label(root, width=7)
Ans_label.grid(row=2,column=2)
Funit_label = Label(root, text='Result:')
Funit_label.grid(row=2, column=0)
root.mainloop()