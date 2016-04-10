from Tkinter import *
root = Tk()
 
first_entry = Entry(root, width=4)
first_entry.pack(side='left')
 
second_entry = Entry(root, width=4)
second_entry.pack(side='right')

def plus():

	try:
		first = float(first_entry.get())

	except Exception:
		ans_label.configure(text='number only')
		ans = first + second
		ans_label.configure(text='%g' % ans)

def minus():
	try:
		first = float(first_entry.get())

    except Exception:
		ans_label.configure(text='number only')
		ans = first - second
		ans_label.configure(text='%g' % ans)    

def divide():
	try:
		first = float(first_entry.get())

    except Exception:
		ans_label.configure(text='number only')
		ans = first / second
		ans_label.configure(text='%g' % ans)

def times():
	try:

		first = float(first_entry.get())

	except Exception:
		ans_label.configure(text='number only')
		ans = first * second
		ans_label.configure(text='%g' % ans)

plus = Button(root, text=' + ', command=plus)
plus.pack(side='left', padx=4)

minus = Button(root, text=' - ', command=minus)
minus.pack(side='left', padx=4)

divide = Button(root, text=' / ', command=divide)
divide.pack(side='right', padx=4)

times = Button(root, text=' * ', command=times)
times.pack(side='right', padx=4)

ans_label = Label(root, width=24,text="0")
ans_label.pack(side='left')
root.mainloop()