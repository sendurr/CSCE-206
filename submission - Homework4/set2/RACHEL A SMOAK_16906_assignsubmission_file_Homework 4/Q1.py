#Rachel Smoak
#27 March 2016
#Homework 4

#Question 1

from Tkinter import *
root = Tk()

No1_entry = Entry(root, width=8)
No1_entry.grid(row = 0, column = 0, columnspan=2, pady = 10, ipadx=10)

No2_entry = Entry(root, width = 8)
No2_entry.grid(row = 0, column = 2, columnspan=2)

def compute(method):
	try:
		No1 = float(No1_entry.get())
		No2 = float(No2_entry.get())
	except:
		Results.configure(text = 'Input numbers only')
	if method == 'add':
		Result = No1+No2
		Results.configure(text = '%.2f' %Result)
	elif method == 'subtract':
		Result = No1 - No2
		Results.configure(text = '%.2f' %Result)
	elif method == 'multiply':
		Result = No1 * No2
		Results.configure(text = '%.2f' %Result)
	elif method == 'divide':
		if No2 == 0:
			Results.configure(text= "Cannot divide by 0")
		else:
			Result = No1/No2
			Results.configure(text = '%.2f' %Result)

add = Button(root, text=' + ', command=lambda: compute('add'))
add.grid(row=3, column = 0, pady=10, ipadx=8)
subtract = Button(root, text=' - ', command=lambda: compute('subtract'))
subtract.grid(row = 3, column = 1, ipadx=8)
multiply = Button(root, text=' * ', command=lambda: compute('multiply'))
multiply.grid(row = 3, column = 2, ipadx=8)
divide = Button(root, text=' / ', command=lambda: compute('divide'))
divide.grid(row = 3, column = 3, ipadx=8)

Results = Label(root, text = "0")
Results.grid(row = 5, column = 3, pady=10)
Results_label = Label(root, text='Result : ')
Results_label.grid(row = 5, column = 1, columnspan = 2)
root.mainloop()