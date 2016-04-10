from Tkinter import *
root = Tk()

root.title("Calculator")
# root.geometry('500x100')

first = Entry(root, width=4)
first.pack(side='left')

second = Entry(root, width=4)
second.pack(side='left')

first_label = Label(root, width=24, text='Enter numbers for operation')
first_label.pack(side='left')

def plus():
	try:
		total = float(first.get()) + float(second.get())
		total_label.configure(text=' %d '%total)
	except:
		first_label.configure(text='number only')
	return total

def minus():
	try:
		total = float(first.get()) - float(second.get())
		total_label.configure(text=' %d '%total)
	except:
		first_label.configure(text='number only')
	return total

def mult():
	try:
		total = float(first.get()) * float(second.get())
		total_label.configure(text=' %d '%total)
	except:
		first_label.configure(text='number only')
	return total

def division():
	try:
		if float(second.get()) == 0:
			total_label.configure(text='Error: division by 0')
		else:
			total = float(first.get()) / float(second.get())
			total_label.configure(text=' %f '%total)
	except:
		first_label.configure(text='number only')
	return total

plusButt = Button(root, text=' + ', command=plus)
plusButt.pack(side='left')
minusButt = Button(root, text=' - ', command=minus)
minusButt.pack(side='left')
multButt = Button(root, text=' * ', command=mult)
multButt.pack(side='left')
divButt = Button(root, text=' / ', command=division)
divButt.pack(side='left')

total_label = Label(root, width=24, text='0')
total_label.pack(side='right')
root.mainloop()