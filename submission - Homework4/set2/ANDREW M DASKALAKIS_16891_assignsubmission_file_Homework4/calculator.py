from Tkinter import *
root = Tk()

xval = Entry(root, width=10)
xval.grid(column=0,row=0,columnspan=5)
yval = Entry(root, width=10)
yval.grid(column=0,row=1,columnspan=2)

#Cunit_label = Label(root, text='Celsius')
#Cunit_label.pack(side='left')
def add():
	try:
		x = float(xval.get())
		y = float(yval.get())
	except:
		answer.configure(text='numbers only')
	z = x+y
	answer.configure(text='%g' % z)

def sub():
	try:
		x = float(xval.get())
		y = float(yval.get())
	except:
		answer.configure(text='numbers only')
	z = x-y
	answer.configure(text='%g' % z)

def mult():
	try:
		x = float(xval.get())
		y = float(yval.get())
	except:
		answer.configure(text='numbers only')
	z = x*y
	answer.configure(text='%g' % z)

def div():
	try:
		x = float(xval.get())
		y = float(yval.get())
	except:
		answer.configure(text='numbers only')
	z = x/y
	answer.configure(text='%g' % z)

add = Button(root, text=' + ', command=add)
add.grid(column=1,row=0)
sub = Button(root, text=' - ', command=sub)
sub.grid(column=1,row=1)
mult = Button(root, text=' * ', command=mult)
mult.grid(column=2,row=0)
div = Button(root, text=' / ', command=div)
div.grid(column=2,row=1)


answer = Label(root, width=24,text="0")
answer.grid(column=0,row=2)


#Funit_label = Label(root, text='Fahrenheit')
#Funit_label.pack(side='left')
root.mainloop()