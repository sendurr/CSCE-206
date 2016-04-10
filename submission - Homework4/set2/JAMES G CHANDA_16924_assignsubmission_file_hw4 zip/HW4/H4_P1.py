from Tkinter import *
from math import *
def evaluate(event):
    res.configure(text = "Result: " + str(eval(entry.get())))
x = Tk()
Label(x, text="Your Expression:").pack()
entry = Entry(x)
entry.bind("<Return>", evaluate)
entry.pack()

result = Label(x)
result.pack()
x.mainloop()

