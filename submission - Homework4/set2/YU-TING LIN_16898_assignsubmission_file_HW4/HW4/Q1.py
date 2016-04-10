from Tkinter import *
root = Tk()
N1_entry = Entry(root, width=5)
N1_entry.pack(side='left')
N2_entry = Entry(root, width=5)
N2_entry.pack(side='left')
def addition():
	N1 = float(N1_entry.get())
	N2 = float(N2_entry.get())
	result = N1+N2
	result_label.configure(text='%g' % result)
addition = Button(root, text=' + ', command=addition)
addition.pack(side='left', padx=5) 
def substraction():
	N1 = float(N1_entry.get())
	N2 = float(N2_entry.get())
	result = N1-N2
	result_label.configure(text='%g' % result)
substraction = Button(root, text=' - ', command=substraction)
substraction.pack(side='left', padx=5) 
def multiplication():
	N1 = float(N1_entry.get())
	N2 = float(N2_entry.get())
	result = N1*N2
	result_label.configure(text='%g' % result)
multiplication = Button(root, text=' * ', command=multiplication)
multiplication.pack(side='left', padx=5)
def division():
	N1 = float(N1_entry.get())
	N2 = float(N2_entry.get())
	result = N1/N2
	result_label.configure(text='%g' % result)
division = Button(root, text=' / ', command=division)
division.pack(side='left', padx=5)

result_label = Label(root, width=4)
result_label.pack(side='right')
resultunit_label = Label(root, text='result:')
resultunit_label.pack(side='right')
root.mainloop()