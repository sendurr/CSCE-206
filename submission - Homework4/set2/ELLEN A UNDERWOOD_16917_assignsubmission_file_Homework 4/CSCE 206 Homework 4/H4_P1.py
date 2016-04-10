from Tkinter import *
root = Tk()
Entry1 = Entry(root, width=5)
Entry1.pack(side='left')
Entry2 = Entry(root, width=5)
Entry2.pack(side="left")


def add():
		ans = (float(Entry1.get())+float(Entry2.get()))
		ans_label.configure(text='%g' % ans)
def sub():		
		ans = (float(Entry1.get())-float(Entry2.get()))
		ans_label.configure(text='%g' % ans)
def mult():	
		ans = (float(Entry1.get())*float(Entry2.get()))
		ans_label.configure(text='%g' % ans)
def div():	
		ans = (float(Entry1.get())/float(Entry2.get()))
		ans_label.configure(text='%g' % ans)



add = Button(root, text=' + ', command=add)
sub = Button(root, text=' - ', command=sub)
mult = Button(root, text=' * ', command=mult)
div = Button(root, text=' / ', command=div)
add.pack(side='left', padx=4) 
sub.pack(side='left', padx=4) 
mult.pack(side='left', padx=4) 
div.pack(side='left', padx=4) 

ans_label = Label(root, width=10)
ans_label.pack(side='left')
root.mainloop()