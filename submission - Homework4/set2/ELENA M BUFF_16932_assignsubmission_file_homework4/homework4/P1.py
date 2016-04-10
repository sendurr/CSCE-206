from Tkinter import *
root = Tk()

entry_A = Entry(root, width=10)  #input text box, put in root window, with width of 4
entry_A.grid(row=0, column=0)  #how to arrange input box in window

root2 = Tk()

entry_B = Entry(root, width=10)  #input text box, put in root window, with width of 4
entry_B.grid(row=0, column=2)  #how to arrange input box in window

def plus():   #defining compute function
	try:
	   	A = float(entry_A.get())  #gets value from input box and converts to float
		B = float(entry_B.get())    
	except:
		F_label.configure(text='number only')
	F = A + B
	F_label.configure(text='%g' % F)  #updates F label with new value     
plus = Button(root, text=' + ', command=plus)  #button after Celcius to compute
plus.grid(row=1,column=0)

def minus():   #defining compute function
	try:
	   	A = float(entry_A.get())  #gets value from input box and converts to float
		B = float(entry_B.get())    
	except:
		F_label.configure(text='number only')
	F = A - B
	F_label.configure(text='%g' % F)  #updates F label with new value     
minus = Button(root, text=' - ', command=minus)  #button after Celcius to compute
minus.grid(row=1,column=1)

def times():   #defining compute function
	try:
	   	A = float(entry_A.get())  #gets value from input box and converts to float
		B = float(entry_B.get())    
	except:
		F_label.configure(text='number only')
	F = A * B
	F_label.configure(text='%g' % F)  #updates F label with new value     
times = Button(root, text=' * ', command=times)  #button after Celcius to compute
times.grid(row=1,column=2)

def dividedby():   #defining compute function
	try:
	   	A = float(entry_A.get())  #gets value from input box and converts to float
		B = float(entry_B.get())    
	except:
		F_label.configure(text='number only')
	F = A / B
	F_label.configure(text='%g' % F)  #updates F label with new value     
dividedby = Button(root, text=' / ', command=dividedby)  #button after Celcius to compute
dividedby.grid(row=1,column=3)

F_label = Label(root, width=10)  #label showing F value, initially empty

F_label.pack(side='left')
F_label.grid(row=2,column=2)
Funit_label = Label(root, text='Result:')  #fixed label
Funit_label.grid(row=2, column=0)
root.mainloop()
