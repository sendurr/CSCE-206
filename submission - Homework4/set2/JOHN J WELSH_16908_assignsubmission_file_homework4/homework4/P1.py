from Tkinter import *
root = Tk()

num1_entry = Entry(root)
num1_entry.grid(row = 0, column = 0)
num2_entry = Entry(root)
num2_entry.grid(row = 0, column = 2)

def add():
	try:
		num1 = float(num1_entry.get())
		num2 = float(num2_entry.get())
	except:
		result_label.configure(text='number only')
	result = num1 + num2
	result_label.configure(text='%f' % result)
def subtract():
	try:
		num1 = float(num1_entry.get())
		num2 = float(num2_entry.get())
	except:
		result_label.configure(text='number only')
	result = num1 - num2
	result_label.configure(text='%f' % result)
def multiply():
	try:
		num1 = float(num1_entry.get())
		num2 = float(num2_entry.get())
	except:
		result_label.configure(text='number only')
	result = num1 * num2
	result_label.configure(text='%f' % result)
def divide():
	try:
		num1 = float(num1_entry.get())
		num2 = float(num2_entry.get())
	except:
		result_label.configure(text='number only')
	try: 
		result = num1 / num2
		result_label.configure(text='%f' % result)
	except:
		result_label.configure(text='Division by Zero')

add = Button(root, text= '+', command=add)
add.grid(row = 1, column = 0, columnspan =1)
subtract = Button(root, text= '-', command=subtract)
subtract.grid(row = 1, column = 1, columnspan = 1)
multiply = Button(root, text= '*', command=multiply)
multiply.grid(row = 1, column = 2, columnspan = 1)
divide = Button(root, text= '/', command=divide)
divide.grid(row = 1, column = 3, columnspan = 1)
result_label = Label(root, width=24,text="0")
result_label.grid(row = 3, column = 0)
root.mainloop()
