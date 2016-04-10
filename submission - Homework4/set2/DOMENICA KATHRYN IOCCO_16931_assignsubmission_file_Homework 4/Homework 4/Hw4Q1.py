import Tkinter as Tk
from Tkinter import *
import sys

root=Tk()
root.title('Basic Calcualtor')
frame=Frame(root)
frame.pack()

number1=StringVar()
leftframe=Frame(root)
leftframe.pack(side=LEFT)
txtdisplay=Entry(frame, textvariable=number1, bd=10, insertwidth=1, font=20)
txtdisplay.pack(side=LEFT)

number2=StringVar()
topframe=Frame(root)
topframe.pack(side=RIGHT)
txtdisplay=Entry(frame, textvariable=number2, bd=10, insertwidth=1, font=20)
txtdisplay.pack(side=RIGHT)

number3=StringVar()
txtdisplay1=Entry(frame, textvariable=number3, bd=10, insertwidth=1, font=20)
txtdisplay1.pack(side=BOTTOM)

button1=Button(topframe, padx=16, pady=16, bd=8, text="+", fg="black")
button1.pack(side=LEFT)
button2=Button(topframe, padx=16, pady=16, bd=8, text="-", fg="black")
button2.pack(side=LEFT)
button3=Button(topframe, padx=16, pady=16, bd=8, text="*", fg="black")
button3.pack(side=LEFT)
button4=Button(topframe, padx=16, pady=16, bd=8, text="/", fg="black")
button4.pack(side=LEFT)
buttons={}

SignVal=''
FirstVal=1

if SignVal is "+":
    set(int(firstval)+int(v.get()))
elif SignVal is "-":
    set(int(firstval)-int(v.get()))
elif SignVal is "*":
    set(int(firstval)*int(v.get()))
elif SignVal is "/":
    set(int(firstval)/int(v.get()))
else:
    set('')

root.mainloop()

#I couldn't figure out how to return the answers
