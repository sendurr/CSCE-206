from Tkinter import *
root = Tk()

V_entry = Entry(root, width=4)
V_entry.pack(side='left')

Vunit_label = Label(root, text='initial velocity')
Vunit_label.pack(side='left')

t_entry = Entry(root, width=4)
t_entry.pack(side='left')

tunit_label = Label(root, text='time')
tunit_label.pack(side='left')


def compute():
	try:
		V = float(V_entry.get())
		t = float(t_entry.get())
	except:
		y_label.configure(text='number only')
	y = V*t-0.5*9.81*t**2
	y_label.configure(text='%g' % y)

compute = Button(root, text=' Go ', command=compute)
compute.pack(side='left', padx=4)
y_label = Label(root, width=24,text="0")
y_label.pack(side='left')
yunit_label = Label(root, text='height')
yunit_label.pack(side='left')
root.mainloop()