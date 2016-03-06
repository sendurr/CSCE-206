from Tkinter import *
root = Tk()

F_entry = Entry(root, width=4)  #input text box, put in root window, with width of 4
F_entry.pack(side='left')  #how to arrange input box in window

Funit_label = Label(root, text='Fahrenheit')  #fixed text that doesn't change "Fahrenheit", label object and put it into root window
Funit_label.pack(side='left')  #we want it on the left
def compute():   #defining compute function
    try:
    	F = float(F_entry.get())  #gets value from input box and converts to float
    except:
    	C_label.configure(text='number only')
    C = (F - 32) * (5./9) #converts from F to C
    C_label.configure(text='%g' % C)  #updates C label with new value
     
compute = Button(root, text=' is ', command=compute)  #button after Celcius to compute
compute.pack(side='left', padx=4)
C_label = Label(root, width=24)  #label showing F value, initially empty
C_label.pack(side='left')
Cunit_label = Label(root, text='Celcius')  #fixed label
Cunit_label.pack(side='left')
root.mainloop()