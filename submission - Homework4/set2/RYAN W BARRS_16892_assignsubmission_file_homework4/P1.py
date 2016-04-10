from Tkinter import *
root=Tk()
Num_entry1 = Entry(root, width=5)
Num_entry1.pack(side='left')
Num_entry2 = Entry(root, width=5)
Num_entry2.pack(side='left')

def plus():
	N1 = float(Num_entry1.get())
	N2 = float(Num_entry2.get())
	P = N1 + N2
	N_label.configure(text='%g' % P)
def minus():
	N1 = float(Num_entry1.get())
	N2 = float(Num_entry2.get())
	M = N1 - N2
	N_label.configure(text='%g' % M)
def multiply():
	N1 = float(Num_entry1.get())
	N2 = float(Num_entry2.get())
	X = N1 * N2
	N_label.configure(text='%g' % X)
def divide():
	N1 = float(Num_entry1.get())
	N2 = float(Num_entry2.get())
	D = N1 / N2
	N_label.configure(text='%g' % D)

plus = Button(root, text='+', command=plus)
plus.pack(side='left', padx=2)
minus = Button(root, text='-', command=minus)
minus.pack(side='left', padx=2)
multiply = Button(root, text='*', command=multiply)
multiply.pack(side='left', padx=2)
divide = Button(root, text='/', command=divide)
divide.pack(side='left', padx=2)
N_label = Label(root, width=4)
N_label.pack(side='right')
Result_label = Label(root, text='Result:')
Result_label.pack(side='left')
root.mainloop()