'''################################################################################
    CSCE 206 Homework4  , Exercise Q1
    FTkinter Calculator
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

from Tkinter import *
root = Tk()

arg1 = Entry(root)
arg1.grid(row=0, column=0)

arg2 = Entry(root)
arg2.grid(row=0, column=2)

def validate(x):
	try:
		float(x)
		return 1
	except Exception:
		return 0

def add_func():

	valid1 =  validate(arg1.get())
	valid2 =  validate(arg2.get())

	if valid1 == 1 and valid2 == 1:
		result = float(arg1.get()) + float(arg2.get())
		result_op.configure(text='%g' % result)
	else:
		if valid1 == 0:
			result_op.configure(text="Invalid arg1")
		else:
			result_op.configure(text="Invalid arg2")


def sub_func():

	valid1 =  validate(arg1.get())
	valid2 =  validate(arg2.get())

	if valid1 == 1 and valid2 == 1:
		result = float(arg1.get()) - float(arg2.get())
		result_op.configure(text='%g' % result)
	else:
		if valid1 == 0:
			result_op.configure(text="Invalid arg1")
		else:
			result_op.configure(text="Invalid arg2")

def mul_func():

	valid1 =  validate(arg1.get())
	valid2 =  validate(arg2.get())

	if valid1 == 1 and valid2 == 1:
		result = float(arg1.get()) * float(arg2.get())
		result_op.configure(text='%g' % result)
	else:
		if valid1 == 0:
			result_op.configure(text="Invalid arg1")
		else:
			result_op.configure(text="Invalid arg2")


def div_func():

	valid1 =  validate(arg1.get())
	valid2 =  validate(arg2.get())

	if valid1 == 1 and valid2 == 1:
		if float(arg2.get()) == 0:
			result_op.configure(text="Arg2 cannot be 0")
		else:
			result = float(arg1.get()) / float(arg2.get())
			result_op.configure(text='%g' % result)
	else:
		if valid1 == 0:
			result_op.configure(text="Invalid arg1")
		else:
			result_op.configure(text="Invalid arg2")



addition = Button(root, text=' + ',bg='red', fg='white', command=add_func)
addition.grid(row=1, column=0, )

subtraction = Button(root, text=' - ', command=sub_func, bg="red", fg="white")
subtraction.grid(row=1, column=1)

Division = Button(root, text=' / ', command=div_func, bg="red", fg="white")
Division.grid(row=1, column=2)

Mulitiplication = Button(root, text=' * ', command=mul_func, bg="red", fg="white")
Mulitiplication.grid(row=1, column=3)

result_text = Label(root, text="Result:")
result_text.grid(row=2, column=0, columnspan=2)

result_op = Label(root,text="0")
result_op.grid(row=2, column=2, columnspan=2)

root.mainloop()


'''################################################################################
    End of Program
################################################################################'''
