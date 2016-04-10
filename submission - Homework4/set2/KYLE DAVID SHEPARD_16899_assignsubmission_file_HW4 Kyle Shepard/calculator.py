from Tkinter import *
root = Tk()

num1_entry = Entry(root, width=15)
num1_entry.pack(side='left')

num2_entry = Entry(root, width=15)
num2_entry.pack(side='left')

def add():
    n1 = float(num1_entry.get())
    n2 = float(num2_entry.get())
    result=n1+n2
    result_label.configure(text='%g' % result)

def sub():
    n1 = float(num1_entry.get())
    n2 = float(num2_entry.get())
    result=n1-n2
    result_label.configure(text='%g' % result)

def mult():
    n1 = float(num1_entry.get())
    n2 = float(num2_entry.get())
    result=n1*n2
    result_label.configure(text='%g' % result)

def div():
    n1 = float(num1_entry.get())
    n2 = float(num2_entry.get())
    result=n1/n2
    result_label.configure(text='%g' % result)

add = Button(root, text=' + ', command=add)
add.pack(side='left', padx=4)

sub = Button(root, text=' - ', command=sub)
sub.pack(side='left', padx=4)

mult = Button(root, text=' * ', command=mult)
mult.pack(side='left', padx=4)

div = Button(root, text=' / ', command=div)
div.pack(side='left', padx=4)

result_label = Label(root, width=15)
result_label.pack(side='left')

root.mainloop()